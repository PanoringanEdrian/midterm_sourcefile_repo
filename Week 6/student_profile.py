# a. Parent class for basic student information.
class Student:
    def __init__(self, name, course, year_level):
        # Store the three values in instance attributes.
        self.name = name
        self.course = course
        self.year_level = year_level

    def get_profile(self):
        # Return the student's information using HTML-like tags.
        return (
            f"<h2>{self.name}</h2>\n"
            f"<p>Course: {self.course}</p>\n"
            f"<p>Year Level: {self.year_level}</p>"
        )


# b. Child class for an IT student.
class ITStudent(Student):
    # Class attribute holding the student's main programming skill.
    skill = "Python"

    def get_skill(self):
        # Return the programming skill using a <p> tag.
        return f"<p>Programming Skill: {self.skill}</p>"


# c. Application class with routes.
class StudentApp:
    def __init__(self, title, student):
        # Store the app title and the student object it will display.
        self.title = title
        self.student = student

    def route(self, path):
        # Return the correct content for /, /profile, or an invalid route.
        if path == "/":
            return f"<h1>{self.title}</h1>"
        elif path == "/profile":
            return f"{self.student.get_profile()}\n{self.student.get_skill()}"
        else:
            return "<h1>404 - Page Not Found</h1>"

    def run(self):
        # Print the app title and test the required routes.
        print(f"Running: {self.title}\n")

        print("GET /")
        print(self.route("/"))
        print()

        print("GET /profile")
        print(self.route("/profile"))
        print()

        print("GET /unknown")
        print(self.route("/unknown"))


# d. Create the student and application objects.
student = ITStudent("Mike Edrian M. Panoringan", "BS Information Technology", 2)
app = StudentApp("PSU Student Profile App", student)

# Start the application.
app.run()