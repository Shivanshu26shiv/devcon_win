'''

'''


try:
    import devcon_win_copy
    from devcon_win_copy import DevconClass
except ModuleNotFoundError:
    exec(open("devcon_win.py").read())
    import devcon_win_copy
import os

hardware_parm = 'find' # (status change requires admin privilege)
hardware_id = devcon_win_copy.HP_TrueVision_HD() # (press space after 'devcon_win_copy.' for options)
devcon_object = DevconClass()
# d = devcon_object.get_hardware_names_dict()
print(devcon_object.devcon_win_func(hardware_parm, hardware_id))
if os.path.exists("devcon_win_copy.py"):
    os.remove("devcon_win_copy.py")
