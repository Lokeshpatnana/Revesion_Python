""" A child can inheriting the properities of parent class and grand parent class,and a parent class can inheriting 
the properities of grand parent class and grand parent class can't inherit the properities of parnet and child classes
are called as Multi-Level Inheritance. """

class grandfather:
    def saving(self):
        print("I am saving money in my bank account for my child and grand child")
    def playing(self):
        print("I want to play with my grand childrens")
class father(grandfather):
    def savings(self):
        print("There is no savings for me i just expenditure to my family")
    def play(self):
        print("There is no time to play with my childrens")
    def work(self):
        print("I am doing hard work for my childrens studies fee")
class Me(father):
    def savings(self):
        print("Still i am studying")
    def frnds(self):
        print("I am always playing and studying with my friends")
b=Me()
b.frnds()
b.play()
b.savings()
b.work()

c=father()
c.playing()
c.saving()
c.work()