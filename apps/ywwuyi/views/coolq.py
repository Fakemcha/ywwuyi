# -*- coding: UTF-8 -*-

from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from ywwuyi.cqrequest import send_group_msg, send_private_msg, delete_msg, ban


class SendGroupMsgView(View):

    def post(self, request):
        result_data = {}
        data = request.POST
        print(data)
        msg = data["message"]
        group_id = data["group_id"]
        result = send_group_msg(msg, group_id)
        print(result)
        # result_data["info"] = "success"
        return JsonResponse(result, safe=False, status=200,
                            json_dumps_params={'ensure_ascii': False})
        # return JsonResponse(result_data, safe=False, status=200,
        #                     json_dumps_params={'ensure_ascii': False})


class SendPrivateMsgView(View):

    def post(self, request):
        result_data = {}
        data = request.POST
        msg = data["message"]
        user_id = data["user_id"]
        result = send_private_msg(msg, user_id)
        print(result)
        # result_data["info"] = "success"
        return JsonResponse(result, safe=False, status=200,
                            json_dumps_params={'ensure_ascii': False})


class DeleteMsgView(View):

    def post(self, request):
        result_data = {}
        data = request.POST
        message_id = data["message_id"]
        result = delete_msg(message_id)
        print(result)
        # result_data["info"] = "success"
        return JsonResponse(result, safe=False, status=200,
                            json_dumps_params={'ensure_ascii': False})


class BanView(View):

    def post(self, request):
        result_data = {}
        data = request.POST
        group_id = data["group_id"]
        user_id = data["user_id"]
        seconds = data["seconds"]
        result = ban(group_id, user_id, seconds)
        print(result)
        # result_data["info"] = "success"
        return JsonResponse(result, safe=False, status=200,
                            json_dumps_params={'ensure_ascii': False})