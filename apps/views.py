import os
import json
import random
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from ywwuyi.cqrequest import send_group_msg
from apps.settings import PROJECT_DIR


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TimestampView(TemplateView):
    template_name = 'timestamp.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TimedownView(TemplateView):
    template_name = 'timedown.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TammView(TemplateView):
    template_name = 'tamm/tamm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class WyyView(TemplateView):

    def get(self, request):
        result = {}
        try:
            with open(os.path.join(PROJECT_DIR, 'public', 'static', 'cqcache', 'wyy_word.json'), mode="r") as f:
                wyy_words = json.loads(f.read())
            wyy_word = wyy_words[random.choice(list(wyy_words))]["text"]
            result["status"] = "ok"
            result["data"] = {}
            result["data"]["word"] = wyy_word
        except Exception as e:
            result["status"] = "failed"
        return JsonResponse(result, safe=False, status=200, json_dumps_params={'ensure_ascii': False})



# class TestJsonView(View):
#
#     def get(self, request):
#         data = {}
#         data["name"] = "tamm"
#         data["age"] = 25
#         import json
#         json_data = json.dumps(data)
#         from django.http import HttpResponse, JsonResponse
#         return JsonResponse(json_data, safe=False)

class SendMsgView(View):

    # def get(self, request):
    #     result_data = {}
    #     data = request.GET
    #     print(data)
    #     # group_id = "1037584440"
    #     msg = data["message"]
    #     group_id = data["group_id"]
    #     send_group_msg(msg, group_id)
    #
    #     result_data["info"] = "success"
    #     return JsonResponse(result_data, safe=False, status=200,
    #                         json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        result_data = {}
        data = request.POST
        # print(data)
        # group_id = "1037584440"
        msg = data["message"]
        group_id = data["group_id"]
        result = send_group_msg(msg, group_id)
        print(result)
        result_data["info"] = "success"
        return JsonResponse(result_data, safe=False, status=200,
                            json_dumps_params={'ensure_ascii': False})
