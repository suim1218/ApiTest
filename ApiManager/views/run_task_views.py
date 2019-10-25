from ApiManager.models import Project, Module, TestCase
import json
import os
from wang_http import settings
from django.http import HttpResponseRedirect, JsonResponse

BASE_PATH = settings.BASE_DIR.replace("\\", "/")

EXTEND_DIR = BASE_PATH + "/tasks/"
RUN_TASK = BASE_PATH + "/ApiManager/views/"
from tasks.task_thread import TaskThread

'''
def write_project_case_data(pid):
    modules = Module.objects.filter(project_id=pid)

    for module in modules:
        cases = TestCase.objects.filter(module_id=module.id)
        case_list = []
        test_data = {}
        for case in cases:
            case_list.append(case.id)

        for cid in case_list:
            case = TestCase.objects.get(id=cid)
            if case.method == 1:
                method = "get"
            elif case.method == 2:
                method = "post"
            else:
                method = "null"

            if case.parameter_type == 1:
                parameter_type = "form"
            else:
                parameter_type = "json"

            if case.assert_type == 1:
                assert_type = "contains"
            else:
                assert_type = "mathches"

            test_data[case.name] = {
                "url": case.url,
                "method": method,
                "header": case.header,
                "parameter_type": parameter_type,
                "parameter_body": case.parameter_body,
                "assert_type": assert_type,
                "assert_text": case.assert_text,
            }

            case_data = json.dumps(test_data, indent=4)
            case_data = case_data.encode('utf-8').decode('unicode_escape')

            with(open(EXTEND_DIR + "test_data_list.json", "w", encoding='utf-8')) as f:
                f.write(case_data)
'''


def run_project_task(request):
    if request.method == "POST":
        pid = request.POST.get("pid", "")
        # print(pid)
        TaskThread(pid).run_cases()

        # write_project_case_data(pid)
        # run_cmd = "python  " + EXTEND_DIR + "run_tests.py"
        # print("运行的命令", run_cmd)
        # os.system(run_cmd)
        # sleep(2)

        # project = Project.objects.get(id=pid)
        # project.status = 2
        # project.save()
        return JsonResponse({"message": "运行完成，请查看测试报告"})
