import re
import keyword

reserved_words = keyword.kwlist
variables = ['float', 'int', 'double', 'string']


tokens_regex = [

    (r'"[^"\n]*"', 'stringS'),
    (r"'[^'\n]*'", 'stringD'),
    (r'\b(?:{})\b'.format('|'.join(reserved_words)), 'keyword'),  # Palabras clave
    (r'\b\d+\b', 'number'),  # Números
    (r'#[^\n]*', 'comment'),  # Comentarios
    (r'[+\-*/%<>=&|^~()]', 'operator'),  # Operadores
    (r'\b(?:{})\b'.format('|'.join(variables)), 'variable'),  # Variables
    (r'\b\w+\(\)', 'function'),  # Funciones sin argumentos

]
# Función para resaltar los tokens en HTML+CSS
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
        * {{background-color: rgb(41, 38, 46); font-family: "JetBrains Mono", monospace; color: white;}}
        .keyword {{ color: rgb(212, 93, 93); }}
        .number {{ color: rgb(235, 122, 255); }}
        .stringS {{ color: rgb(255, 251, 0); }}
        .stringD {{ color: rgb(255, 251, 0); }}
        .comment {{ color: gray; }}
        .identifier {{ color: rgb(255, 255, 255); }}
        .operator {{ color: rgb(212, 93, 93); }}
        .variable {{color: #6f35f8;}}
        .function {{color: #00ff62;}}
    </style>
</head>
<body>
    <pre>{highlighted_code}</pre>
</body>
</html>"""

# Escribe el código HTML en un archivo
with open("highlighted_code.html", "w") as file:
    file.write(html_code)