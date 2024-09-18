def remove_dubl(input_list):
    # Створюємо новий список, де будемо зберігати унікальні елементи
    unique_list = []
    seen = set()
    for item in input_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list


def main():
    while True:
        input_str = input("Введіть елементи списку через пробіл: ")

        # Перетворення введеного рядка на список
        input_list = input_str.split()

        print("Початковий список:", input_list)

        # Видалення повторень
        result_list = remove_dubl(input_list)

        print("Список без повторень:", result_list)

        repeat = input("Бажаєте повторити? (y/n): ").strip().lower()
        if repeat != 'y':
            break

if __name__ == "__main__":
    main()