import noapi, time, settings

noapi.Server(1234, __import__(__name__)).start_in_thread()
time.sleep(0.1)

c = noapi.Client('localhost', 1234)


test_list = ["yo", "mama", c]
settings.setup('test')
test_setting = settings.Toggle("toggle", True)


print(isinstance(c.test_setting, settings.Toggle))
