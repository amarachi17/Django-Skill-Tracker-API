from django.contrib import admin
from .models import Skill

# Register your models here.
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'level', 'category', 'created_at']
    list_filter = ['level', 'category']
    search_fields = ['title', 'description']