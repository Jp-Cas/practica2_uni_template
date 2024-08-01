

def main():
    cadena   = input()
    cadena_0 = ''
    
    for caracter in cadena:
        if caracter.isalnum():
            cadena_0 += caracter
    
    if cadena_0 == cadena_0[::-1]:
        print('Es un palíndromo')
    else:
        print('No es un palíndromo')
    

if __name__ == '__main__':
    main()


