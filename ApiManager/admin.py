from django.contrib import admin

from ApiManager.models import Project, Module, TestCase, Environment


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    """
    项目
    """
    list_display = ['name', 'describe', 'create_time']
    search_fields = ['name']


class ModuleAdmin(admin.ModelAdmin):
    """
    模块
    """
    list_display = ['name', 'describe', 'create_time', 'project']
    search_fields = ['name']
    list_filter = ['project']


class TestCaseAdmin(admin.ModelAdmin):
    """
    用例
    """
    list_display = ['name', 'belong_project', 'create_time', 'module']
    search_fields = ['name']


class EnvironmentAdmin(admin.ModelAdmin):
    """
    环境
    """
    list_display = ['name', 'address']
    search_fields = ['name']


admin.site.register(Module, ModuleAdmin)

admin.site.register(Project, ProjectAdmin)
admin.site.register(TestCase, TestCaseAdmin)
admin.site.register(Environment, EnvironmentAdmin)
