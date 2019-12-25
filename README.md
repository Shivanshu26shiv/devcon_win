<h2>devcon_win - to access devcon.exe in NT systems</h2>
With devcon_win, you can access all functions of devcon.exe. In addition, you can see all available drivers as a function.
<br>See below for more details.
<h3>Getting it:</h3>
To download devcon_win, either fork this github repo or simply use 
Pypi via pip.
```
$ pip install devcon_win
```

<h3>Using it:</h3>

```python
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
print(devcon_object.devcon_win_func(hardware_parm, hardware_id))
if os.path.exists("devcon_win_copy.py"):
    os.remove("devcon_win_copy.py")
```