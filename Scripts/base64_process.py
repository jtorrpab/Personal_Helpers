import base64
      
def encode():
    print("\nIngrese el valor a codificar:")
    try:
        input_value = input('> ')
        bytes_value = input_value.encode()
        text_encode = base64.b64encode(bytes_value)
        print(f'Valor codificado: {text_encode.decode()}\n')
    except Exception as ex:
        print(f'\nNo se pudo codificar {input_value}, Error: {ex}')
    
def decode():
    print("\nIngrese el valor a decodificar:")
    try:
        input_value = input('> ')
        bytes_value = input_value.encode()
        text_decode = base64.b64decode(bytes_value)
        print(f'Valor decodificado: {text_decode.decode()}\n') 
    except Exception as ex:
        print(f'\nNo se pudo decodificar {input_value}, Error: {ex}')

def print_options():
    print("Seleccione una opción:")
    print(' 1. Codifificar')
    print(' 2. Decodificar')
    print('-1. Salir')
    option = input("> ")
    return option

def base64_process():
    
    option = print_options()    
    while option != -1:
        if option == "1":
            encode()
            option = print_options()
            
        if option == "2":  
            decode()
            option = print_options()
            
        if option == "-1":
            break

if __name__ == '__main__':
    base64_process()