from enum import Enum
from djangoProject.project_app.models import Course


class Semesters(Enum):
    Fall = 'Fall'
    Spring = 'Spring'
    Summer = 'Summer'

class CourseClass:
    def __init__(self, course_id, course_name, semester, year):
        self.course_id = course_id
        self.course_name = course_name
        self.semester = semester
        self.year = year

    def save(self):
        course = Course.objects.create(course_id=self.course_id, course_name=self.course_name,
                                       semester=self.semester, year=self.year)
        return (f"{course.course_name} for the {course.semester} "
                f"{course.year} semester saved to database")

class SectionClass: # Like a plane, and the seats on the plane, or Deck of Cards
    def __init__(self, section_id, type, course, user=None):
        self.section_id = section_id
        self.type = type
        self.course = course
        self.user = user

    def save(self):
        section = Section.objects.create(section_id=self.section_id, type=self.type, course=self.course, user=self.user)
        return f"{section.course}-{section.section_id} saved to database"

class Section(Course):
    pass