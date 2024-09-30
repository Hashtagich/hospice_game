from django.contrib import admin
from .models import Diagnosis, Patient, Categories, Procedure


# Register your models here.

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'condition', 'sentiment', 'fatigue')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'categories', 'effectiveness')
