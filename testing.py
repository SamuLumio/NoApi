import noapi, time, settings, tkinter, settings_gui.tkinter

noapi.Server(1234, __import__(__name__)).start_in_thread()
time.sleep(0.1)

c = noapi.Client('localhost', 1234)


test_list = ["yo", "mama", c]
settings.setup('test')
test_setting = settings.Multichoice('multichoice', ["1", "2", "3"], ["2"])

print(test_setting)
c.test_setting.value = ["2"]
print(test_setting)

# window = tkinter.Tk()
# settings_gui.tkinter.section_frames.SectionFrame(window, c.settings.base.default_section).pack()
# window.mainloop()
