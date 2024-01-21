# Завдання 2

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    # Кількість ітерацій
    count = 0

    # Верхня межа
    upper_bound = None

    # Перевірка на входження елемента у границі відсортованого масиву
    if x < arr[0] or x > arr[-1]:
        return (count, upper_bound)
    else:
        upper_bound = arr[-1]

    while low <= high:
        mid = (high + low) // 2
        count += 1

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return (count, x)

    # якщо елемент не знайдений
    return (count, upper_bound)


if __name__ == "__main__":
    arr = [-4, -2, -1, 0, 1, 3, 6, 7, 9, 10, 30, 50, 60, 90, 100]

    x_list = [-5, -4.5, -4, -3, -2, -1.5, -1, 0,
              1, 2, 4, 7, 8, 12.9, 30, 54, 99, 100, 101]

    dividing_line = f"| {'-'*20:^20} | {'-'*20:^20} | {'-'*20:^20} | {'-'*20:^20} |"
    header = f"| {'Значення для пошуку':^20} | {'Результат пошуку':^20} | {'Кількість ітерацій':^20} | {'Верхня межа':^20} |"

    print(dividing_line)
    print(header)
    print(dividing_line)
    for x in x_list:
        result = binary_search(arr, x)
        body = f"| {x:^20} | {str(result):^20} | {str(result[0]):^20} | {str('відсутня' if result[1] is None else result[1]):^20} |"
        print(body)
    print(dividing_line)
