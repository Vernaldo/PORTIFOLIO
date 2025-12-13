from django.contrib import admin
from .models import  About, Skill, Project, Contact, WorkExperience, Education, Certification, Referee

admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Referee)

