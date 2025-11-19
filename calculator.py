from math import *
message = input("Quel type d'opération veut tu effectuer ? :")

multiplication : "multiplication".strip().lower()
addition : "addition".strip().lower()
soustraction : "soustraction".strip().lower()
division : "division".strip().lower()

a = float(input("Entrez votre premier nombre entier :"))
b = float(input("Entrez votre deuxième nombre entier :"))

multiplication = a * b
addition = a + b
soustraction = a - b
division = a / b
if message == ("multiplication" , "addition" , "soustraction" , "division") :
   print("Erreur, Veuillez entrer une opération valide (multiplication, addition, soustraction, division)")
if multiplication :
    print("Le résultat de la multiplication est :", multiplication)
if addition : 
    print("Le résultat de l'addition est :", addition)
if soustraction :
    print("Le résultat de la soustraction est :", soustraction)
if division :
    print("Le résultat de la division est :", division)
