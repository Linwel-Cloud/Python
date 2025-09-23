#install first: pip install art
from art import text2art

def x():
    name = input("Enter your name: ")
    art = text2art(name)
    print(art)

x()