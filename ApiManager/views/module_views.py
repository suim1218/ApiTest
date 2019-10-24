from django.contrib import auth
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from ApiManager.models import Project, Module

import logging


# Create your views here.

# logger = logging.getLogger('HttpRunnerManager')


def module_list(request):
    """
    模块列表页
    """
    module_all = Module.objects.all()
    return render(request, 'module_list.html', {"modules": module_all})


def add_module(request):
    """
    增加模块
    """
    if request.method == "GET":
        return render(request, "add_module.html")
    if request.method == "POST":
        module_name = request.POST.get("module_name", "")
        simple_desc = request.POST.get("simple_desc", "")
        pid = request.POST.get("pid", "")
        if module_name == "":
            return JsonResponse({"message": "模块名称不能为空"})
        if len(module_name) > 50:
            return JsonResponse({"message": "模块名称不能超过50个字符"})

        # print(module_name,simple_desc,pid)

        Module.objects.create(name=module_name, describe=simple_desc, project_id=pid)
        return JsonResponse({"message": "添加成功"})


def get_select_data(request):
    """
    获取 "项目>模块" 列表
    :param request:
    :return: 项目接口列表
    """
    if request.method == "GET":
        projects = Project.objects.all()
        data_list = []
        for project in projects:
            project_dict = {
                "id": project.id,
                "name": project.name
            }

            modules = Module.objects.filter(project_id=project.id)
            module_list = []
            for module in modules:
                module_list.append({
                    "id": module.id,
                    "name": module.name,
                })

            project_dict["moduleList"] = module_list
            data_list.append(project_dict)

        return JsonResponse({"status": 10200, "message": "success", "data": data_list})

    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})


def delete_module(request, mid):
    """
    删除项目
    """
    if request.method == "GET":
        try:
            module = Module.objects.get(id=mid)
        except module.DoesNotExist:
            return HttpResponseRedirect("/module_list/")
        else:
            module.delete()
        return HttpResponseRedirect("/module_list/")
    else:
        return HttpResponseRedirect("/module_list/")


def edit_module(request, mid):
    """
    编辑模块
    """
    if request.method == "GET":
        return render(request, "edit_module.html")


def get_module_info(request):
    """
    模块信息传给前端页面
    """
    if request.method == "POST":
        mid = request.POST.get("mid", "")
        module = Module.objects.get(id=mid)
        project_id = module.project.id

        module_dict = {
            "id": project_id,
            "name": module.name,
            "description": module.describe,

        }
        return JsonResponse({"status": 10200, "message": "请求成功", "data": module_dict})

    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})


def save_module(request):
    """
    编辑模块后更新
    """
    if request.method == "POST":
        mid = request.POST.get("mid", "")
        module_name = request.POST.get("module_name", "")
        simple_desc = request.POST.get("simple_desc", "")
        pid = request.POST.get("pid", "")
        if module_name == "":
            return JsonResponse({"message": "模块名称不能为空"})
        if len(module_name) > 50:
            return JsonResponse({"message": "模块名称不能超过50个字符"})
        # print(pid)
        try:
            m = Module.objects.get(id=mid)
        except Module.DoesNotExist:
            return JsonResponse({"message": "模块不存在"})
        else:
            m.name = module_name
            m.describe = simple_desc
            m.project_id = pid
            m.save()
            return JsonResponse({"status": 10200, "message": "保存成功"})
