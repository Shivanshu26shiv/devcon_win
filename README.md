<h2>devcon_win - to access <a href='https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/devcon' target='_blank'>devcon.exe</a> in NT systems</h2>
With devcon_win, you can access all functions of devcon.exe. In addition, you can see all available drivers as a function.
<br>See below for more details.
<h3>Getting it:</h3>
To download devcon_win, either fork this github repo or simply use 
Pypi via pip.


```
$ pip install devcon_win
```

<h3>Compatibility:</h3>
devcon_win is compatible for both python2 and python3.

<h3>Using it:</h3>

<ol>

<li>The devcon.exe present in this rep is for '64 bit windows 10'. If your windows's version is different then download <a href='https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/devcon' target='_blank'>devcon.exe</a> as per requirement.</li>
<li>Move devcon.exe in the current script's directory or any path defined in environment variables say Python27/Scripts.</li>
<li>Install devcon_win from pip.</li>

<li>Use <b>devcon_win_driver.py</b> as a sample to <b>disable webcam</b> or any other driver as per requirement <b>{BE CAREFUL}</b>:

```python
import devcon_win
print(devcon_win.HP_TrueVision_HD('enable')) # will show options after 'devcon_win.'
```
</li>

</ol>

<b>
Note: if user is not administrator, and parm passed is intended to change status of hardware instance, (like enable/disable) then code though asks user's permission and executes but returns None. 
</b>
