class Course:
    #Constructor for course class
    def __init__(self, name, credit_hours):
        self.name = name
        self.credit_hours = credit_hours
        self.prerequisites = []

class Major:
    #constructor for major class
    def __init__(self, name, credit_hours_required, college):
        self.name = name
        self.credit_hours_required = credit_hours_required
        self.college = college
        self.courses = []
    #add course to the array of courses
    def add_course(self, course_name, credit_hours):
        course = Course(course_name, credit_hours)
        self.courses.append(course)

    #add prerequesite to the list in the Course class
    def add_prerequisite(self, course_name, prerequisite_name):
        for course in self.courses:
            if course.name == course_name:
                for prerequisite in self.courses:
                    if prerequisite.name == prerequisite_name:
                        course.prerequisites.append(prerequisite)
                        return
                prerequisite = Course(prerequisite_name, 0)
                self.courses.append(prerequisite)
                course.prerequisites.append(prerequisite)
                return
                
    #Print statement for class
    def __str__(self):
        result = f"{self.name} ({self.credit_hours_required} credit hours)\n"
        for course in self.courses:
            result += f"  {course.name} ({course.credit_hours} credit hours)"
            if course.prerequisites:
                result += " Prerequisites: "
                result += ", ".join([p.name for p in course.prerequisites])
            result += "\n"
        return result
