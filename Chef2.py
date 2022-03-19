# Contains Chef class
# Used in 24_inheritance.py
from Chef1 import Chef1


class Chef2(Chef1):
    def makeSpecialDish(self):
        print("Chef is making Fried Rice")

    def makeBiryani(self):
        print("Chef is making Biryani")
