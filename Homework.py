#Problema 1: usar try and except  para resolver o problema
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print('Something is wrong!')


#Problema 2: usar try, except e finally para continuar rodando o programa
try:
    x = 5
    y = 0

    z = x/y
except:
    print("Wrong math.")
finally:
    print('The program has ended.')


#Problema 3: usar try, except e finally com while loop
def ask():
    while True:
        try:
            num = int(input("Please type a number: "))
        except:
            print('That is not a number! Try Again.')
            continue
        else:
            print('Thank you. Number squared: ', num**2)
            break

ask()




