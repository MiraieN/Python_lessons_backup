class Human:
    def __init__(self, name, age, gender, job, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.job = job
        self.salary = salary

    def getValues(self):
        print("Human\n")
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"gender: {self.gender}")
        print(f"job: {self.job}")
        print(f"salary: {self.salary}")

    def setJob(self, job):
        self.job = job

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        print("salary is:", self.salary)

