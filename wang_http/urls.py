"""wang_http URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ApiManager.views import project_views, module_views, case_views, environment_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 项目操作
    path('project_list/', project_views.project_list),
    path('add_project/', project_views.add_project),
    path('delete_project/<int:pid>/', project_views.delete_project),
    path('edit_project/<int:pid>/', project_views.edit_project),
    path('save_project/', project_views.save_project),
    path('get_project_info/', project_views.get_project_info),

    # 模块操作
    path('module_list/', module_views.module_list),
    path('add_module/', module_views.add_module),
    path('get_select_data/', module_views.get_select_data),
    path('delete_module/<int:mid>/', module_views.delete_module),
    path('edit_module/<int:mid>/', module_views.edit_module),
    path('get_module_info/', module_views.get_module_info),
    path('save_module/', module_views.save_module),

    # 用例操作
    # path('module_detail/<int:mid>/', case_views.module_detail),
    path('case_list/', case_views.case_list),
    path('add_case/', case_views.add_case),
    path('case_debug/', case_views.case_debug),


    # 环境操作
    path('environment_list/', environment_views.environment_list),
    path('add_environment/', environment_views.add_environment),
    path('delete_environment/<int:eid>/', environment_views.delete_environment),
    path('get_environment_info/', environment_views.get_environment_info),
    path('edit_environment/<int:eid>/', environment_views.edit_environment),
    path('save_environment/', environment_views.save_environment),


]