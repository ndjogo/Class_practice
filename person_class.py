#importing library 
import datetime 



#creating a person class
class Person():
    def __init__(self, name, date_of_birth:datetime.date, friends:list):
        self.name = name 
        self.date_of_birth = date_of_birth
        self.friends = friends

if __name__ == "__main__":
    #creating person 1
    person_1 = Person("Nick", "1990-03-10", ["Muj"]) 
    print(person_1.name, person_1.date_of_birth, person_1.friends)
    #creating person 2 
    person_2 = Person("Caitlin", "1989-07-08", ["Nick", "Connor"])
    print(person_2.name, person_2.date_of_birth, person_2.friends)