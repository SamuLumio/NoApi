import noapi, time, settings, tkinter, settings_gui.tkinter

noapi.Node(1234, __import__(__name__))
time.sleep(0.1)

r = noapi.Remote(1234, 'localhost').control_portal

test_list = ["yo", "mama", r, None]
settings.setup('test')
test_setting = settings.Toggle('toggle', True)

string = "sdhdfhbdsth"


def raise_error():
	raise AttributeError("yo mama")


# print("Alkaa")
# r.test_list.append(test_setting)
# test_setting.set(False)
# print(test_list[-1].value)


window = tkinter.Tk()
settings_gui.tkinter.section_frames.SectionFrame(window, r.settings.base.default_section).pack()
window.mainloop()
