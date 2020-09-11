"""
Created by Tyler Gassan
9/9/2020

Basic GPA calculator
"""

class GPA():

    def __init__(self):
        self.data = []
        self.total = 0
        self.loadSave()
        self.menu()
        
    def add_grade(self):
        try:
            grade = float(input('Add Grade: '))
            if (grade < 0 or grade > 100):
                print("Invalid data")
                self.add_grade()
            self.data.append(grade)
        except:
            self.add_grade()
        self.menu()
        
    def remove_grade(self):
        print(self.data)
        grade = int(input('Remove Grade: '))
        try:
            self.data.remove(grade)
        except:
            print("Grade not found")
            self.remove_grade()
        self.menu()
       
    def calculate(self):
        values = len(self.data)
        for value in self.data:
            self.total += value 
        try:
            gpa = (self.total/values)
        except:
            self.menu()
        print("GPA: ",gpa)
        self.total = 0
        self.menu()
        
    def displayGrades(self):
        if len(self.data) == 0:
            print("No values inputted")
        print("Grades: ",self.data)
        self.menu()
        
    def saveGrades(self):
        file = open('data.txt','a')
        file.write(str(self.data) + "\n")
        file.close()
        print("Data: ",self.data, " saved")
        self.menu()
        
    def loadSave(self):
        file = open('data.txt','r')
        try:
            lines = file.readlines()
            if len(lines) < 1:
                raise
            loads = []
            i = 0
            for line in lines:
                loads.append(line)
                print("(",i,") ",line)
                i += 1
            choice = int(input("\nLoad save: "))
            x = loads[choice].rstrip()
            load = x.strip('][').split(', ')
            for i in range(0, len(load)): 
                load[i] = float(load[i])
            for value in load:
                self.data.append(float(value))
            self.data = load
        except:
            print("No available loads")
        file.close()
        
    def menu(self):     
        print('----------------------------------')
        print("Current Grades: ",self.data)
        x = input('[1] Add grade\n[2] Remove grade\n[3] Calculate\n[4] Display grades\n[5] Save\n')

        if x == '1':
            self.add_grade()
        elif x == '2':
            self.remove_grade()
        elif x == '3':
            self.calculate()
        elif x == '4':
            self.displayGrades()       
        elif x == '5':
            self.saveGrades()           
        else:
            print('Please choose 1-5')
            self.menu()
        print('----------------------------------')
        
test = GPA()                    

