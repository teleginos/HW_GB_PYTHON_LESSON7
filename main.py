def case1():
    def check_rhythm(poem):

        phrases = poem.split()

        syllable_counts = []

        for phrase in phrases:
            syllable_count = sum(1 for char in phrase if char in 'аеёиоуыэюя')

            syllable_counts.append(syllable_count)

        if len(set(syllable_counts)) == 1:
            return "Парам пам-пам"
        else:
            return "Пам парам"

    print(check_rhythm(input("Введите ваше стихотворенье: ")))


def case2():
    def multiply(a, b):
        return a * b

    def print_operation_table(operation):

        num_rows = int(input("Введите количество строк: "))
        num_columns = int(input("Введите количество столбцов: "))

        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                print(operation(i, j), end='\t')
            print('\n')

    # Тестирование функции
    print_operation_table(multiply)


def default():
    print("Вы выбрали неизвестный случай")


switch_case = {
    1: case1,
    2: case2
}

user_input: int = int(input("""1.Ритм в стихах Вини-Пуха.
2.Таблица умножения.
Введите Ваш выбор: """))

print("=" * 50)

switch_case.get(user_input, default)()
