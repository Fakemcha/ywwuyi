import os
import time
import threading
from apps.settings import PROJECT_DIR
from django.apps import AppConfig
from ywwuyi.games.guess_keyword import forbidden_words_game
from ywwuyi.timedtask.controller import timedtaskController


class ywwuyiConfig(AppConfig):
    name = 'ywwuyi'

    def ready(self):
        # super().ready()
        print("初始化程序")
        # if os.path.exists(PROJECT_DIR + "/tmp/keywords.json"):
        #     print("读取禁语")
        #     with open(PROJECT_DIR + "/tmp/keywords.json", mode="r") as f:
        #         d = json.loads(f.read())
        #     guess_keyword.player_dict = d.copy()
        #     print(d)
        # timedtaskController.run()

        # from ywwuyi.miraiwebsocket import mirai_session
        from ywwuyi.qqproxy.mirai import mirai_session

        def get_miraiclient():
            def miraiclient():
                while True:
                    mirai_session.start()
                    time.sleep(10)

            return miraiclient

        def get_mirairelease():
            def mirairelease():
                while True:
                    time.sleep(10)
                    mirai_session.release()
                    

            return mirairelease

        DJANGO_AUTORELOAD_ENV = 'RUN_MAIN'
        if os.environ.get(DJANGO_AUTORELOAD_ENV) == 'true':
            # if not os.path.exists(PROJECT_DIR + "/tmp/init.flag"):
            #     with open(PROJECT_DIR + "/tmp/init.flag", mode="w") as f:
            #         f.write("1")
            mirai_thread = threading.Thread(target=get_miraiclient())
            mirai_thread.start()

            # mirai_release_thread = threading.Thread(target=get_mirairelease())
            # mirai_release_thread.start()

            timedtaskController.run()

        # forbidden_words_game.read_forbidden_words()


