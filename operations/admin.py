"""
from django.contrib import admin

# Register your models here.
from .models import Objective, Question, Term, Formula_Parameters

class TermsInline(admin.TabularInline):
  model = Term
  extra = 2

class QuestionAdmin(admin.ModelAdmin):
  inlines = [TermsInline]

class ParamsInline(admin.TabularInline):
  model = Formula_Parameters
  extra = 2

class ObjectiveAdmin(admin.ModelAdmin):
  inlines = [ParamsInline]


admin.site.register(Objective, ObjectiveAdmin)
admin.site.register(Question, QuestionAdmin)
"""