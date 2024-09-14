from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.generate)

    def generate(self):
        signs=''
        if self.ui.checkBox.isChecked():
            signs +='adsfghjklqwertyuiopzxcvbnm'
        if self.ui.cb_numbers.isChecked():
            signs +='123456789'

        resul =''
        number = random.randint(5,10)
        for _ in range(number):
            resul+=random.choice(signs)

        self.ui.result.setText(resul)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()