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
POSITIVE_INFINITE = cmath.inf
POSITIVE_COMPLEX_INFINITE = cmath.infj
NAN = cmath.nan
NAN_COMPLEX = cmath.nanj

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
    def convert_to_float(user_number):
        """Funcao para converter o input do usuario para float aceitando pi ou euler.

        Args:
            user_number (float): input do usuario que sera passado como tipo float
        """
        pi_or_euler = {
            "pi": PI,
            "euler": EULER,
            "a":"",
            }

        if user_number in pi_or_euler:
            return pi_or_euler[user_number]
        else:
            return float(user_number)

    def convert_to_pi_or_euler():
        if real == PI:
            pass
        elif real == EULER:
            pass


re1 =float(input("Digite o numero real do primeiro complexo: "))
im1 = float(input("Digite o numero imaginario do primeiro complexo: "))

# converter = Converter()
# real = converter.convert_to_float(re1)
# imag = converter.convert_to_float(im1)

z1 = complex(re1, im1)
operation = Operations(z1)

print("[1] conjugado\n[2] z1 + z2\n[3] z1 - z2\n[4] z1 * z2\n[5] z1 / z2")
escolha = input("digite o que vc quer fazer: ")


if escolha == "1":
    conjugado = operation.conjugated()
    print("o conjugado é", conjugado)

elif escolha != "1":
    re2 = int(input("Digite o numero real do segundo complexo: "))
    im2 = int(input("Digite o numero imaginario do segundo complexo: "))

    z2 = complex(re2, im2)

    if escolha == "2":
        soma = operation.addition(z2)
        print("A soma dos complexos é: ", soma)

    elif escolha == "3":
        sub = operation.subtraction(z2)
        print("A subtraçao dos complexos é: ", sub)

    elif escolha == "4":
        mult = operation.multiplication(z2)
        print("A multiplicação dos complexos é: ", mult)

    elif escolha == "5":
        div = operation.division(z2)
        print("A divisão dos complexos é: ", div)
