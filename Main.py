import statistics
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
        #I think that this one gets garbage collected at some point?
        self.coursesToDisplay = gradebook.courseinstances[:]
        #---------------------------
        self.coursesDisplayed = []
        self.gradeBook = gradebook
        self.done = False

        


        self.root = Tk()
        self.root.title("Contestant 1785 Project 2")

        self.frame = ttk.Frame(self.root).grid(column=0, row=0, sticky=(N, E, S, W))

        self.title = ttk.Label(self.frame, text="Grade Book Manager").grid(column=1, row=1)
        
        self.errorMessageVar = StringVar()
        self.errorMessageVar.set("")

        self.displayCourseForm()

        for child in self.root.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def displayCourseForm(self):
        
        for course in self.coursesToDisplay:
            courseDisplayed = CourseDisplay(course, self.frame)
            self.coursesDisplayed.append(courseDisplayed)

        self.calculateButton = ttk.Button(self.frame, text="Calculate", command=self.newGradePortFolio)
        self.calculateButton.grid(row=7, column=2)

    def newGradePortFolio(self):

        for course in self.coursesDisplayed:
            if course.gradeVar.get() != "":
                try:
                    grade = float(course.gradeVar.get())
                    if grade < 0:
                        self.errorMessageVar.set("Error: Enter a positive num")
                        return
                except ValueError:
                    self.errorMessageVar.set("Error: Enter a number")
                    return

                indexValue = self.coursesDisplayed.index(course)
                self.gradeBook.courseinstances[indexValue].allgrades.append(grade)
            else:
                self.errorMessageVar.set("Error: Missing Values") 
                return
            
        self.displaySummary()
        
    def displaySummary(self):
        self.courseSummaryInstances = []
        self.summaryTitle = ttk.Label(self.frame, text="Summary").grid(row=9, column=1)
        self.errorMessage = ttk.Label(self.frame, textvariable=self.errorMessageVar).grid(row=10, column=1)

        self.done = False
        if self.done == False:
            for course in self.coursesDisplayed:
                courseSummary = CourseSummaryDisplay(course, self.coursesDisplayed, self.gradeBook, self.frame)
            self.done = True
            CourseSummaryDisplay.startrow = 10
        



        
    def start(self):
        self.root.mainloop()


class CourseDisplay():
    rowNumber = 2
    def __init__(self, course, frame):
        self.name = course.name
        self.frame = frame
        self.label = ttk.Label(self.frame, text=self.name).grid(row=CourseDisplay.rowNumber, column=1 )
        self.gradeVar = StringVar()
        self.gradeVar.set("")

        self.gradeEntry = ttk.Entry(self.frame, width=4, textvariable=self.gradeVar).grid(row=CourseDisplay.rowNumber, column=2)
        CourseDisplay.rowNumber += 1

class CourseSummaryDisplay():
    startrow = 10
    def __init__(self, course, displayedCourses, gradeBook, frame):
        self.frame = frame
        self.indexValue = displayedCourses.index(course)
        self.course = gradeBook.courseinstances[self.indexValue]
        self.average = 0
        self.min = 0
        self.max = 0
        if self.course.allgrades != []:
            self.average = statistics.mean(self.course.allgrades)
            self.min = sorted(self.course.allgrades)[0]
            self.max = sorted(self.course.allgrades)[-1]

        self.nameLabel = ttk.Label(self.frame, text=self.course.name).grid(row=CourseSummaryDisplay.startrow+1, column=1)
        CourseSummaryDisplay.startrow += 1
        self.averageLabel = ttk.Label(self.frame, text="Average:").grid(row=CourseSummaryDisplay.startrow+1, column=1, sticky=E)
        CourseSummaryDisplay.startrow += 1
        self.averageNumber = ttk.Label(self.frame, text=str(self.average)).grid(row=CourseSummaryDisplay.startrow, column=2)
        CourseSummaryDisplay.startrow +=1
        self.minLabel = ttk.Label(self.frame, text="Min:").grid(row=CourseSummaryDisplay.startrow+1, column=1, sticky=E)
        CourseSummaryDisplay.startrow += 1
        self.minNumber = ttk.Label(self.frame, text=str(self.min)).grid(row=CourseSummaryDisplay.startrow, column=2)
        CourseSummaryDisplay.startrow +=1
        self.maxLabel = ttk.Label(self.frame, text="Max:").grid(row=CourseSummaryDisplay.startrow+1, column=1, sticky=E)
        CourseSummaryDisplay.startrow += 1
        self.maxNumber = ttk.Label(self.frame, text=str(self.max)).grid(row=CourseSummaryDisplay.startrow, column=2,)
        CourseSummaryDisplay.startrow +=1



        
        
        

        
courses = ['Programming', 'Art', 'Science', 'Math', 'History']

gradeBook = GradeBook(courses)
gradeBookDisplay = GradeBookDisplay(gradeBook)
gradeBookDisplay.start()



