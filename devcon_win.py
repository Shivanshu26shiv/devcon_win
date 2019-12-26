from __future__ import unicode_literals
import os
import sys
import time
import ctypes
import inspect
import subprocess
import getpass
import logging
from shutil import copyfile

class DevconClass:

    def get_hardware_names_dict(self):
        try:
            parsed_info = subprocess.getoutput('devcon find ' + '@"*"').splitlines()
        except AttributeError:
            parsed_info = subprocess.check_output('devcon find ' + '@"*"').splitlines()

        func_lst = ["logging.debug('Status:')",
                    "logging.debug('')"]
        for instance in parsed_info:
            instance = instance.split(':')
            if len(instance) > 1:
                instance[0] = repr(instance[0].strip())
                # https://stackoverflow.com/a/23996445
                instance[1] = instance[1].strip().translate({ord(cardinal): '_' for cardinal in ' -()/.!@#$%^&*<>?\|}{~:}'})

                try:
                    func_lst.extend(
                        ["def " + instance[1] + "(arg='status'):",
                         "   logging.debug('Argument: '+str(arg))",
                         "   if arg in ['status', 'find'] or is_admin(): ",
                         str(compat_text[0].replace('to_be_replaced', instance[0])),
                         str(compat_text[1]),
                         str(compat_text[2]),
                         "         logging.debug('Authentication: failed')",
                         "      else:",
                         "         logging.debug('Authentication: successful')",
                         "      logging.debug('')",
                         "   time.sleep(2)",
                         "   return("+instance[1] + "('status'))"]
                    )
                except SyntaxError:
                    continue

        # logging.debug(func_lst)
        func_lst.extend([
            "try:",
            "    os.remove('"+CURRENT_FILE_NAME_COPY+"')",
            "except WindowsError:",
            "    pass"
        ])
        return func_lst


if __name__ != '__main__':

    logging.basicConfig(level=logging.DEBUG, format='%(message)s')

    assert sys.version_info >= (2, 7), 'Python version should be at least 2.7'

    assert hasattr(sys, 'getwindowsversion'), "Operating system is not Windows"

    CURRENT_FILE_NAME = 'devcon_win.py'
    CURRENT_FILE_NAME_COPY = 'devcon_win_copy.py'

    to_be_replaced = 'to_be_replaced'
    if sys.version_info[0] == 3:
        compat_text = ["      return subprocess.getoutput('devcon '+arg+  ' @\"'" + to_be_replaced + ')',
                       "   else:",
                       "      if (ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, caller_script, None, 0)) !=42:"]
    else:
        compat_text = ["      return subprocess.check_output('devcon '+arg+  ' @\"'" + to_be_replaced + ')',
                       "   else:",
                       "      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:"]


    # refer https://stackoverflow.com/a/41930586
    def is_admin():
        logging.debug('Authenticating with user: ' + getpass.getuser())
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False


    try:
        os.remove(CURRENT_FILE_NAME_COPY)
    except:
        pass

    copyfile(CURRENT_FILE_NAME, CURRENT_FILE_NAME_COPY)

    frame = inspect.stack()[-1]
    module = inspect.getmodule(frame[0])
    file_path = module.__file__
    caller_script = file_path.split('/')[-1]

    int_devcon_object = DevconClass()
    final_lst = os.linesep.join(int_devcon_object.get_hardware_names_dict())
    with open(CURRENT_FILE_NAME_COPY, 'a') as f:
        f.write(final_lst)

    from devcon_win_copy import *
