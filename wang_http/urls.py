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
from ApiManager.views import project_views, module_views, case_views, environment_views,run_task_views,report_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 项目操作
    path('project_list/', project_views.project_list),
    path('add_project/', project_views.add_project),
    path('delete_project/<int:pid>/', project_views.delete_project),
    path('edit_project/<int:pid>/', project_views.edit_project),
    path('save_project/', project_views.save_project),
    path('get_project_info/', project_views.get_project_info),
    path('project_module_list/<int:pid>/', project_views.project_module_list),
    path('project_module_case_list/<int:mid>/', project_views.project_module_case_list),


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
    path('case_assert/', case_views.case_assert),
    # path('get_case_info/', case_views.get_case_info),
    path('edit_case/<int:eid>/', case_views.edit_case),
    path('delete_case/<int:cid>/', case_views.delete_case),
    # path('get_case_environment_info/', case_views.get_case_environment_info),




    # 环境操作
    path('environment_list/', environment_views.environment_list),
    path('add_environment/', environment_views.add_environment),
    path('delete_environment/<int:eid>/', environment_views.delete_environment),
    path('get_environment_info/', environment_views.get_environment_info),
    path('edit_environment/<int:eid>/', environment_views.edit_environment),
    path('save_environment/', environment_views.save_environment),
    path('on_off/', environment_views.on_off),


    # 运行用例
    path('run_project_task/', run_task_views.run_project_task),
    # path('get_case/', run_case_views.get_case),


    # 测试报告
    path('report/', report_views.report),
]
