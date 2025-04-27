"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lubomír Smola
email: L.smola@seznam.cz
"""

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
cara = "-" * 40
login_udaje = {"bob": "123",
              "ann": "pass123",
              "mike": "password123",
              "liz": "pass123"}
username = input("username:").lower()
password = input("password:")
print(cara)

if username in login_udaje and password == login_udaje[username]:
    print(f"Welcome to the app, {username}.")
    print("We have 3 texts to be analyzed.")
else:
    print("unregistered user, terminating the program...")
    exit()
print(cara)

#Volba textu
text_choose = input("Enter a number btw. 1 and 3 to select: ")
if text_choose.isdigit() and 1 <= int(text_choose) <= 3:
    choosed_text = TEXTS[int(text_choose) - 1]
elif not text_choose.isdigit():
    print("Wrong type of input. Exiting the app.")
    SystemExit()
elif int(text_choose) < 1 or int(text_choose) > 3:
    print("The number is not in range (1-3). Exiting the app.")
    SystemExit()
print(cara)

#Analýza textu
from math import fsum
from collections import Counter
import string

print("Analyzing the text...")
for punc in string.punctuation:
    choosed_text = choosed_text.replace(punc, " ")

text_words = choosed_text.split()
text_title = []
text_upper = []
text_lower = []
text_number = []

for word in text_words:
    if word.istitle():
        text_title.append("*")
    elif word.isupper():
        text_upper.append("*")
    elif word.islower():
        text_lower.append("*")
    elif word.isdigit():
        text_number.append(word)

print(f"There are {len(text_words)} words in the selected text.")
print(f"There are {len(text_title)} tittlecase words.")
print(f"There are {len(text_upper)} uppercase words.")
print(f"There are {len(text_lower)} lovercase words.")
print(f"There are {len(text_number)} numeric strings.")
print(f"The sum of all the numbers is {sum(map(int, text_number))}")
print(cara)
print("LEN|" + " " * 5 + "OCCURENCES" + " " * 5 + "|NR.")
print(cara)

#Počty znaků ve slovech
word_len1 =[len(word) == 1 for word in text_words]
word_len2 =[len(word) == 2 for word in text_words]
word_len3 =[len(word) == 3 for word in text_words]
word_len4 =[len(word) == 4 for word in text_words]
word_len5 =[len(word) == 5 for word in text_words]
word_len6 =[len(word) == 6 for word in text_words]
word_len7 =[len(word) == 7 for word in text_words]
word_len8 =[len(word) == 8 for word in text_words]
word_len9 =[len(word) == 9 for word in text_words]
word_len10=[len(word) == 10 for word in text_words]
word_len11=[len(word) == 11 for word in text_words]

#Vizualizace výstupu
print(f"  1|{"*" * word_len1.count(True)}"
      f"{" " * (20 - word_len1.count(True))}|{word_len1.count(True)}"
)
print(f"  2|{"*" * word_len2.count(True)}"
      f"{" " * (20 - word_len2.count(True))}|{word_len2.count(True)}"
)
print(f"  3|{"*" * word_len3.count(True)}"
      f"{" " * (20 - word_len3.count(True))}|{word_len3.count(True)}"
)
print(f"  4|{"*" * word_len4.count(True)}"
      f"{" " * (20 - word_len4.count(True))}|{word_len4.count(True)}"
)
print(f"  5|{"*" * word_len5.count(True)}"
      f"{" " * (20 - word_len5.count(True))}|{word_len5.count(True)}"
)
print(f"  6|{"*" * word_len6.count(True)}"
      f"{" " * (20 - word_len6.count(True))}|{word_len6.count(True)}"
)
print(f"  7|{"*" * word_len7.count(True)}"
      f"{" " * (20 - word_len7.count(True))}|{word_len7.count(True)}"
)
print(f"  8|{"*" * word_len8.count(True)}"
      f"{" " * (20 - word_len8.count(True))}|{word_len8.count(True)}"
)
print(f"  9|{"*" * word_len9.count(True)}"
      f"{" " * (20 - word_len9.count(True))}|{word_len9.count(True)}"
)
print(f" 10|{"*" * word_len10.count(True)}"
      f"{" " * (20 - word_len10.count(True))}|{word_len10.count(True)}"
)
print(f" 11|{"*" * word_len11.count(True)}"
      f"{" " * (20 - word_len11.count(True))}|{word_len11.count(True)}"
)
exit()