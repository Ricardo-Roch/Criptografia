import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QHBoxLayout, \
    QMessageBox, QDialog, QTextBrowser


# Función para realizar el cifrado César
def cifrado_cesar(texto, clave):
    resultado = ""
    alfabeto_min = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_may = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for letra in texto:
        if letra in alfabeto_min:
            indice = (alfabeto_min.index(letra) + clave) % len(alfabeto_min)
            resultado += alfabeto_min[indice]
        elif letra in alfabeto_may:
            indice = (alfabeto_may.index(letra) + clave) % len(alfabeto_may)
            resultado += alfabeto_may[indice]
        else:
            resultado += letra

    return resultado

# Función para cifrar o descifrar
def cifrar_descifrar(clave, cifrar=True):
    texto = entrada_texto.toPlainText()
    if not texto:
        QMessageBox.warning(window, "Advertencia", "El campo de texto está vacío. Por favor, ingrese texto.")
    elif not clave:
        QMessageBox.warning(window, "Advertencia", "El campo de clave está vacío. Por favor, ingrese una clave.")
    else:
        try:
            clave = int(clave)
            if cifrar:
                texto_cifrado = cifrado_cesar(texto, clave)
            else:
                texto_cifrado = cifrado_cesar(texto, -clave)
            resultado.setText(texto_cifrado)
        except ValueError:
            QMessageBox.warning(window, "Advertencia", "La clave ingresada no es un número válido. Por favor, ingrese un número entero.")

def limpiar_campos():
    entrada_texto.clear()
    entrada_clave.clear()
    resultado.clear()

def verificar_texto():
    texto = entrada_texto.toPlainText()
    texto_limpio = ''.join(char for char in texto if char.isalpha() or char.isspace())
    if texto != texto_limpio:
        entrada_texto.setPlainText(texto_limpio)

def verificar_clave():
    clave = entrada_clave.text()
    entrada_clave.setText(''.join(char for char in clave if char.isdigit()))

def mostrar_informacion():
    dialogo = QDialog()
    dialogo.setWindowTitle("Información")

    layout = QVBoxLayout()

    etiqueta_info = QLabel("Programa de Encriptación/Desencriptación con el cifrado de CESAR")
    etiqueta_autor = QLabel("Autor: Ricardo Rocha Moreno")
    etiqueta_script = QLabel("Script:")

    script_content = ""
    with open(__file__, "r") as script_file:
        script_content = script_file.read()

    texto_script = QTextBrowser()
    texto_script.setPlainText(script_content)

    layout.addWidget(etiqueta_info)
    layout.addWidget(etiqueta_autor)
    layout.addWidget(etiqueta_script)
    layout.addWidget(texto_script)

    dialogo.setLayout(layout)
    dialogo.exec_()

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Cifrado César")

layout = QVBoxLayout()

label_alfabeto = QLabel("Alfabeto: abcdefghijklmnopqrstuvwxyz ")
label = QLabel("Texto:")
layout.addWidget(label_alfabeto)
layout.addWidget(label)
entrada_texto = QTextEdit()
entrada_texto.setPlaceholderText("Ingrese su texto")

entrada_texto.textChanged.connect(verificar_texto)  # Conectar la función de verificación
layout.addWidget(entrada_texto)

label_clave = QLabel("Clave:")
entrada_clave = QLineEdit()
entrada_clave.setPlaceholderText("Ingrese su clave")
layout.addWidget(label_clave)

entrada_clave.textChanged.connect(verificar_clave)
layout.addWidget(entrada_clave)

boton_cifrar = QPushButton("Cifrar")
boton_descifrar = QPushButton("Descifrar")
boton_limpiar = QPushButton("Limpiar")
boton_info = QPushButton("Información")

boton_cifrar.clicked.connect(lambda: cifrar_descifrar(entrada_clave.text()))
boton_descifrar.clicked.connect(lambda: cifrar_descifrar(entrada_clave.text(), cifrar=False))
boton_limpiar.clicked.connect(limpiar_campos)
boton_info.clicked.connect(mostrar_informacion)
#boton_info.clicked.connect(lambda: QMessageBox.information(window, "Información", "Programa de Encriptación/Desencriptación con el cifrado de CESAR\nAutor: Ricardo Rocha Moreno \nScript:\n"))

layout_botones = QHBoxLayout()
layout_botones.addWidget(boton_cifrar)
layout_botones.addWidget(boton_descifrar)
layout_botones.addWidget(boton_limpiar)
layout_botones.addWidget(boton_info)

label_salida = QLabel("Resultado:")
resultado = QTextEdit()
resultado.setReadOnly(True)

layout.addLayout(layout_botones)
layout.addWidget(label_salida)
layout.addWidget(resultado)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
