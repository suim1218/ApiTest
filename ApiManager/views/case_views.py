import json
import requests
from django.contrib import auth
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from ApiManager.models import Project, Module, Environment, TestCase


def case_list(request):
    cases = TestCase.objects.all()
    return render(request, 'case_list.html', {"cases": cases})


def case_debug(request):
    """
    测试用例的调试
    """
    if request.method == "POST":
        environment_id = request.POST.get("environment_id", "")
        url = request.POST.get("url", "")  # URL
        method = request.POST.get("method", "")  # 方法
        header = request.POST.get("header", "")  # header
        par_type = request.POST.get("type", "")  # 参数类型
        par_body = request.POST.get("parameter", "")  # 参数

        environment_obj = Environment.objects.get(id=environment_id)
        environment_address = environment_obj.address
        print(environment_address)
        # print(method)
        print(par_type)

        if header == "":
            header = "{}"

        try:
            header = json.loads(header.replace("\'", "\""))
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "header类型错误"})

        if par_body == "":
            par_body = "{}"

        try:
            payload = json.loads(par_body.replace("\'", "\""))

        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "参数类型错误"})

        result_text = None
        if method == "get":
            r = requests.get(environment_address + url, params=payload, headers=header)
            result_text = r.text

        if method == "post":
            if par_type == "form":
                r = requests.post(environment_address + url, data=payload, headers=header)
                result_text = r.text

            if par_type == "json":
                r = requests.post(environment_address + url, json=payload, headers=header)
                result_text = r.text

        return JsonResponse({"result": result_text})
    else:
        return JsonResponse({"result": "请求方法错误"})


def case_assert(request):
    """
    测试用例的断言
    """
    if request.method == "POST":
        result_text = request.POST.get("result", "")
        assert_text = request.POST.get("assert", "")
        assert_type = request.POST.get("assert_type", "")

        if result_text == "" or assert_text == "":
            return JsonResponse({"result": "断言的文本不能为空"})

        if assert_type == "contains":
            assert_list = assert_text.split(">>")
            for assert_value in assert_list:
                if assert_value not in result_text:
                    return JsonResponse({"result": "断言失败"})
                else:
                    return JsonResponse({"result": "断言成功"})

        elif assert_type == "mathches":
            if assert_text != result_text:
                return JsonResponse({"result": "断言失败"})
            else:
                return JsonResponse({"result": "断言成功"})

    else:
        return JsonResponse({"result": "请求方法错误"})


def add_case(request):
    """
    增加用例
    """
    environment_all = Environment.objects.all()
    if request.method == "GET":
        return render(request, "add_case.html", {"environments": environment_all})
    if request.method == "POST":
        environment_id = request.POST.get("environment_id", "")
        module_id = request.POST.get("module_id", "")
        case_name = request.POST.get("case_name", "")
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        header = request.POST.get("header", "")
        parameter_type = request.POST.get("par_type", "")
        parameter_body = request.POST.get("par_body", "")
        assert_type = request.POST.get("ass_type", "")
        assert_text = request.POST.get("ass_text", "")
        cid = request.POST.get("cid", "")

        if case_name == "":
            return JsonResponse({"status": 10101, "message": "用例名称不能为空"})

        if module_id == "":
            return JsonResponse({"status": 10103, "message": "所属的模块不能为空"})

        if assert_type == "" or assert_text == "":
            return JsonResponse({"status": 10102, "message": "断言的类型或文本不能为空"})

        # print(parameter_body)
        payload = parameter_body.replace("\"", "\'")
        # print(payload)
        # ...
        if method == "get":
            method_number = 1
        elif method == "post":
            method_number = 2
        elif method == "delete":
            method_number = 3
        elif method == "put":
            method_number = 4
        else:
            return JsonResponse({"status": 10104, "message": "未知的请求方法"})

        if parameter_type == "form":
            parameter_number = 1
        elif parameter_type == "json":
            parameter_number = 2
        else:
            return JsonResponse({"status": 10104, "message": "未知的参数类型"})

        if assert_type == "contains":
            assert_number = 1
        elif assert_type == "mathches":
            assert_number = 2
        else:
            return JsonResponse({"status": 10104, "message": "未知的断言类型"})

        if cid == "":
            TestCase.objects.create(environment=environment_id, name=case_name, module_id=module_id,
                                    url=url, method=method_number, header=header,
                                    parameter_type=parameter_number, parameter_body=payload,
                                    assert_type=assert_number, assert_text=assert_text)
        else:
            case = TestCase.objects.get(id=cid)
            case.environment = environment_id
            case.name = case_name
            case.module_id = module_id
            case.url = url
            case.method = method_number
            case.header = header
            case.parameter_type = parameter_number
            case.parameter_body = payload
            case.assert_type = assert_number
            case.assert_text = assert_text
            case.save()

        return JsonResponse({"status": 10200, "message": "保存成功！"})

    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})


def edit_case(request, cid):
    environment_all = Environment.objects.all()
    case = TestCase.objects.get(id=cid)
    environment_id = case.environment
    # print(environment_id)
    return render(request, 'edit_case.html', {"environment_id": environment_id, "environments": environment_all})


def get_case_info(request):
    """获取接口数据"""
    if request.method == "POST":
        cid = request.POST.get("cid", "")
        case = TestCase.objects.get(id=cid)
        module = Module.objects.get(id=case.module.id)
        project_id = module.project.id;

        case_dict = {
            "id": case.id,
            "url": case.url,
            "case_name": case.name,
            "method": case.method,
            "header": case.header,
            "parameter_type": case.parameter_type,
            "parameter_body": case.parameter_body,
            "assert_type": case.assert_type,
            "assert_text": case.assert_text,
            "module_id": case.module.id,
            "project_id": project_id,
        }
        return JsonResponse({"status": 10200, "message": "请求成功", "data": case_dict})

    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})


def delete_case(request, cid):
    """
    删除用例
    """
    if request.method == "GET":
        try:
            testcase = TestCase.objects.get(id=cid)
        except TestCase.DoesNotExist:
            return HttpResponseRedirect("/case_list/")
        else:
            testcase.delete()
        return HttpResponseRedirect("/case_list/")
    else:
        return HttpResponseRedirect("/case_list/")
