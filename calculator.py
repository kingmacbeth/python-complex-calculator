import cmath
import numpy as np

"""
Axiomas

Numeros complexos se comportam como numeros reais para adicao e multiplicacao.

1) a, b pertencem aos Reais


"""
#Constants
PI = cmath.pi
EULER = cmath.e

class Operations():
    def __init__(self, z1):
        self.z1 = z1

    def conjugated(self):
        conj = np.conj(self.z1)
        return conj

    def addition(self, z2):
        add = self.z1 + z2
        return add

    def subtraction(self, z2):
        sub = self.z1 - z2
        return sub

    def multiplication(self, z2):
        mult = self.z1 * z2
        return mult

    def division(self, z2):
        div = self.z1 / z2
        return div

class Converter():
    def __init__(self, user_number):
        self.user_number = user_number

    def convert_to_float(self):
        pi_or_euler = {
            "pi": PI,
            "euler": EULER,
            }

        if self.user_number in pi_or_euler:
            return pi_or_euler[self.user_number]
        else:
            return float(self.user_number)

my_bool = True

while my_bool:
    re1 = input("Digite o numero real do primeiro complexo: ")
    im1 = input("Digite o numero imaginario do primeiro complexo: ")

    converter_real = Converter(re1)
    real = converter_real.convert_to_float()

    converter_imag = Converter(im1)
    imag = converter_imag.convert_to_float()

    z1 = complex(real, imag)
    operation = Operations(z1)

    print("[1] Conjugado\n[2] Adicao\n[3] Subtracao\n[4] Multiplicacao\n[5] Divisao")
    escolha = input("Digite qual operacao deseja utilizar: ")

    if escolha == "1":
        conjugado = operation.conjugated()
        print("o conjugado é", conjugado)

    elif escolha != "1":
        re2 = input("Digite o numero real do segundo complexo: ")
        im2 = input("Digite o numero imaginario do segundo complexo: ")

        converter_real_2 = Converter(re2)
        real_2 = converter_real.convert_to_float()

        converter_imag_2 = Converter(im2)
        imag_2 = converter_imag.convert_to_float()

        z2 = complex(real_2, imag_2)

        if escolha == "2":
            resultado = operation.addition(z2)
            print("A soma dos complexos é: ", resultado)

        elif escolha == "3":
            resultado = operation.subtraction(z2)
            print("A subtraçao dos complexos é: ", resultado)

        elif escolha == "4":
            resultado = operation.multiplication(z2)
            print("A multiplicação dos complexos é: ", resultado)

        elif escolha == "5":
            resultado = operation.division(z2)
            print("A divisão dos complexos é: ", resultado)

    #TODO Adicionar funcao para deixar a calculadora rodando
    #TODO Adicionar opcao de reiniciar a calculadora
    #TODO Adicionar opcao de desligar a calculadora
    #TODO Adicionar opcao de realizar outra operacao com o resultado final
