import re
import keyword

reserved_words = keyword.kwlist

tokens_regex = [
    (r'\b(?:{})\b'.format('|'.join(reserved_words)), 'keyword'),  # Palabras clave
    (r'\b\d+\b', 'number'),  # Números
    (r'(["\'])(?:(?=(\\?))\2.)*?\1', 'string'),  # Cadenas de texto
    (r'#[^\n]*', 'comment'),  # Comentarios
    (r'\b[a-zA-Z_]\w*\b', 'identifier'),  # Identificadores
    (r'[+\-*/%<>=&|^~]', 'operator'),  # Operadores
    # Añadir más expresiones regulares según sea necesario
]

# Función para resaltar los tokens en HTML+CSS
def highlight_tokens(code):
    highlighted_code = code
    for token_regex, token_class in tokens_regex:
        highlighted_code = re.sub(token_regex, r'<span class="{}">\g<0></span>'.format(token_class), highlighted_code)
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
        .keyword {{ color: blue; }}
        .number {{ color: orange; }}
        .string {{ color: green; }}
        .comment {{ color: gray; }}
        .identifier {{ color: black; }}
        .operator {{ color: purple; }}
    </style>
</head>
<body>
    <pre>{highlighted_code}</pre>
</body>
</html>"""

# Escribe el código HTML en un archivo
with open("highlighted_code.html", "w") as file:
    file.write(html_code)
