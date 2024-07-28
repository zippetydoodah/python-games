

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, location):
        self.location = location
        self.books = []
        self.employees = []
        self.customers = []

    def addBook(self, book):
        self.books.append(book)

    def addEmployee(self, person):
        self.employees.append(person)

    def addCustomer(self, person):
        self.customers.append(person)

class Person:
    def __init__(self):
        self.first_name = None
        self.last_name = None

    def getInput(self):
        self.first_name = input("what is your first name?")
        self.last_name = input ("what is your last name?")
        
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


library = Library('Oxford')
library.addBook(Book('lord of the rings', 'JRR Tolkein'))
library.addBook(Book('the hobbit', 'JRR Tolkein'))
library.addEmployee(Person('Zach', 'Willians'))
library.addCustomer(Person('Matt', 'Willians'))

london = Library('Oxford')
london.addBook(Book('lord of the rings', 'JRR Tolkein'))
london.addBook(Book('the hobbit', 'JRR Tolkein'))
london.addEmployee(Person('Zach', 'Willians'))
london.addCustomer(Person('Matt', 'Willians'))


matt = Person()
matt.getInput()

zach = Person()
zach.first_name = 'Zach'
zach.last_name = 'WIlliams'

print(zach)
print(matt)