""" A Single Child can inheriting the properities of morethan one parent classes is called Multiple Inheritance. """

class Father:
    love = "Fail"
    def books(self):
        print("Okay go bookstore purchase books what you want.")
    def movie(self):
        print("Don't go for any movie just read at home.")
    def laptop(self):
        print("It's mandotory ok then i purchase and give you.")
class Mother:
    sai = "Lalith"
    def movie(self):
        print("ok I ask your father and you can go for movies")
    def food(self):
        print("after ate the food you go and sleep")
    def phone(self):
        print("always seeing phone you can get eyesite")
# class Me(Father,Mother):
class Me(Mother,Father):
    def frnds(self):
        print("I want to go out with my friends")
    def bike(self):
        print("I want ride a bike")
a=Me()
a.bike()
a.frnds()
a.books()
a.movie()
a.phone()
print(a.sai)
print(a.love)
a.laptop()