class Cylinder():
    def __init__(self, height, radius = 1):
        self.height = height 
        self.radius = radius 
        self.surface_area = self.get_surface_area() 
        self.volume = self.get_volume()


    def get_surface_area(self):
        #fucntion to get the surface area of a cylinder
        pi = 22/7
        self.surface_area = 2*(pi)*self.radius**2 + 2*(pi)*self.radius*self.height
        return round(self.surface_area, 2)

    def get_volume(self):
        #function to get the area of a cylinder 
        pi = 22/7 
        self.volume = pi*(self.radius**2)*self.height
        return round(self.volume, 2)


if __name__ == "__main__":
    cylinder_1 = Cylinder(2, 5)
    print(cylinder_1.height, cylinder_1.radius, cylinder_1.surface_area, cylinder_1.volume)