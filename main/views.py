from django.shortcuts import render
from .models import About, Skill, Project, Contact, WorkExperience, Education, Certification, Referee
import re

def normalize(text):
    """Lowercase and remove punctuation for consistent matching"""
    text = text.lower()
    text = re.sub(r'[&().]', '', text)  # remove &, (, ), .
    text = text.strip()
    return text

def home(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all().order_by('-created_at')
    contact = Contact.objects.first()
    work_experiences = WorkExperience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-end_year')
    certifications = Certification.objects.all()
    referees = Referee.objects.all()

    # --- ICON MAP ---
    icon_map = {
        "c#": "fa-solid fa-code",
        "c++": "fa-solid fa-code",
        "c programming": "fa-solid fa-laptop-code",
        "python": "fa-brands fa-python",
        "java": "fa-brands fa-java",
        "javascript": "fa-brands fa-js",
        "sql": "fa-solid fa-database",
        "mobile application development": "fa-solid fa-mobile-screen-button",
        "android applications": "fa-brands fa-android",
        "web development": "fa-solid fa-globe",
        "database management": "fa-solid fa-database",
        "cyber security": "fa-solid fa-shield-halved",
        "computer networking": "fa-solid fa-network-wired",
        "electronics and circuitry design": "fa-solid fa-microchip",
        "computer maintenance & repair": "fa-solid fa-screwdriver-wrench",
        "computer aided design": "fa-solid fa-ruler-combined",
        "computer application software": "fa-solid fa-laptop",
        "discrete maths": "fa-solid fa-square-root-alt",
        "machine learning": "fa-solid fa-robot",
        "artificial intelligence": "fa-solid fa-brain",
    }

    # Normalize icon_map keys for matching
    norm_icon_map = {normalize(k): v for k, v in icon_map.items()}

    # --- Attach icons dynamically ---
    for skill in skills:
        skill_name_norm = normalize(skill.name)
        icon = "fa-solid fa-star"  # fallback
        for keyword, icon_class in norm_icon_map.items():
            if keyword in skill_name_norm:
                icon = icon_class
                break
        skill.icon = icon

    return render(request, 'home.html', {
        'about': about,
        'skills': skills,
        'projects': projects,
        'contact': contact,
        'work_experiences': work_experiences,
        'educations': educations,
        'certifications': certifications,
        'referees': referees,
    })


