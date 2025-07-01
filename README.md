# Django-Skill-Tracker-API

# A simple API to track and manage skills using Django Rest Framework.

# Created a virul enironment skill

# Installed Django and DjangoRestFramework

# Ran django-admin statproject skill_tracker

# Created an app skills

# Added rest_framework and skills to skill_tracker settings

# Created a class model Skill in skill_tracker\skills\models.py

# python manage.py makemigrations skills
# python manage.py migrate

# Updated the admin.py to import Skill from models
# @admin.register(Skill)
# class SkillAdmin(admin.ModelAdmin):
#    list_display = ['title', 'level', 'category', 'created_at']
#    list_filter = ['level', 'category']
#    search_fields = ['title', 'description']
    
# Created a superuser

# Logged in to /admin
# Addded a few test skills and ensured filters and search works

## Day 1 Progress
- Created Skill model with title, description, level, category, and timestamp
- Registered model in admin
- Enabled search, filter, and display enhancements
