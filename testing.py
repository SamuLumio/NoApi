import noapi, time, settings, tkinter, settings_gui.tkinter

n = noapi.Node(1234, __import__(__name__), log=True)
print(n.active)
time.sleep(0.1)
print(n.active)

r = noapi.Remote(1234, 'localhost', n).control_portal

list = ["yo", "mama", r, None]
settings.setup('test')
setting = settings.Toggle('toggle', True)

string = "sdhdfhbdsth"


def raise_error():
	raise AttributeError("yo mama")

r_list = r.list
r_list.append(1)


n.deactivate()
time.sleep(1)
print(n.active)