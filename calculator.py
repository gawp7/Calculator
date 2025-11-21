from math import *

def operationsvalides(): 
      return ["multiplication","addition","soustraction","division"]

message = input("Quel type d'opération veut tu effectuer ? :").strip().casefold()

if message not in operationsvalides() :
      print("Veuillez entrez une opération valide")
      exit()

try :
    a = float(input("Entre le premier nombre :"))
    b = float(input("Entre le deuxième nombre :"))
except : 
    print("Veuillez entrez un nombre entier ou à virgule")
    exit()

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

