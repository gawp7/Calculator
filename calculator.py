from math import *

def operationsvalides(): 
      return ["multiplication","addition","soustraction","division"]
while True:
    message = input("Quel type d'opération veux-tu effectuer ? : ").strip().casefold()
    if message in operationsvalides():
          break
    else:
      print("Opération invalide, recommence.")

a = float(int(input("Entre le premier nombre :")))
b = float(int(input("Entre le deuxième nombre :")))


def multiplication(): 
      return a * b
def addition() : 
      return a + b
def soustraction() : 
      return a - b      
def division() : 
      return a / b

if message == "multiplication":
    print("Le résultat de votre Multiplication:", multiplication())
elif message == "addition" :
        print("Le résultat de votre addition :", addition())
elif message == "soustraction":
        print("Le résultat de votre soustraction :", soustraction())
elif message == "division":
        print("Le résultat de votre division :", division())

