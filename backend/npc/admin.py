from django.contrib import admin
from .models import (Diagnosis, Patient, Categories, Procedure, PatientProcedure, UserPatient, Profession, Doctor,
                     UserDoctor)


class ProcedureInline(admin.TabularInline):
    extra = 5
    verbose_name = "Процедура"
    verbose_name_plural = "Процедуры"
    model = Patient.procedure.through


class CategoriesProcedureInline(admin.TabularInline):
    extra = 3
    verbose_name = "Категории процедуры"
    verbose_name_plural = "Категории Процедур"
    model = Patient.categories_procedure.through


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'age')
    inlines = (CategoriesProcedureInline, ProcedureInline)
    exclude = ('categories_procedure', 'procedure')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'categories', 'effectiveness')


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Doctor)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'id', 'profession', 'price', 'room')


@admin.register(PatientProcedure)
class PatientProcedureAdmin(admin.ModelAdmin):
    list_display = ('patient', 'id', 'procedure', 'counter', 'is_done')  # Поля, которые будут отображаться в списке
    search_fields = ('patient__name', 'procedure__name')  # Поиск по полям
    list_filter = ('patient', 'procedure', 'is_done')  # Фильтрация по полям


@admin.register(UserPatient)
class UserPatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'patient', 'is_done')
    search_fields = ('patient__name', 'user__name')
    list_filter = ('patient', 'user')


@admin.register(UserDoctor)
class UserDoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'doctor', 'level', 'busyness')
    search_fields = ('doctor__name', 'doctor__surname', 'doctor__patronymic', 'user__name')
    list_filter = ('doctor', 'user')
