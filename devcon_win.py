from __future__ import unicode_literals

import ctypes
import getpass
import inspect
import os
import subprocess
import sys
from shutil import copyfile
import time


class DevconClass(object):

    @staticmethod
    def get_hardware_names_dict():
        try:
            parsed_info = subprocess.getoutput('devcon find ' + '@"*"').splitlines()
        except AttributeError:
            parsed_info = subprocess.check_output('devcon find ' + '@"*"').splitlines()

        func_lst = []
        for instance in parsed_info:
            instance = instance.split(':')
            if len(instance) > 1:
                instance[0] = repr(instance[0].strip())
                # https://stackoverflow.com/a/23996445
                instance[1] = instance[1].strip().translate({ord(cardinal): '_' for cardinal in u' -()/.!@#$%^&*<>?\\|}{~:"\'+~`=[];|,€'})

                try:
                    func_lst.extend(
                        ["def " + instance[1] + "(arg='status'):",
                         "   print('Argument: '+str(arg))",
                         "   if arg in ['status', 'find'] or is_admin(): ",
                         str(compat_text[0].replace('to_be_replaced', instance[0])),
                         str(compat_text[1]),
                         str(compat_text[2]),
                         "         print('Authentication: failed')",
                         "      else:",
                         "         print('Authentication: successful')",
                         "      print('')",
                         "   print('Refreshing...')",
                         "   print('')",
                         "   time.sleep(3)",
                         "   return(" + instance[1] + "('status'))"]
                    )
                except SyntaxError:
                    continue

        # print(func_lst)
        '''
        func_lst.extend([
            "try:",
            "    os.remove('"+CURRENT_FILE_NAME_COPY_PATH+"')",
            "except WindowsError:",
            "    pass"
        ])

        func_lst.extend([
            "del [f, caller_script, CURRENT_FILE_NAME_COPY, CURRENT_FILE_NAME, CURRENT_FILE_NAME_COPY_PATH,"
            "     CURRENT_FILE_NAME_PATH, DevconClass, compat_text, copyfile, ctypes, final_lst, frame, getpass,"
            "     inspect, int_devcon_object, unicode_literals, is_admin, module, script_file_path, script_file_path_list,"
            "     to_be_replaced]"])
        '''

        return func_lst


assert sys.version_info >= (2, 7), 'Python version should be at least 2.7'

assert hasattr(sys, 'getwindowsversion'), "Operating system is not Windows"

script_file_path_list = os.path.abspath(__file__).split('\\')
CURRENT_FILE_NAME_PATH = '\\'.join(os.path.abspath(__file__).split('\\')[:len(script_file_path_list) - 1]) + '\\' + 'devcon_win.py'
CURRENT_FILE_NAME_COPY_PATH = CURRENT_FILE_NAME_PATH.replace('.py', '_copy.py')

if sys.version_info[0] == 3:
    compat_text = ["      return subprocess.getoutput('devcon '+arg+  ' @\"'to_be_replaced"')',
                   "   else:",
                   "      if (ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, caller_script, None, 0)) !=42:"]
else:
    compat_text = ["      return subprocess.check_output('devcon '+arg+  ' @\"'to_be_replaced"')',
                   "   else:",
                   "      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:"]


# refer https://stackoverflow.com/a/41930586
def is_admin():
    print('Authenticating with user: ' + getpass.getuser())
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


try:
    os.remove(CURRENT_FILE_NAME_COPY_PATH)
except Exception:
    pass

copyfile(CURRENT_FILE_NAME_PATH, CURRENT_FILE_NAME_COPY_PATH)

try:
    file_path = inspect.getmodule(inspect.stack()[-1][0]).__file__
    caller_script = file_path.split('/')[-1]
except AttributeError:
    caller_script = __file__

int_devcon_object = DevconClass()
# print(final_lst)
with open(CURRENT_FILE_NAME_COPY_PATH, 'a') as file_obj:
    file_obj.write(os.linesep.join(int_devcon_object.get_hardware_names_dict()))

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from devcon_win_copy import *
