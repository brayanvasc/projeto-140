import random

numeros = [1,2,3,4,5,6]

for dado in numeros:
    no = random.randint(1,6)

    if no == 1:
        print("[0  ]")
    if no == 2:
        print("[0  ]")
        print("[ 0 ]")
    if no == 3:
        print("[0  ]")
        print("[ 0 ]")
        print("[  0]")
    if no == 4:
        print("[0  ]")
        print("[ 0 ]")
        print("[  0]")
        print("[ 0 ]")
    if no == 5:
        print("[0  ]")
        print("[ 0 ]")
        print("[  0]")
        print("[ 0 ]")
        print("[0  ]")
    if no == 6:
        print("[0  ]")
        print("[ 0 ]")
        print("[  0]")
        print("[ 0 ]")
        print("[0  ]")
        print("[ 0 ]")
    print(dado)

