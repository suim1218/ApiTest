from django.contrib import auth
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from ApiManager.models import Project, Module, Environment


def environment_list(request):
    """
    环境列表页
    :param request:
    :return:
    """
    environment_all = Environment.objects.all()
    return render(request, 'environment_list.html', {"environments": environment_all})


def add_environment(request):
    """
    增加环境配置
    """
    if request.method == "GET":
        return render(request, "add_environment.html")
    if request.method == "POST":
        environment_name = request.POST.get("environment_name", "")
        environment_address = request.POST.get("environment_address", "")
        print(environment_name, environment_address)
        Environment.objects.create(name=environment_name, address=environment_address)
        return JsonResponse({"mes": "添加成功"})


def delete_environment(request, eid):
    """
    删除项目
    """
    if request.method == "GET":
        try:
            environment = Environment.objects.get(id=eid)
        except Project.DoesNotExist:
            return HttpResponseRedirect("/environment_list/")
        else:
            environment.delete()
        return HttpResponseRedirect("/environment_list/")
    else:
        return HttpResponseRedirect("/environment_list/")


def get_environment_info(request):
    """
    项目信息传给前端页面
    """
    if request.method == "POST":
        eid = request.POST.get("eid", "")
        environment = Environment.objects.get(id=eid)
        # print("========================")
        # print(eid)
        environment_dict = {
            "id": environment.id,
            "name": environment.name,
            "address": environment.address,

        }
        return JsonResponse({"status": 10200, "message": "请求成功", "data": environment_dict})

    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})


def edit_environment(request, eid):
    """
    编辑项目
    """
    if request.method == "GET":
        return render(request, "edit_environment.html")


def save_environment(request):
    """
    编辑环境后更新
    """
    if request.method == "POST":
        eid = request.POST.get("eid", "")
        environment_name = request.POST.get("environment_name", "")
        environment_address = request.POST.get("environment_address", "")

        environment = Environment.objects.get(id=eid)
        environment.name = environment_name
        environment.address = environment_address
        environment.save()
        return JsonResponse({"status": 10200, "message": "保存成功"})


def on_off(request):
    """
    开关
    """
    if request.method == "POST":
        eid = request.POST.get("eid", "")
        # print(eid)
        environment = Environment.objects.get(id=eid)
        # print(environment.status)
        # print(type(environment.status))
        if environment.status == 1:
            environment.status = 0
            environment.save()
            return JsonResponse({"message": "环境已停用"})

        if environment.status == 0:
            environment_all = Environment.objects.all()
            for i in environment_all:
                if i.status == 1:
                    return JsonResponse({"message": "当前已有环境开启,请关闭开启的环境"})
                else:
                    environment.status = 1
                    environment.save()
                    return JsonResponse({"message": "开启成功"})
    else:
        return JsonResponse({"message": "请求方法错误"})


def get_environment_url():
    """
    获取当前开启的环境address
    :return:
    """
    environment_all = Environment.objects.all()
    for environment in environment_all:
        if environment.status == 1:
            return environment.address
        else:
            pass
