#Criar classe para calcular a distancia entre duas coordenadas e a inclinacao

class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return (y2-y1)/(x2-x1)

c1 = (3,2)
c2 = (8,10)

li = Line(c1, c2)

print(li.distance())
print(li.slope())

#Classe para calcular o volume e a area da superficie de um cilindro
class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.14*(self.radius**2)*self.height

    def surface_area(self):
        return 2*3.14*self.radius*self.height+2*3.14*(self.radius**2)

#Testando para um cilindro de 2 de altura e 3 de raio
cyl = Cylinder(2,3)
print(cyl.volume())
print(cyl.surface_area())
