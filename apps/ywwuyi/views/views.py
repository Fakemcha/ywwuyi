import json
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from ywwuyi.command.handler import commandHandler
from ywwuyi.command.pattern import CommandPattern
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from ywwuyi.poi import handle_url


class TestJsonView(View):

    def get(self, request):
        data = {}
        data["name"] = "tamm"
        data["age"] = 25
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)


class CommandView(View):

    def get(self, request):
        return JsonResponse(commandHandler.get_command_patterns_name(), safe=False,
                            json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        error_data = {}
        res_data = {}
        iserror = False
        print(request.POST)
        data = request.POST
        regex = data.get("regex", "")
        private = data.get("private", None)
        group = data.get("group", None)
        description = data.get("description", "")
        call = data.get("call", "")
        if regex == "":
            error_data["info"] = "regex不能为空"
            iserror = True
        elif private is not None and not isinstance(json.loads(private), list):
            error_data["info"] = "private格式错误"
            iserror = True
        elif group is not None and not isinstance(json.loads(group), list):
            error_data["info"] = "group格式错误"
            iserror = True
        elif not call.startswith("http"):
            error_data["info"] = "call格式错误"
            iserror = True
        if iserror:
            return JsonResponse(error_data, safe=False, status=400,
                                json_dumps_params={'ensure_ascii': False})
        cp = CommandPattern(regex, handle_url(call), description, private, group)
        commandHandler.add_command_pattern(cp)
        res_data["info"] = "success"
        return JsonResponse(res_data, safe=False, status=201,
                            json_dumps_params={'ensure_ascii': False})

    def delete(self, request):
        # data = request.POST
        print("This is delete")
        # from django.http import QueryDict
        # data = QueryDict(request.body)
        # for key in data:
        #     print(key)
        # print("-"*50)
        # print(data[" name"])
        # print("-" * 50)
        # print(data.get("regex", "goushi"))
        print("GET:")
        print(request.GET)
        print("POST:")
        print(request.POST)
        print("BODY:")
        from django.http import QueryDict
        print(QueryDict(request.body))
        return JsonResponse({"info":"success"}, safe=False,
                            json_dumps_params={'ensure_ascii': False})

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(CommandView, self).dispatch(*args, **kwargs)


class CommandView2(View):

    def get(self, request):
        return HttpResponse(json.dumps(commandHandler.get_command_patterns_name(),ensure_ascii=False), content_type="application/json,charset=utf-8")
        # return JsonResponse(commandHandler.get_command_patterns_name(), safe=False, json_dumps_params={'ensure_ascii': False})
        # return JsonResponse(commandHandler.get_command_patterns_name(), safe=False, content_type="application/json,charset=utf-8", json_dumps_params={'ensure_ascii': False})


class SBPZ(View):

    def get(self, request):
        data = {
            "message": "煞笔胖子",
            "group_id": "532799508"
        }
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})