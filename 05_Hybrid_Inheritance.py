""" --> The hybrid inheritance is a combination of other types of inheritance.
--> Mostly it is a combination of multilevel and multiple inheritance. This type of inheritance is not much used.
--> In general, multiple and multilevel inheritance is widely used in real-time problems. 
--> Single inheritance is used for simple applications. """
'or'
""" Ir can be a combination of any kind of inheritance like--> Single,Multiple,Multi-Level and Hierarchical Inheritances. """

'Note:- There is no sequence in which child class can inherit which parent class (or) sub class.'


''' Example '''

class Parent1:
    def money(self):
        print("I am doing hard work for giving a bright future to my family")
class Parent2(Parent1):
    def home(self):
        print("I am preparing food and clean home for good health of my family")
class Parent3:
    def play(self):
        print("I want to play with my grand childrens")
class Me(Parent2,Parent3):
    def Enjoy(self):
        print("With all my lovely family we just enjoying our life as it comes with zero regrets")
a = Me()
a.Enjoy()
a.money()
a.play()
a.home()