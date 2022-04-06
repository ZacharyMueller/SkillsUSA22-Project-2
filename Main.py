from tkinter import *
from tkinter import ttk

class Course():
    
    def __init__(self, course):
        self.name = course
        self.allgrades = []



class GradeBook():

    def __init__(self, courses):

        self.courses = courses
        self.courseinstances = []

        for course in self.courses:
            courseinstance = Course(course)
            self.courseinstances.append(courseinstance)

class GradeBookDisplay():
    
    def __init__(self, gradebook):
        self.coursesToDisplay = gradebook.courseinstances[:]
        self.coursesDisplayed = []


        self.root = Tk()
        self.root.title("Contestant 1785 Project 2")

        self.frame = ttk.Frame(self.root).grid(column=0, row=0, sticky=(N, E, S, W))

        self.title = ttk.Label(self.frame, text="Grade Book Manager").grid(column=1, row=1)

        self.displayCourseForm()

        

    def displayCourseForm(self):
        
        for course in self.coursesToDisplay:
            courseDisplayed = CourseDisplay(course)
            self.coursesDisplayed.append(courseDisplayed)

        print(self.coursesToDisplay)
        
    def start(self):
        self.root.mainloop()

class CourseDisplay():
    
    def __init__(self, course):
        pass

        
courses = ['Programming', 'Art', 'Science', 'Math', 'History']

gradeBook = GradeBook(courses)
gradeBookDisplay = GradeBookDisplay(gradeBook)
gradeBookDisplay.start()



