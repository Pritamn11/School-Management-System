from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User, Student, Teacher, Department

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

admin.site.register(User, UserAdmin)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'date_of_admission', 'fee')
    search_fields = ('user__email', 'department__name')
    list_filter = ('department',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'date_of_joining', 'salary')
    search_fields = ('user__email', 'department__name')
    list_filter = ('department',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.unregister(Group)
