"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lubomír Smola
email: L.smola@seznam.cz
"""

cara = "*" * 40
#zadaný pracovní text
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
#Přihlášení a ověření uživatele

login_udaje = {"bob": "123",
              "ann": "pass123",
              "mike": "password123",
              "liz": "pass123"}
username = input("Zadejte uživatelské jméno: ")
password = input("Zadejte password: ")
print("username: ", username)
print("password: ", password)
print(cara)

if username in login_udaje and password == login_udaje[username]:
    print(f"Welcome to the app, {username}.")
    print("We have 3 texts to be analyzed.")
else:
    print("Wrong username or password. Exiting the app.")
    SystemExit()
print(cara)

#Volba textu

cast_textu = input("Enter a number btw. 1 and 3 to select: ")
if cast_textu.isdigit() and 1 <= int(cast_textu) <= 3:
    zvoleny_text = TEXTS[int(cast_textu) - 1]
elif not cast_textu.isdigit():
    print("Wrong type of input. Exiting the app.")
    SystemExit()
elif int(cast_textu) < 1 or int(cast_textu) > 3:
    print("The number is not in range (1-3). Exiting the app.")
    SystemExit()
print(cara)

#Analýza textu
from math import fsum
from collections import Counter
import string

print("Analyzing the text...")
for punc in string.punctuation:
    zvoleny_text = zvoleny_text.replace(punc, " ")

text_slova = zvoleny_text.split()
text_title = []
text_upper = []
text_lower = []
text_number = []

for word in text_slova:
    if word.istitle():
        text_title.append("*")
    elif word.isupper():
        text_upper.append("*")
    elif word.islower():
        text_lower.append("*")
    elif word.isdigit():
        text_number.append(word)

print(f"There are {len(text_slova)} words in the selected text.")
print(f"There are {len(text_title)} tittlecase words.")
print(f"There are {len(text_upper)} uppercase words.")
print(f"There are {len(text_lower)} lovercase words.")
print(f"There are {len(text_number)} numeric strings.")
print(text_number)
#print(text_number.fsum())