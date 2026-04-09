# object oriented programming 
# methods 
# class person:
#  def start(self):
#     print()
## constructor run object is created
            # _init_ ()
# destructor destroy the object
            # _del_
# class ---- blue print  # inside,outside
# class dog:
#     d1= dog("max")

# class dog:
#   species ="canine" #attribute
# d1= dog("max")
# d2 =dog()
# print(d1.species)
# print(d2.species)
# components 
# name ="emma"
# self.name = name
# def show(self):
#     print("hello")
# def
# object --- instances
            # class = car_brand:
            # car_brand=car("toyota")
                # class car_brand:
                #     def _init_(self,brands):
                #         self.brands = brands
                #     def show (self):
                # car_brand1=car_brand("toyota")
# attributes
# pillars: 
# 1 encapsulation
# 2.inheritance
# 3.polymorphism
# 4 abstarction
# special method (magic )
#  types of methods (instance ,class,static )
# 
class className:
    def _init_(self,parameters):
        # attributes
        self.variable =parameters
    def method_name(self):
        # behaviour
        pass

class car:
    def _init_(self,brand,colour):
        self._brand =brand 
        self.colour = colour
    # def _del_(self, brand ,colour):
    def display(self):
    # def drive(self):
        print(f"{self.brand} car is {self.colour}")
# object instance (self) of a class
car1 = car ("nissan", "red")
car1.display()

