"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from .views import IndexView, TammView, SendMsgView, TimestampView, TimedownView, WyyView
from django.views.generic.base import RedirectView
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.inventory.manager import InventoryManager
from ansible.plugins.callback import CallbackBase
from ansible.playbook.play import Play


urlpatterns = [
    url(r'^v1/$', IndexView.as_view(), name='index'),
    url(r'^v1/tamm/$', TammView.as_view(), name='tamm'),
    url(r'^v1/timestamp/$', TimestampView.as_view(), name='timestamp'),
    url(r'^v1/timedown/$', TimedownView.as_view(), name='timedown'),
    url(r'^v1/wyyword/$', WyyView.as_view(), name='wyyword'),
    # url(r'^testjson/$', TestJsonView.as_view(), name='testjson'),
    url(r'^v1/ywwuyi/', include(('ywwuyi.urls', 'ywwuyi'), namespace='ywwuyi')),
    # url(r'^send_group_msg', SendMsgView.as_view(), name='sendmsg'),
    url(r'^v1/favicon.ico$', RedirectView.as_view(url=r'static/img/favicon.ico')),
]
