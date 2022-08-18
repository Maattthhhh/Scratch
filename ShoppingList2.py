import random
from random import choice
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "[]{}#()*;._-"

def chooseDishes(days):
    while len(myMenu) < int(days):
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("Done! Here's your menu: ")
    for dish in myMenu:
        print(dish)
    print()
    print("Out of these, my favorite is. . ." + choice(myMenu))
    print()

def buildShoppingList():
    myShoppingList = []
    if "Adobo" in myMenu:
        myShoppingList.append(adobo)
    if "Afritada" in myMenu:
        myShoppingList.append(afritada)
    if "Champorado" in myMenu:
        myShoppingList.append(champorado)
    if "Sopas" in myMenu:
        myShoppingList.append(sopas)
    if "Tinola" in myMenu:
        myShoppingList.append(tinola)
    for dish in myShoppingList:
        for ingredient in dish:
            def textbook(notepad):
                if ingredient not in notepad:
                    notepad.append(ingredient)
            print(ingredient)
    print("Viola! Bon apetit!")
    print()
    
foodWeLike = ["Adobo", "Afritada", "Champorado", "Sopas", "Tinola"]
adobo = ["garlic", "onion", "soy sauce", "vinegar", "chicken", "pepper"]
afritada = ["chicken", "tomato sauce", "potato", "carrot", "salt", "bellpeppers", "green peas"]
champorado = ["cocoa powder", "evaporated milk", "brown sugar", "sticky rice"]
sopas = ["evaporated milk", "elbow macaroni", "chicken", "carrot", "onion", "garlic"]
tinola = ["chicken", "sayote", "ginger", "garlic", "onion", "salt", "pepper", "dahon ng sili"]

myMenu = []

print("Hi, I'm Munch! I'll help you plan your dinner menu! :)");
print()
username = input("First, please enter your username: ");
print()
print("Hello " + username + ", would you like us to generate your password?");
pw = input("Type Y for yes, N for no. ");
if pw == "Y":
    all= lower + upper + number + symbol
    length = 9
    password = "".join(random.sample(all,length))
    print("Ok, your new password is: ", password)

else:
    newpassword = input("Alright, please enter your new password: ")
    
answer = input("Great! How many days would you like me to plan? ")
print("Ok, I'm going to plan " + answer + " dinners from your favorites.")

chooseDishes(answer)

print("Would you like a shopping list for this menu?");
answer = input("Type Y for yes, N for no. ");

if answer == "Y":
    buildShoppingList()
    print("Would you like me search for discounts or promos? ");
    discount = input("Type Y for yes, N for no. ");
    if discount == "Y":
        MAPPING = {
        '0':'零',
        '1':'壱',
        '2':'弐つ',
        '3':'参',
        '4':'四',
        '5':'五',
        '6':'六',
        '7':'セブン',
        '8':'八',
        '9':'九'
        }

        def cipher(original):
                text = ""
                for letter in original:
                        letter = letter.upper()
                        new_letter = MAPPING[letter]
                        text = text + new_letter
                return text

        text = input("Please enter your zip code: ")
        result = cipher(text)
        from urllib.request import urlopen

        def get_condition(city):
                url = "http://wttr.in/" + city + "?format=%c"
                page = urlopen(url)
                raw = page.read()
                condition = raw.decode("utf-8")
                return condition

        city = input("Which city do you want to shop? ")
        condition = get_condition(city)
        if condition == "Clear":
                print("Great! Your promo code is:", result)
                print("No umbrella needed ^_^")
        else:
                print("Great! Your promo code is:", result)
                print("Also, bring umbrella, just in case :)")
    else:
        print("Alright. Bye for now :)")    
else:
    print("Alright. Bye for now :)")
