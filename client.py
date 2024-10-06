import Pyro4

def factorial_client(number):
    # Conectar con el servidor
    uri = input("Introduce la URI del servidor: ")
    factorial_server = Pyro4.Proxy(uri)
    try:
        result = factorial_server.factorial(number)
        print(f"Factorial de {number} es {result}")
    except Exception as e:
        print(f"Error al calcular el factorial: {e}")

if __name__ == "__main__":
    number = int(input("Introduce un número: "))
    factorial_client(number)
