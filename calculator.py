import sys
from math import sqrt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi("Qt_Designer/calculator.ui", self)
        self.first_screen.setText('0')
        for i in range(10):
            getattr(self, f'input_{i}').clicked.connect(self.digit_pressed)

        self.input_X.clicked.connect(self.multiplication_operation)
        self.input_division.clicked.connect(self.division_operation)
        self.input_minus.clicked.connect(self.minus_operation)
        self.input_plus.clicked.connect(self.plus_operation)
        self.input_equals.clicked.connect(self.equals_operation)
        self.pow_x_2.clicked.connect(self.pow_x_2_operation)
        self.sqrt.clicked.connect(self.sqrt_operation)
        self.one_divided_by_x.clicked.connect(self.one_divided_by_x_operation)
        self.del_all.clicked.connect(self.delete_all)
        self.delete.clicked.connect(self.delete_the_last_character)

        self.first_number = None
        self.second_number = None
        self.operation = None
        self.result = None

    def digit_pressed(self):
        if self.first_screen.text() == '0':
            self.first_screen.clear()
        if self.operation in ['-', '+', '*', '/']:
            self.first_screen.clear()
            self.operation = None
        button = self.sender()
        current_text = self.first_screen.text()
        new_text = current_text + button.text()
        self.first_screen.setText(new_text)

    def delete_the_last_character(self):
        self.first_screen.setText(self.first_screen.text().rstrip(self.first_screen.text()[-1]))

    def delete_all(self):
        self.first_screen.clear()
        self.second_screen.clear()

    def assigning_results(self):
        self.first_number = int(self.first_screen.text())
        self.second_screen.setText(f'{self.first_number} {str(self.operation)}')
        self.result = self.first_number

    def plus_operation(self):
        self.operation = '+'
        self.assigning_results()

    def minus_operation(self):
        self.operation = '-'
        self.assigning_results()

    def multiplication_operation(self):
        self.operation = '*'
        self.assigning_results()

    def division_operation(self):
        self.operation = '/'
        self.assigning_results()

    def pow_x_2_operation(self):
        if self.second_screen.text() == '':
            self.first_number = int(self.first_screen.text())
            self.second_screen.setText(f'sqr({self.first_number})')
        else:
            self.second_screen.setText(f'sqr({self.second_screen.text()})')
            if self.first_screen.text()[-2::] == '.0':
                self.first_number = int(self.first_screen.text())
            else:
                self.first_number = float(self.first_screen.text())

        self.result = pow(self.first_number, 2)
        self.first_screen.setText(f'{self.result}')

    def sqrt_operation(self):
        self.first_number = int(self.first_screen.text())
        self.second_screen.setText(f'√({self.first_number})')
        self.result = sqrt(self.first_number)
        if str(self.result)[-2::] == '.0':
            self.result = int(self.result)
        self.first_screen.setText(f'{self.result}')

    def one_divided_by_x_operation(self):
        self.first_number = int(self.first_screen.text())
        self.second_screen.setText(f'1/({self.first_number})')
        self.result = 1 / self.first_number
        self.first_screen.setText(f'{self.result}')

    def equals_operation(self):
        self.second_screen.setText(f'{self.second_screen.text()} {self.first_screen.text()} =')
        if '+' in self.second_screen.text():
            self.result += int(self.first_screen.text())
        elif '-' in self.second_screen.text():
            self.result -= int(self.first_screen.text())
        elif '*' in self.second_screen.text():
            self.result *= int(self.first_screen.text())
        elif '/' in self.second_screen.text():
            self.result /= int(self.first_screen.text())
            if str(self.result)[-2::] == '.0':
                self.result = int(self.result)
        self.first_screen.setText(f'{self.result}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
