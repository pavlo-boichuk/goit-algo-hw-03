import random

def get_numbers_ticket(min, max, quantity):
    '''
    Функція генерує вказану кількість унікальних чисел у заданому діапазоні
    :param min: int — мінімальне можливе число у наборі (не менше 1)
    :param max: int — максимальне можливе число у наборі (не більше 1000)
    :param quantity: int — кількість чисел, які потрібно вибрати (значення між min і max)
    :return: list - повертає список випадково вибраних, відсортованих чисел
    '''

    # контроль відповідності вхідних параметрів заданим обмеженням
    if not (1 <= min <= max <= 1000):
        print(f'Значення параметрів [min, max] не відповідають умовам: 1 <= min <= max <= 1000')
        
    if not (min <= quantity <= max):
        print(f'Значення параметру [quantity] не відповідає умові: min <= quantity <= max')

    # генерування списку значень від min до max
    list_of_range = list(range(min, max + 1))

    # вибрати quantity унікальних елементів зі списку, використовуючи метод random.sample(population, k)
    numbers_lst = random.sample(list_of_range, quantity)
     
    return sorted(numbers_lst)


def get_numbers_ticket2(min, max, quantity):

    # контроль відповідності вхідних параметрів заданим обмеженням
    if not (1 <= min <= max <= 1000):
        print(f'Значення параметрів [min, max] не відповідають умовам: 1 <= min <= max <= 1000')
        
    if not (min <= quantity <= max):
        print(f'Значення параметру [quantity] не відповідає умові: min <= quantity <= max')

    # створення порожньої множини для наповнення числами 
    numbers_set = set()

    # цикл перерветься після наповнення множини потрібною кількістю значень 
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min, max)) # Наповнення множини випадковими цілими числами від min до max

    # повертаємо відсортований список значень  
    return sorted(list(numbers_set))


lottery_numbers = get_numbers_ticket(1, 100, 7)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket2(1, 100, 7)
print("Ваші лотерейні числа (функція №2):", lottery_numbers)