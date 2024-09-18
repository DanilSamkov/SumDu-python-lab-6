def get_set(prompt):
    user_input = input(prompt)
    # Створення множини з введеного рядка
    return set(user_input.split())


def modify_set(A, x):
    # Перевірка типу A
    if not isinstance(A, set):
        raise ValueError("A повинна бути множиною (set)")

    # Створення копії множини A для модифікацій
    B = set(A)

    # Перевірка наявності елемента x у множині B
    if x in B:
        B.remove(x)
    else:
        B.add(x)

    # Виведення результату
    print("Множина B:")
    if len(B) == 0:
        # Перетворення пустої множини на список
        result = list(B)
        # Виведення списку, перетвореного назад на множину
        print(set(result))
    else:
        print(B)


def main():
    while True:
        A = get_set("Введіть множину A (символи розділені пробілом): ")

        x = input("Введіть символ x: ")

        # Виконання операцій над множиною
        modify_set(A, x)

        repeat = input("Бажаєте повторити? (y/n): ").strip().lower()
        if repeat != 'y':
            break

if __name__ == "__main__":
    main()