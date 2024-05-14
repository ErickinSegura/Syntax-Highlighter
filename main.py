import time
import re
import keyword

inicio = time.time()


reserved_words = keyword.kwlist
variables = ['float', 'int', 'double', 'string', 'f']

tokens_regex = [
    (r'\b(?:{})\b'.format('|'.join(variables)), 'variable'),  # Variables
    (r'\b\w+\(', 'function'),  # Funciones sin argumentos
    (r'"[^"\n]*"', 'stringS'),
    (r"'[^'\n]*'", 'stringD'),
    (r'\b(?:{})\b'.format('|'.join(reserved_words)), 'keyword'),  # Palabras clave
    (r'\b\d+(\.\d*)?([eE][+-]?\d+)?\b', 'number'),  # Números
    (r'#[^\n]*', 'comment'),  # Comentarios
    (r'[+\-*/%<>=&|^~()\[\]{}]', 'operator'),  # Operadores
]


# Función para resaltar los tokens en HTML+CSS
def highlight_tokens(code):
    # Inicializamos el código resaltado como una cadena vacía
    highlighted_code = ''
    # Inicializamos el índice de inicio del próximo token
    start_index = 0
    # Buscamos coincidencias con todas las expresiones regulares en tokens_regex
    for match in re.finditer('|'.join(f'({pattern})' for pattern, _ in tokens_regex), code):
        # Extraemos el token y su posición en el código
        token = match.group(0)
        token_start = match.start()
        token_end = match.end()
        # Agregamos el texto no resaltado que precede al token
        highlighted_code += code[start_index:token_start]
        # Buscamos la clase correspondiente al token en tokens_regex
        for token_regex, token_class in tokens_regex:
            if re.match(token_regex, token):
                # Aplicamos la clase correspondiente al token
                if (token_class == 'function'):
                    highlighted_code += f'<span class="{token_class}">{token[:-1]}</span>'
                    highlighted_code += f'<span class="operator">(</span>'
                    break

                highlighted_code += f'<span class="{token_class}">{token}</span>'
                break
            
        # Actualizamos el índice de inicio del próximo token
        start_index = token_end
    # Agregamos el texto no resaltado que sigue al último token
    highlighted_code += code[start_index:]
    return highlighted_code


# Lee el archivo fuente
with open("fuente.py", "r") as file:
    source_code = file.read()

# Resalta los tokens en HTML+CSS
highlighted_code = highlight_tokens(source_code)

# Genera el código HTML completo
html_code = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resaltado de sintaxis en Python</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&display=swap');
        * {{background-color: rgb(30, 30, 46); font-family: "JetBrains Mono", monospace; color: white;}}
        .keyword {{ color: rgb(243, 139, 168); }}
        .number {{ color: rgb(203, 166, 247); }}
        .stringS {{ color: rgb(249, 226, 175); }}
        .stringM {{ color: rgb(249, 226, 175); }}
        .stringD {{ color: rgb(249, 226, 175); }}
        .comment {{ color: rgb(166, 173, 200); }}
        .identifier {{ color: rgb(255, 255, 255); }}
        .operator {{ color: rgb(243, 139, 168); }}
        .variable {{color: rgb(137, 180, 250);}}
        .function {{color: rgb(166, 227, 161);}}
    </style>
</head>
<body>
    <pre>{highlighted_code}</pre>
</body>
</html>"""

# Escribe el código HTML en un archivo
with open("highlighted_code.html", "w") as file:
    file.write(html_code)

fin = time.time()

print(f"Tiempo de ejecución: {(fin-inicio):.6f} segundos")