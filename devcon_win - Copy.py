'''
Be careful
'''

import sys
import subprocess


class NonWindowsOs(Exception):
    pass


class DevconClass:

    def __init__(self, hardware_parm='find', hardware_id='*'):
        self.hardware_parm = hardware_parm
        self.hardware_id = hardware_id

    def devcon_win_func(self, hardware_parm, hardware_id):
        self.hardware_id = hardware_id
        """This function uses devcon. devcon_win_func(hardware_parm, instance_name)
            Examples of hardware_parm: find, enable, disable...
            List of instance_names: devcon_object.get_hardware_names_dict()"""

        if not hasattr(sys, 'getwindowsversion'):
            raise NonWindowsOs("Operating system is not Windows")

        var = 'devcon '+hardware_parm+' '+'@"'+hardware_id+'"'
        return subprocess.getoutput(var)

    def get_hardware_names_dict(self):
        parsed_info = self.devcon_win_func('find', '*').splitlines()
        hardware_names_dict = {}
        for e in parsed_info:
            e = e.split(':')
            if len(e) > 1:
                e[0] = repr(e[0].strip())
                e[1] = e[1].strip().replace(' ', '_')
                hardware_names_dict[e[1]]= e[0]

        return hardware_names_dict


if __name__ == "__main__":
    import os
    from shutil import copyfile

    devcon_internal_object = DevconClass()
    func_lst = []
    internal_dict = devcon_internal_object.get_hardware_names_dict()
    for instance_name, instance_id in internal_dict.items():
        instance_name = instance_name.translate({ord(cardinal): '_' for cardinal in r'-()/.!@#$%^&*<>?\|}{~:}'})
        try:
            func_lst.append("def " + instance_name + "(): return " + instance_id)
        except SyntaxError:
            continue

    def filer():
        copyfile("devcon_win.py", "devcon_win_copy.py")
        final_lst = os.linesep.join(func_lst)
        with open("devcon_win_copy.py", 'a') as f:
            f.write(final_lst)

    try:
        os.remove("devcon_win_copy.py")
        filer()
    except (FileNotFoundError, OSError):
        filer()

