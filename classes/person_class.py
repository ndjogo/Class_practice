#importing library 
import datetime 



#creating a person class
class Person():
    def __init__(self, name, date_of_birth:datetime.date, friends:list):
        self.name = name 
        self.date_of_birth = date_of_birth
        self.friends = friends

    def __str__(self):
        #returns person details as a string
        return f"name: {self.name}, \ndate of birth: {self.date_of_birth}, \nfriends: {len(self.friends)}"
    
    def __gt__(self, second_person):
        #compares the date of birth 
        return self.date_of_birth > second_person.date_of_birth 

    def add_friend(self, second_person):
        #adds second person's name to first person friends list
        self.friends.append(second_person.name)
        #adds first person's name to second person friends list
        second_person.friends.append(self.name)
        





if __name__ == "__main__":
    #creating person 1
    person_1 = Person("Nick", "1990-03-10", ["Muj"]) 
    print(person_1.name, person_1.date_of_birth, person_1.friends)
    #creating person 2 
    person_2 = Person("Caitlin", "1989-07-08", ["Sam", "Connor"])
    print(person_2.name, person_2.date_of_birth, person_2.friends)
    #print the string 
    print(person_1)
    #comparing two ages
    print(person_1 > person_2)
    #using function to add names to friends list 
    person_1.add_friend(person_2)
    #print friends list 
    print(person_1.friends, person_2.friends)
