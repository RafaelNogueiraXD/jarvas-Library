from jarvas import Jarvas
import json
import random

jarvas = Jarvas(
    url="https://8dff-186-251-193-131.ngrok-free.app",
    app_name='bubble sort',
    phone="5555996852212"
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
    jarvas.change_state_app('started')
    try:
        x = 10000
        jarvas.change_state_app('the numbers were generated')
        sortedNum = bubble_sort(generate_numbers(x))
        jarvas.change_state_app('the numbers were sorted \n33% of aplication to conclusion')
        sortedNum = bubble_sort(generate_numbers(x))
        jarvas.change_state_app('the numbers were sorted \n66% of aplication to conclusion')
        sortedNum = bubble_sort(generate_numbers(x))
        jarvas.change_state_app('the numbers were sorted \n99% of aplication to conclusion')
        # print("Sorted numbers:", sortedNum)
        jarvas.change_state_app('the application has been finalized')

    except ValueError:
        jarvas.change_state_app('the application have an error!')

if __name__ == "__main__":
    main()
    print(jarvas.read_apps())

