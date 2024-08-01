from jarvas import Jarvas
import json
import random

jarvas = Jarvas(
    url="http://127.0.0.1:8000",
    app_name='bubble sort'
)
file = 'credentials.json'
jarvas.token(file)


def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista

def generate_numbers(qtd):
    return [random.randint(0, 100) for _ in range(qtd)]

def main():
    jarvas.change_State_App('started')
    try:
        x = 500

        numbers = generate_numbers(x)
        print("Generate numbers:", numbers)
        jarvas.change_State_App('the numbers were generated')


        sortedNum = bubble_sort(numbers)
        jarvas.change_State_App('the numbers were sorted')
        print("Sorted numbers:", sortedNum)
        jarvas.change_State_App('the application has been finalized')

    except ValueError:
        jarvas.change_State_App('the application have an error!')

if __name__ == "__main__":
    main()
    print(jarvas.read_apps())

