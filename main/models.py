from django.db import models

class About(models.Model):
    full_name = models.CharField(max_length=100,blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100,blank=True, null=True)
    photo = models.ImageField(upload_to='about_photos/',blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20,blank=True, null=True)
    field = models.CharField(max_length=100,blank=True, null=True) 
    profession = models.CharField(max_length=100,blank=True, null=True) 
    description = models.TextField(blank=True, null=True)  
    
    def __str__(self):
        return self.full_name
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, help_text="FontAwesome class, e.g. fa-brands fa-python", blank=True, null=True)


    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.email


class Project(models.Model):
    PROJECT_TYPES = [
        ('mobile', 'Mobile App-Project'),
        ('web', 'Website=Project'),
        ('hardware', 'Hardware-Project'),
        ('software', 'Software-Project'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='about_photos/',blank=True, null=True)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    reason_for_the_project = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='project_videos/', blank=True, null=True)
    problem_solved = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class WorkExperience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # null means “Currently working”
    responsibility_1 = models.TextField(blank=True, null=True)
    responsibility_2 = models.TextField(blank=True, null=True)
    responsibility_3 = models.TextField(blank=True, null=True)
    responsibility_4 = models.TextField(blank=True, null=True)
    responsibility_5 = models.TextField(blank=True, null=True)
    responsibility_6 = models.TextField(blank=True, null=True)
    responsibility_7 = models.TextField(blank=True, null=True)
    responsibility_8 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.role} at {self.company}"


class Education(models.Model):
    school = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200) 
    field_of_study = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.qualification} - {self.school}"


class Certification(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return self.title



class Referee(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField()
    address = models.CharField(max_length=200 ,blank=True, null=True)
    position = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name



