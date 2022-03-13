class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        
    def distance(self):
        return (  (self.coor2[0]-self.coor1[0])**2  +  (self.coor2[1]-self.coor1[1])**2  )**(1/2)

    def slope(self):
        return ( self.coor2[1]-self.coor1[1] ) / ( self.coor2[0]-self.coor1[0] )

li = Line((3,2),(8,10))
print(li.distance())
print(li.slope())


class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        self.pi = 3.14

    def volume(self):
        return self.pi * self.radius**2 * self.height

    def surface_area(self):
        return 2*self.pi*self.radius**2 + 2*self.pi*self.radius*self.height

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())


class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}  \nAccount balance: ${self.balance}' 

    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if amount <= self.balance: self.balance -= amount
        else: print("Unavailable!")


acc = Account('Jose', 100)
print(acc)
print(acc.owner)
acc.deposit(10)
print(acc.balance)
acc.withdraw(20)
print(acc.balance)
acc.withdraw(200)