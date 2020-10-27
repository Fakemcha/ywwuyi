import threading
from common.logs import write_test_log
from .config import timedtaskPatterns


# def func1(name):
#     s = "This is thread {},active count {}".format(name, str(threading.activeCount()))
#     print (s)
#     write_test_log(s, filename="thread.log")
#     threading.Timer(8, func1, (name,)).start()


#由此来创建和控制timer线程
class TimedtaskController(object):
    """使用单例模式"""
    def __init__(self):
        self.tasks = {}

    def makekeep(self, fun, ttp):
        def keep():
            try:
                fun()
            except Exception as e:
                print(e)
            # distance = ttp.get_next_distance()
            # method = ttp.method
            # t = threading.Timer(distance, self.makekeep(method, ttp), ())
            # self.tasks[ttp.name].cancel()
            # # t.name("ywwuyi")
            # t.name = "ywwuyi"
            # self.tasks[ttp.name] = t
            # t.start()
            self.add_task(ttp)
        return keep

    def add_task(self, ttp):
        """
        创建一个线程,并启动线程,维护一个ttp的执行
        :param ttp: timedtaskPatterns
        :return:
        """
        distance = ttp.get_next_distance()
        method = ttp.method
        name = ttp.get_name()
        self.cancel_task(name)
        t = threading.Timer(distance, self.makekeep(method, ttp), ())
        t.name = name
        t.start()
        self.tasks[name] = t

    def cancel_task(self, name):
        if name in self.tasks:
            self.tasks[name].cancel()
            del self.tasks[name]

    def get_task_name(self):
        res = ""
        for name in self.tasks:
            res += name
            res += "\n"
        return res

    def run(self):
        # for ttp in timedtaskPatterns:
        #     distance = ttp.get_next_distance()
        #     method = ttp.method
        #     threading.Timer(distance, self.makekeep(method, ttp), ()).start()
        for ttp in timedtaskPatterns:
            self.add_task(ttp)
        # for key in self.tasks:
        #     self.tasks[key].start()

    def get_tasks(self):
        return self.tasks


timedtaskController = TimedtaskController()

# if __name__ == "__main__":
#     print("active count {}".format(str(threading.activeCount())))
#     timedtaskController.run()