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
            print("Operación borrada.")
            continue

        resultado = calcular(operacion)
        print(resultado)


if _name_ == "_main_":
    main()
