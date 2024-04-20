from djangoProject.project_app.models import User


class UserClass:
    def __init__(self, employee):
        self.employee = employee

    def save(self):
        user = User.objects.create(id=self.id, password=self.password,
                                   first_name=self.first_name, last_name=self.last_name,
                                   email=self.email, role=self.role,
                                   phone_number=self.phone_number, address=self.address)
        return f"{user.first_name} {user.last_name} with role {self.role} saved to database"

    def isAdmin(self):  # An admin is their own manager.
        if (self.employee.get_manager != self.employee): return False

    def isInstr(self):  # You are an Instructor if your manager is an admin
        manager = self.employee.get_manager()
        if (manager.employee.get_manager != manager): return False

    def createCourse(self):
        pass

    def deleteCourse(self):
        pass

    def createUser(self):
        pass

    def deleteUser(self):
        pass

    def assignInstructorToCourse(self):  # we don't assign instructors to courses (see design)
        pass

    def assignTAToCourse(self):  # When would we ever assign TA to courses?
        pass

        # precondition:   course must be valid
        # post-condition: section is created and is dependent on Course
        #                 this is made possible by not being able to accesss Section without valid course. (sloppy)
        # output:         returns Section that is NOT assigned to any user
        # side-effect:    N/A
        # Note:           Doesn't not check if section_id meets course number nomenclature (i.e. "-001" for lecture)

    def createSection(self, course, type, section_id):
        if not isinstance(course, CourseClass): raise TypeError("course must be of Type CourseClass!")
        if not isinstance(type, Type): raise TypeError("type must be of Type Type (Lecture or Lab)!")
        if not isinstance(section_id, int): raise TypeError("section_id must be of Type int!")
        if (section_id > 999): raise ValueError("sections must not exceed 3-digits!")
        return SectionClass(course, type, section_id)  # there is no user assigned to this course

        # precondition:  section is valid
        # postcondition: section is assigned a TA
        # output:        N/A
        # side-effect:   N/A

    def assignTAToSection(self, section, user):
        if not isinstance(user, TA): raise ValueError("User must be of TA, this is the 'AssignTA' method!")
        if not isinstance(section, SectionClass): raise TypeError("invalid section (not of Type SectionClass)!")

        type = section.type
        if (type != Type.Lab): raise ValueError("You can only assign TAs to a Lab Section")
        section.user = user
