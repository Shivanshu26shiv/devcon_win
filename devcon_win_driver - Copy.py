'''

'''


import sys
import ctypes
import getpass

try:
    import devcon_win_copy
    from devcon_win_copy import DevconClass
except ModuleNotFoundError:
    exec(open("devcon_win.py").read())


################################################
# Options without admin privilege:
hardware_parm = 'disable' # (status change requires admin privilege)
hardware_id = devcon_win_copy.HP_TrueVision_HD() # (press space after 'devcon_win_copy.' for options)
################################################


# refer https://stackoverflow.com/a/41930586
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    devcon_object = DevconClass()
    # d = devcon_object.get_hardware_names_dict()
    print(devcon_object.devcon_win_func(hardware_parm, hardware_id))


if hardware_parm in ['status', 'find'] or is_admin():
    main()
else:
    # Re-run the program with admin rights
    print('User '+getpass.getuser()+' is not admin. Trying to execute with admin privilege...')
    # below statement will run only the command which needed admin pivilege, nothing else
    if ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1) != 42:
        print('Command execution failed!')
    else:
        print('Command executed successfully!')
