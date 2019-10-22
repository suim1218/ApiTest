from django.contrib import auth
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from ApiManager.models import Project, Module

import logging


# Create your views here.

# logger = logging.getLogger('HttpRunnerManager')


def index(request):
    return render(request, 'base.html')


def project_list(request):
    """
    项目列表页
    """
    project_all = Project.objects.all()
    return render(request, 'project_list.html', {"projects": project_all,
                                                 })


def add_project(request):
    """
    增加项目
    """
    if request.method == "GET":
        return render(request, "add_project.html")
    if request.method == "POST":
        project_name = request.POST.get("project_name", "")
        simple_desc = request.POST.get("simple_desc", "")
        Project.objects.create(name=project_name, describe=simple_desc)
        return JsonResponse({"mes": "添加成功"})


def delete_project(request, pid):
    """
    删除项目
    """
    if request.method == "GET":
        try:
            project = Project.objects.get(id=pid)
        except Project.DoesNotExist:
            return HttpResponseRedirect("/project_list/")
        else:
            project.delete()
        return HttpResponseRedirect("/project_list/")
    else:
        return HttpResponseRedirect("/project_list/")


def get_project_info(request):
    """
    项目信息传给前端页面
    """
    if request.method == "POST":
        pid = request.POST.get("pid", "")
        project = Project.objects.get(id=pid)
        print(pid)
        project_dict = {
            "id": project.id,
            "name": project.name,
            "description": project.describe,

        }
        return JsonResponse({"status": 10200, "message": "请求成功", "data": project_dict})

    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})


def edit_project(request, pid):
    """
    编辑项目
    """
    if request.method == "GET":
        return render(request, "edit_project.html")


def save_project(request):
    """
    编辑项目后更新
    """
    if request.method == "POST":
        pid = request.POST.get("pid", "")
        project_name = request.POST.get("project_name", "")
        simple_desc = request.POST.get("simple_desc", "")

        p = Project.objects.get(id=pid)
        p.name = project_name
        p.describe = simple_desc
        p.save()
        return JsonResponse({"status": 10200, "message": "保存成功"})


