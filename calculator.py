import cmath
import numpy as np
import time
import sys

"""
Axiomas

Numeros complexos se comportam como numeros reais para adicao e multiplicacao.

1) a, b pertencem aos Reais, portanto precisam ser tipo Float.


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

def convert_to_float(user_number):
    pi_or_euler = {
        "pi": PI,
        "euler": EULER,
        }

    if user_number in pi_or_euler:
        return pi_or_euler[user_number]
    else:
        return float(user_number)

def exit_calc():
    return sys.exit("Ate logo!")

def chamada_z2():
    re2 = input("Digite o numero real do segundo complexo: ")
    im2 = input("Digite o numero imaginario do segundo complexo: ")

    real_2 = convert_to_float(re2)
    imag_2 = convert_to_float(im2)

    z2 = complex(real_2, imag_2)

    return z2

def novas_opcoes(resultado):
        print("")
        print("[1] Sair da Calculadora.\n[2] Reiniciar Calculadora.\n[3] Realizar operacao com o resultado anterior.")
        print("")
        escolha_final = input("Digite qual operacao deseja utilizar: ")
        if escolha_final == "1":
            exit_calc()
        elif escolha_final == "2":
            print("Reiniciando a calculadora...")
            time.sleep(2)
            print("")
        elif escolha_final == "3":
            pass


my_bool = True

while my_bool:
    re1 = input("Digite o numero real do primeiro complexo: ")
    im1 = input("Digite o numero imaginario do primeiro complexo: ")

    real = convert_to_float(re1)
    imag = convert_to_float(im1)

    z1 = complex(real, imag)
    operation = Operations(z1)

    print("")
    print("[1] Conjugado\n[2] Adicao\n[3] Subtracao\n[4] Multiplicacao\n[5] Divisao")
    print("")
    escolha = input("Digite qual operacao deseja utilizar: ")

    if escolha == "1":
        resultado = operation.conjugated()
        print("O conjugado é: ", resultado)
        time.sleep(2)

        novas_opcoes()

    elif escolha != "1":
        z2 = chamada_z2()

        if escolha == "2":
            resultado = operation.addition(z2)
            print("A soma dos complexos é: ", resultado)
            time.sleep(2)

            novas_opcoes()

        elif escolha == "3":
            resultado = operation.subtraction(z2)
            print("A subtraçao dos complexos é: ", resultado)
            time.sleep(2)

            novas_opcoes()

        elif escolha == "4":
            resultado = operation.multiplication(z2)
            print("A multiplicação dos complexos é: ", resultado)
            time.sleep(2)

            novas_opcoes()

        elif escolha == "5":
            resultado = operation.division(z2)
            print("A divisão dos complexos é: ", resultado)
            time.sleep(2)

            novas_opcoes()

    #TODO Adicionar opcao de realizar outra operacao com o resultado final
