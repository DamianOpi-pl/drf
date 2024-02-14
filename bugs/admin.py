from django.contrib import admin

from bugs.models import Bug, Project, User


@admin.register(Project)
class ProjectAdm(admin.ModelAdmin):
    list_display = ("project_id", "name")


@admin.register(User)
class UserAdm(admin.ModelAdmin):
    list_display = ("user_id", "username")


@admin.register(Bug)
class BugAdm(admin.ModelAdmin):
    list_display = ("bug_id", "user", "project", "description")
