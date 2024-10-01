from django.contrib import admin
from .models import Diagnosis, Patient, Categories, Procedure, PatientProcedure


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


@admin.register(PatientProcedure)
class PatientProcedureAdmin(admin.ModelAdmin):
    list_display = ('patient', 'procedure', 'counter', 'is_done')  # Поля, которые будут отображаться в списке
    search_fields = ('patient__name', 'procedure__name')  # Поиск по полям
    list_filter = ('patient', 'procedure', 'is_done')  # Фильтрация по полям
