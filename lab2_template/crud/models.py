"""Online course app models"""
from django.db import models
from django.utils.timezone import now


class User(models.Model):
    """User model"""
    first_name = models.CharField(null=False, max_length=30, default='John')
    last_name = models.CharField(null=False, max_length=30, default='Doe')
    dob = models.DateField(null=True)

    def __str__(self):
        """toString method for User string representation"""
        return self.first_name + self.last_name


class Instructor(User):
    """Instructor model"""
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    def __str__(self):
        """toString method for Instructor string representation"""
        return "First name: " + self.first_name + ", " + \
            "Last name: " + self.last_name + ", " + \
            "Is full time: " + str(self.full_time) + ", " + \
            "Total Learners: " + str(self.total_learners)


class Learner(User):
    """Learner model"""
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    )
    social_link = models.URLField(max_length=200)

    def __str__(self):
        """toString method for Learner string representation"""
        return "First name: " + self.first_name + ", " + \
            "Last name: " + self.last_name + ", " \
            "Date of Birth: " + str(self.dob) + ", " + \
            "Occupation: " + self.occupation + ", " + \
            "Social Link: " + self.social_link


class Course(models.Model):
    """Course model"""
    name = models.CharField(null=False, max_length=100, default='Online Course')
    description = models.CharField(max_length=500)
    # Many-To-Many relationship with Instructor
    instructor = models.ManyToManyField(Instructor)
    # Many-To-Many relationship with Learner via Enrollment relationship
    learners = models.ManyToManyField(Learner, through='Enrollment')

    def __str__(self):
        """toString method for Course string representation"""
        return "Name: " + self.name + ", " + "Description: " + self.description


class Enrollment(models.Model):
    """Enrollment model"""
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor'),
    ]
    # Add a learner foreign key
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    # Add a course foreign key
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Enrollment date
    date_enrolled = models.DateField(default=now)
    # Enrollment mode
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)


class Lesson(models.Model):
    """Lesson model"""
    title = models.CharField(max_length=200, default='title')
    # One-To-Many relationship with Course
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()
