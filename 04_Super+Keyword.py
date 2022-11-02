""" child class can inherit the properities of parent class , but parent class can't inherit the properities of
child class. But there is technique(keyword) parent class can inherit the properities of child class.the keyword is
'super()'. """


class House:
    def home(self):
        print("I am Home")
class Furniture(House):
    def wood(self):
        super().home()
        print("I am Furniture")
        super().home()
a=Furniture()
a.home()
a.wood()