import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from subprocess import run

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Selección de Cifrado")
        self.setGeometry(100, 100, 400, 150)

        layout = QVBoxLayout()

        btn_cesar = QPushButton("Cifrado César")
        btn_vigenere = QPushButton("Cifrado Vigenère")

        btn_cesar.clicked.connect(self.open_cesar_script)
        btn_vigenere.clicked.connect(self.open_vigenere_script)

        layout.addWidget(btn_cesar)
        layout.addWidget(btn_vigenere)

        self.setLayout(layout)

    def open_cesar_script(self):
        run(["python", "Cifrado_Cesar.py"])

    def open_vigenere_script(self):
        run(["python", "Cigrado_Vigenère.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
