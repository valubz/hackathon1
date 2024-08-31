import os
import platform

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"


def calcular(operacion):
    try:

        return eval(operacion)
    except ZeroDivisionError:
        return "Error: División por cero"
    except Exception as e:
        return f"Error: {e}"

def main():
    while True:
        operacion = input("Introduce una operación (o presiona 'c' para borrar): ")
        
        if operacion.lower() == 'c':
            borrar_consola()
            continue
        
        resultado = calcular(operacion)
        print(resultado)

def borrar_consola():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    main()
