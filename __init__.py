try:
    from devcon_win_copy import *
except:
    import os
    file_path = os.path.abspath(__file__)
    file_path_parsed = '\\'.join(file_path.split('\\')[:len(file_path.split('\\'))-1])+'\\devcon_win.py'
    exec(open(file_path_parsed).read())
    from devcon_win_copy import *

