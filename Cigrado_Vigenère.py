import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QTextCursor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QHBoxLayout, \
    QMessageBox, QDialog, QTextBrowser
import re

def cifrado_vigenere(texto, clave):
    resultado = ""
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    clave = clave.lower()
    i = 0
    clave_len = len(clave)

    for letra in texto:
        if letra in alfabeto:
            if letra == ' ':
                resultado += ' '
            else:
                indice = (alfabeto.index(letra) - alfabeto.index(clave[i % clave_len])) % len(alfabeto)
                resultado += alfabeto[indice]
                i += 1
        else:
            resultado += letra

    return resultado

def descifrado_vigenere(texto, clave):
    resultado = ""
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    clave = clave.lower()
    i = 0
    clave_len = len(clave)

    for letra in texto:
        if letra in alfabeto:
            if letra == ' ':
                resultado += ' '
            else:
                indice = (alfabeto.index(letra) + alfabeto.index(clave[i % clave_len])) % len(alfabeto)
                resultado += alfabeto[indice]
                i += 1
        else:
            resultado += letra

    return resultado

def cifrar_descifrar(clave, cifrar=True):
    texto = entrada_texto.toPlainText()
    clave = clave.lower()  # Convertir la clave a minúsculas
    if not texto:
        QMessageBox.warning(window, "Advertencia", "El campo de texto está vacío. Por favor, ingrese texto.")
    elif not clave:
        QMessageBox.warning(window, "Advertencia", "El campo de clave está vacío. Por favor, ingrese una clave.")
    else:
        # Mantener la capitalización original en el resultado
        resultado_final = ""
        i = 0
        for letra in texto:
            if letra.isalpha():
                if letra.isupper():
                    letra_resultado = cifrado_vigenere(letra.lower(), clave[i % len(clave)]).upper()
                    if not cifrar:
                        letra_resultado = descifrado_vigenere(letra.lower(), clave[i % len(clave)]).upper()
                    resultado_final += letra_resultado
                else:
                    letra_resultado = cifrado_vigenere(letra, clave[i % len(clave)])
                    if not cifrar:
                        letra_resultado = descifrado_vigenere(letra, clave[i % len(clave)])
                    resultado_final += letra_resultado
                i += 1
            else:
                resultado_final += letra

        resultado.setText(resultado_final)

def limpiar_campos():
    entrada_texto.clear()
    entrada_clave.clear()
    resultado.clear()

def verificar_texto():
    entrada_texto.textChanged.disconnect(verificar_texto)  # Desconectar la función para evitar recursión
    texto = entrada_texto.toPlainText()
    texto_limpio = ''.join(char for char in texto if char.isalpha() or char.isspace())
    entrada_texto.setPlainText(texto_limpio)
    entrada_texto.moveCursor(QTextCursor.End)  # Mover el cursor al final
    entrada_texto.textChanged.connect(verificar_texto)  # Volver a conectar la función


def mostrar_informacion():
    dialogo = QDialog()
    dialogo.setWindowTitle("Información")

    layout = QVBoxLayout()

    etiqueta_info = QLabel("Programa de Encriptación/Desencriptación con el cifrado de VIGENERE")
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
window.setWindowTitle("Cifrado Vigenère")

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

# Validador para aceptar solo letras y espacios en clave
clave_validator = QRegExpValidator(QRegExp("^[a-zA-Z]*$"))
entrada_clave.setValidator(clave_validator)

layout.addWidget(label_clave)
layout.addWidget(entrada_clave)

boton_cifrar = QPushButton("Cifrar")
boton_descifrar = QPushButton("Descifrar")
boton_limpiar = QPushButton("Limpiar")
boton_info = QPushButton("Información")

boton_cifrar.clicked.connect(lambda: cifrar_descifrar(entrada_clave.text()))
boton_descifrar.clicked.connect(lambda: cifrar_descifrar(entrada_clave.text(), cifrar=False))
boton_limpiar.clicked.connect(limpiar_campos)
boton_info.clicked.connect(mostrar_informacion)

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


