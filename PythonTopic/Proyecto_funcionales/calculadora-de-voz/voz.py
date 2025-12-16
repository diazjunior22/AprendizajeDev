import pyttsx3

#voz.say()
#voz.runAndWait()


def voz(palabra : str, numero =  None):
    engine = pyttsx3.init()
    if numero is not None:
        palabra = palabra + f" {numero}"
    engine.say(palabra)
    engine.runAndWait()
        

     
def calculadora(numA,NumB,operador):
    try:
        if operador == '+' :
            resultado = numA + NumB 
            return  resultado
        elif operador == '-' :
            resultado = numA - NumB 
            return  resultado
        elif operador == 'x' :
            resultado = numA * NumB 
            return  resultado
        elif operador == '/' :
            resultado = numA / NumB  
            return  resultado
        else:
            print('Numero INCORRECTO')
    except ValueError:
            print("❌ Error: eso no es un número. Inténtalo de nuevo.")
            
                    
def preguntar():
    while True:
        try:
            voz('ELIJA El PRIMER NUMERO')
            numA = int(input('ELIJA El PRIMER NUMERO: '))
            break
        except ValueError:
            voz('Coloca Bien El Numero')
            print('COLOCA BIEN EL NUMERO')
    while True:
        try:
            voz('ELIJA EL SEGUNDO EL NUMERO')
            numB = int(input('ELIJA EL SEGUNDO EL NUMERO; '))
            break
        except ValueError:
            voz('Coloca Bien El Numero')
            print('COLOCA BIEN EL NUMERO')
        
    return numA ,numB



while True:
    voz('BIENVENIDO A LA CALCULADORA ESPECIAL')
    print('BIENVENIDO A LA CALCULADORA ESPECIAL')
    try:
        voz('ELIJA UNA OPCIÓN. 1 SUMAR, 2 RESTAR, 3 MULTIPLICAR, 4 DIVIDIR, 0 SALIR')
        opciones = int(input('ELIJE UNA OPCION\n 1 PARA SUMAR \n 2 PARA RESTAR \n 3 PARA MULTIPLICAR \n 4 PARA DIVIDIR \n 0 PARA SALIR  '))
        if opciones == 0:
            voz('HAZ SALIDO DE LA CALCULADORA')
            print('HAZ SALIDO DE LA CALCULADORA');
            break      
        elif opciones == 1:
            numA , numB =  preguntar()
            resultado = calculadora(numA,numB,'+')
            voz('EL RESULTADO DE SU SUMA FUE', resultado)   
            print(f'EL RESULTADO DE SU SUMA FUE {resultado}')
        elif opciones == 2:
            numA , numB =  preguntar()
            resultado = calculadora(numA,numB,'-')
            voz('EL RESULTADO DE SU RESTA' , resultado)
            print(f'EL RESULTADO DE SU RESTA FUE {resultado}')

        elif opciones == 3:
            numA , numB =  preguntar()
            resultado = calculadora(numA,numB,'x')
            print(f'EL RESULTADO DE SU MULTIPLICACION FUE {resultado}')
            voz('EL RESULTADO DE SU MULTIPLICACION FUE', resultado)
        elif opciones == 4:
            numA , numB =  preguntar()
            resultado = calculadora(numA,numB,'/')
            if numA == 0 or numB == 0:
                voz('ERROR ZERO DIVISION')
                print('ERROR ZERO DIVISION')
            else:
                voz('EL RESULTADO DE SU DIVISION  FUE',resultado )
                print(f'EL RESULTADO DE SU DIVISION  FUE {resultado}')
        else: 
            voz('ELIJA UNA OPCION CORRECTA')
            print('ELIGE UNA OPCION CORRECTA')
            
            
    except ValueError:
        print('elija un valor correcto')
        
    