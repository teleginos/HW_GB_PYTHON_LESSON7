import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel, QSpinBox


def case1():
    class RhythmChecker(QWidget):
        def __init__(self):
            super().__init__()

            # Инициализация интерфейса
            self.initUI()

        def initUI(self):
            layout = QVBoxLayout()

            # Текстовое поле для ввода стихотворения
            self.poem_input = QTextEdit(self)
            layout.addWidget(self.poem_input)

            # Кнопка для проверки ритма
            self.check_button = QPushButton("Проверить ритм", self)
            self.check_button.clicked.connect(self.check_rhythm)
            layout.addWidget(self.check_button)

            # Метка для отображения результата
            self.result_label = QLabel("", self)
            layout.addWidget(self.result_label)

            self.setLayout(layout)
            self.setWindowTitle('Проверка ритма')
            self.resize(300, 200)

        def check_rhythm(self):
            poem = self.poem_input.toPlainText()

            phrases = poem.split()

            syllable_counts = []

            for phrase in phrases:
                syllable_count = sum(1 for char in phrase if char in 'аеёиоуыэюя')
                syllable_counts.append(syllable_count)

            if len(set(syllable_counts)) == 1:
                self.result_label.setText("Парам пам-пам")
            else:
                self.result_label.setText("Пам парам")

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        checker = RhythmChecker()
        checker.show()
        sys.exit(app.exec())


def case2():
    class OperationTableGUI(QWidget):
        def __init__(self):
            super().__init__()

            # Инициализация интерфейса
            self.initUI()

        def initUI(self):
            layout = QVBoxLayout()

            # Создаем и добавляем элементы управления
            self.row_label = QLabel("Количество строк:")
            self.row_input = QSpinBox()
            self.row_input.setMinimum(1)
            self.row_input.setMaximum(20)
            layout.addWidget(self.row_label)
            layout.addWidget(self.row_input)

            self.column_label = QLabel("Количество столбцов:")
            self.column_input = QSpinBox()
            self.column_input.setMinimum(1)
            self.column_input.setMaximum(20)
            layout.addWidget(self.column_label)
            layout.addWidget(self.column_input)

            self.calculate_button = QPushButton("Показать таблицу")
            self.calculate_button.clicked.connect(self.show_table)
            layout.addWidget(self.calculate_button)

            self.result_display = QTextEdit()
            self.result_display.setReadOnly(True)
            layout.addWidget(self.result_display)

            self.setLayout(layout)
            self.setWindowTitle('Таблица умножения')
            self.resize(800, 400)

        def multiply(self, a, b):
            return a * b

        def show_table(self):
            num_rows = self.row_input.value()
            num_columns = self.column_input.value()
            result = ""

            for i in range(1, num_rows + 1):
                for j in range(1, num_columns + 1):
                    result += str(self.multiply(i, j)) + '\t'
                result += '\n'

            self.result_display.setText(result)

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = OperationTableGUI()
        window.show()
        sys.exit(app.exec())


def case3():
    pass


def default():
    print("Вы выбрали неизвестный случай")


switch_case = {
    1: case1,
    2: case2,
    3: case3
}

user_input: int = int(input("""1.Ритм в стихах Вини-Пуха.
2.Таблица умножения.
Введите Ваш выбор: """))

print("=" * 50)

switch_case.get(user_input, default)()
