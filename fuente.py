d = [
        {'letra': 5, 'digito': 1, 'simbolo': 8, 'comentario': 6, '_': 9, '.': 2, 'E': 5, "espacio": 9},  # Estado 0   0       Entrada
        {'letra': 9, 'digito': 1, 'simbolo': 9, 'comentario': 6, '_': 9, '.': 2, 'E': 9, "espacio": 9},  # Estado N1         1       Entero
        {'letra': 9, 'digito': 2, 'simbolo': 9, 'comentario': 6, '_': 9, '.': 9, 'E': 3, "espacio": 9},  # Estado N2         2       Real
        {'letra': 9, 'digito': 4, 'simbolo': 10, 'comentario': 6, '_': 9, '.': 9, 'E': 9, "espacio": 9},  # Estado N3         3
        {'letra': 9, 'digito': 4, 'simbolo': 9, 'comentario': 6, '_': 9, '.': 9, 'E': 9, "espacio": 9},  # Estado N4         4       Real
        {'letra': 5, 'digito': 5, 'simbolo': 9, 'comentario': 6, '_': 5, '.': 9, 'E': 5, "espacio": 9},  # Estado V1         5       Variable
        {'letra': 9, 'digito': 9, 'simbolo': 9, 'comentario': 7, '_': 9, '.': 9, 'E': 9, "espacio": 9},  # Estado C1         6       Division
        {'letra': 7, 'digito': 7, 'simbolo': 7, 'comentario': 7, '_': 7, '.': 7, 'E': 7, "espacio": 7},  # Estado C2         7       Comentario
        {'letra': 9, 'digito': 9, 'simbolo': 9, 'comentario': 6, '_': 9, '.': 9, 'E': 9, "espacio": 9},  # Estado S1         8       Simbolo
        {'letra': 9, 'digito': 9, 'simbolo': 9, 'comentario': 9, '_': 9, '.': 9, 'E': 9, "espacio": 9},  # Estado Null       9
        {'letra': 9, 'digito': 10, 'simbolo': 9, 'comentario': 6, '_': 9, '.': 9, 'E': 9, "espacio": 9},  # Estado real       10      Real
        ]

alfabeto = {
    'letra': 'abcdfghijklmnñopqrstuvwxyzABCDFGHIJKLMNÑOPQRSTUVWXYZ',
    'digito': '0123456789',
    'simbolo': '+-*=()^%',
    'comentario': '//',
    '_': '_',
    '.': '.',
    'E': 'Ee',
    'espacio': ' ',
}


dict_estado = {
    0: 'Entrada',
    1: 'Entero',
    2: 'Real',
    3: 'Real',
    4: 'Real',
    5: 'Variable',
    6: 'Division',
    7: 'Comentario',
    8: 'Simbolo',
    9: 'Nulo',
    10: 'Real'
}


dict_simbolo = {
    '+': 'Suma',
    '-': 'Resta',
    '*': 'Multiplicacion',
    '=': 'Asignacion',
    '(': 'Parentesis que abre',
    ')': 'Parentesis que cierra',
    '^': 'Potencia',
    '%': 'Porcentaje'
}

# Función para obtener el estado de un token en el autómata
def dame_estado(token, prev_estado=0):
  # Busca el token en el alfabeto y devuelve el estado correspondiente
  for categoria, conjunto_caracteres in alfabeto.items():
      if token in conjunto_caracteres:
          llave = categoria
          return d[prev_estado][llave]

  # Imprime un mensaje si el token no se encuentra en el alfabeto
  print(f"{token}\tNulo")

# Función para verificar si un estado representa un dígito
def isDigit(prev_estado, estado):
  # Verifica si el estado actual o el estado previo corresponden a un número real
  if (prev_estado==1) and (dict_estado[estado] == 'Real'):
    return True
  if (estado==1) and (dict_estado[prev_estado]=='Real'):
    return True
  return False

# Función para ejecutar el autómata en una línea de texto
def correr_automaton(line):
  palabra = ''
  prev_estado = 0
  estado = None
  # Itera sobre cada token en la línea
  for token in line:
    estado = dame_estado(token, prev_estado)
    if estado == 9:
      estado = dame_estado(token)

    # Concatena caracteres si el estado no cambia o si el estado anterior es 0
    if (prev_estado == 0) or (dict_estado[estado] == dict_estado[prev_estado]):
      palabra += token
      prev_estado = estado
    elif estado != 9:
      # Maneja casos específicos de transición de estado
      if prev_estado == 6 and estado == 7:
        palabra += token
        prev_estado = 7
        continue
      if prev_estado == 8:
        for char in palabra:
          if char != '-':
             print(f"{char}\t{dict_simbolo[char]}")
             continue
        if palabra[-1] == '-':
          if dict_estado[estado] == 'Real' or dict_estado[estado] == 'Entero':
            palabra = '-' + token
            prev_estado = 4
          else:
            print(f"{palabra[-1]}\t{dict_simbolo[palabra[-1]]}")
            palabra = token
            prev_estado = estado
          continue
      elif isDigit(prev_estado, estado):
        prev_estado = 2
        palabra += token
        continue
      else:
        print(f"{palabra}\t{dict_estado[prev_estado]}")
      palabra = token
      prev_estado = estado

  # Imprime el último batch si el estado no es 9 y prev_estado no es None
  if estado != 9 and prev_estado is not None:
    print(f"{palabra}\t{dict_estado[prev_estado]}")
  print()

# Función principal para el análisis léxico de un archivo
def lexerAritmetico(archivo):
    with open(archivo, 'r') as file:
        # Itera sobre cada línea en el archivo
        for line in file:
            line = line.strip()
            if line != '':
              # Ejecuta el autómata para cada línea no vacía
              correr_automaton(line)

lexerAritmetico('expresiones.txt')