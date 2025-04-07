class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old.")

class Programmer(Human):
    def code(self):
        print(f"I'm a self-taught programmer")

class Designer(Human):
    def design(self):
        print(f"I design various things")

class Goaprogrammer(Programmer):
    def code(self):
        print(f"I'm a full stack coder who can lead his team")

class Goadesigner(Designer):
    def design(self):
        print(f"I design various things and I can be a good leader")

class Professional(Programmer, Designer):
    def show_skills(self):
        print(f"I'am both programmer and designer")

prgmr = Programmer("Erekle", 19)
prgmr.introduce()
prgmr.code()

prgmrG = Goaprogrammer("Erekle", 19)
prgmrG.introduce()
prgmrG.code()

designer = Designer("Erekle", 19)
designer.introduce()
designer.design()

Gdesigner = Goadesigner("Erekle", 19)
Gdesigner.introduce()
Gdesigner.design()

pro = Professional("Erekle", 19)
pro.introduce()  
pro.code()      
pro.design()     
pro.show_skills()
