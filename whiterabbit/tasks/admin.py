from django.contrib import admin
from tasks.models import Project, Task


class ChoiceTask(admin.StackedInline):
    model = Task


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ChoiceTask]


admin.site.register(Project, ProjectAdmin)
