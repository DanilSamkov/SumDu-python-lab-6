def input_list():
    while True:
        user_input = input("Введіть елементи списку через пробіл: ")
        try:
            lst = list(map(int, user_input.split()))
            return lst
        except ValueError:
            print("Будь ласка, введіть лише цілі числа.")

def find_min_el(lst):
    return sorted(lst)[:5]

def main():
    while True:
        lst = input_list()

        # Пошук перших п’яти мінімальних елементів
        min_elements = find_min_el(lst)

        print("Перші п'ять мінімальних елементів:", min_elements)

        repeat = input("Бажаєте повторити? (y/n): ").strip().lower()
        if repeat != 'y':
            break

if __name__ == "__main__":
    main()