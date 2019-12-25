<h2>devcon_win - to access <a href='https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/devcon' target='_blank'>devcon.exe</a> in NT systems</h2>
With devcon_win, you can access all functions of devcon.exe. In addition, you can see all available drivers as a function.
<br>See below for more details.
<h3>Getting it:</h3>
To download devcon_win, either fork this github repo or simply use 
Pypi via pip.


```
$ pip install devcon_win
```

<h3>Using it:</h3>

<ol>

<li>The devcon.exe present in this rep is for '64 bit windows 10'. If your windows's version is different then download <a href='https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/devcon' target='_blank'>devcon.exe</a> as per requirement.</li>
<li>Move devcon.exe in the script's directory.</li>
<li>Install devcon_win from pip.</li>

<li>Use devcon_win_driver.py as a sample to disable webcam or any other driver as per requirement {BE CAREFUL}:

```python
try:
    import devcon_win_copy
    from devcon_win_copy import DevconClass
except ModuleNotFoundError:
    exec(open("devcon_win.py").read())
    import devcon_win_copy
import os

hardware_parm = 'disable' # (status change requires admin privilege)
hardware_id = devcon_win_copy.HP_TrueVision_HD() # (press space after 'devcon_win_copy.' for options)
devcon_object = DevconClass()
print(devcon_object.devcon_win_func(hardware_parm, hardware_id))
if os.path.exists("devcon_win_copy.py"):
    os.remove("devcon_win_copy.py")
```
</li>

</ol>

