import json
import requests
from django.contrib import auth
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from ApiManager.models import Project, Module, Environment


def case_list(request):
    return render(request, 'case_list.html')


def case_debug(request):
    """
    测试用例的调试
    """
    if request.method == "POST":
        environment = request.POST.get("environment", "")
        url = request.POST.get("url", "")  # URL
        method = request.POST.get("method", "")  # 方法
        header = request.POST.get("header", "")  # header
        par_type = request.POST.get("type", "")  # 参数类型
        par_body = request.POST.get("parameter", "")  # 参数
        environment_obj = Environment.objects.get(name=environment)
        environment_address = environment_obj.address

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
            r = requests.get(environment_address + '/' + url, params=payload, headers=header)
            result_text = r.text

        if method == "post":
            if par_type == "form":
                r = requests.post(environment_address + '/' +url, data=payload, headers=header)
                result_text = r.text

            if par_type == "json":
                r = requests.post(environment_address + '/' +url, json=payload, headers=header)
                result_text = r.text

        return JsonResponse({"result": result_text})
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
        case_name = request.POST.get("case_name", "")
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        header = request.POST.get("header", "")
        parameter_type = request.POST.get("par_type", "")
        parameter_body = request.POST.get("par_body", "")
        assert_type = request.POST.get("ass_type", "")
        assert_text = request.POST.get("ass_text", "")
        cid = request.POST.get("cid", "")

        print("url", url)
        print("method", method)
        print("header", header)
        print("parameter_type", parameter_type)
        print("parameter_body", parameter_body)
        print("assert_type", assert_type)
        print("assert_text", assert_text)
        print("module_id", module_id)
        print("name", name)
        print("cid", cid)

        '''
        if name == "":
            return JsonResponse({"status": 10101, "message": "用例名称不能为空"})

        if module_id == "":
            return JsonResponse({"status": 10103, "message": "所属的模块不能为空"})

        if assert_type == "" or assert_text == "":
            return JsonResponse({"status": 10102, "message": "断言的类型或文本不能为空"})

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
            ret = TestCase.objects.create(name=name, module_id=module_id,
                                          url=url, method=method_number, header=header,
                                          parameter_type=parameter_number, parameter_body=parameter_body,
                                          assert_type=assert_number, assert_text=assert_text)
        else:
            case = TestCase.objects.get(id=cid)
            case.name = name
            case.module_id = module_id
            case.url = url
            case.method = method_number
            case.header = header
            case.parameter_type = parameter_number
            case.parameter_body = parameter_body
            case.assert_type = assert_number
            case.assert_text = assert_text
            case.save()

        return JsonResponse({"status": 10200, "message": "创建成功！"})

    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})
'''
