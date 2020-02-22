title1 = ("Sir","Master","Grand Master","Sire","Lord","Gaurdian Immortal","Herald","His Excellency","His Eminence","Nuncio","Polemarch","Towel Attendant","Vicar","Vicar General","Tribune","His highness");
import random
while title1 == title1:
    title2 = random.choice(title1)
    name = input("What is your name: ")
    print(title2+" "+name)
    cuit = input("Would you like continue?(Y/N)")
    if cuit == "N":
        print("Thanks for playing.")
        break