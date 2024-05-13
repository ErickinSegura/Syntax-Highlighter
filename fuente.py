# Año Bisiesto
#Erick Segura Sánchez

def es_bisiesto(an):
    if ((an%4==0 and an%100!=0) or an%400==0):
        print("Si es año bisiesto")
    
    else:
        print('No es año bisiesto')    

def main():
    an=int(input('Escribe tu año: '))
    es_bisiesto(an)
main()
    
