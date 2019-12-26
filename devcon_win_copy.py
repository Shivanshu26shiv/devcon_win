from __future__ import unicode_literals
import os
import sys
import ctypes
import inspect
import subprocess
from shutil import copyfile
import getpass
import time

assert sys.version_info >= (2, 7), 'Python version should be at least 2.7'

assert hasattr(sys, 'getwindowsversion'), "Operating system is not Windows"

CURRENT_FILE_NAME = 'devcon_win.py'
CURRENT_FILE_NAME_COPY = 'devcon_win_copy.py'

to_be_replaced = 'to_be_replaced'
if sys.version_info[0] == 3:
    compat_text = ["      return subprocess.getoutput('devcon '+arg+  ' @\"'"+ to_be_replaced + ')',
                   "   else:",
                   "      if (ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, caller_script, None, 0)) !=42:"]
else:
    compat_text = ["      return subprocess.check_output('devcon '+arg+  ' @\"'" + to_be_replaced + ')',
                   "   else:",
                   "      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:"]


# refer https://stackoverflow.com/a/41930586
def is_admin():
    print('Authenticating with user: '+getpass.getuser())
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


class DevconClass:

    def get_hardware_names_dict(self):
        try:
            parsed_info = subprocess.getoutput('devcon find ' + '@"*"').splitlines()
        except AttributeError:
            parsed_info = subprocess.check_output('devcon find ' + '@"*"').splitlines()

        func_lst = ["print('Status:')",
                    "print('')"]
        for instance in parsed_info:
            instance = instance.split(':')
            if len(instance) > 1:
                instance[0] = repr(instance[0].strip())
                # https://stackoverflow.com/a/23996445
                instance[1] = instance[1].strip().translate({ord(cardinal): '_' for cardinal in ' -()/.!@#$%^&*<>?\|}{~:}'})

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
                         "   time.sleep(2)",
                         "   return("+instance[1] + "('status'))"]
                    )
                except SyntaxError:
                    continue

        # print(func_lst)
        func_lst.extend([
            "try:",
            "    os.remove('"+CURRENT_FILE_NAME_COPY+"')",
            "except WindowsError:",
            "    pass"
        ])
        return func_lst


if __name__ != '__main__':

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
print('Status:')
print('')
def PS_2_Compatible_Mouse(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\ETD0711\\4&1E609E49&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(PS_2_Compatible_Mouse('status'))
def Direct_memory_access_controller(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0200\\4&1E609E49&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Direct_memory_access_controller('status'))
def AMD_Radeon_TM__R4_Graphics(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1002&DEV_9851&SUBSYS_81E5103C&REV_40\\3&2411E6FE&0&08')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(AMD_Radeon_TM__R4_Graphics('status'))
def Standard_PS_2_Keyboard(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\HPQ8001\\4&1E609E49&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Standard_PS_2_Keyboard('status'))
def Microsoft_ACPI_Compliant_Control_Method_Battery(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0C0A\\1')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_ACPI_Compliant_Control_Method_Battery('status'))
def ACPI_Fan(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0C0B\\0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(ACPI_Fan('status'))
def High_Definition_Audio_Controller(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1002&DEV_9840&SUBSYS_81E5103C&REV_00\\3&2411E6FE&0&09')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(High_Definition_Audio_Controller('status'))
def Speakers__High_Definition_Audio_Device_(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'SWD\\MMDEVAPI\\{0.0.0.00000000}.{3EFE33CA-4AB1-4353-8BFC-0EFFF2963B0C}')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Speakers__High_Definition_Audio_Device_('status'))
def Root_Print_Queue(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'SWD\\PRINTENUM\\PRINTQUEUES')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Root_Print_Queue('status'))
def Volume_Manager(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ROOT\\VOLMGR\\0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Volume_Manager('status'))
def PCI_standard_host_CPU_bridge(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_1581&SUBSYS_00000000&REV_00\\3&2411E6FE&0&C1')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(PCI_standard_host_CPU_bridge('status'))
def Standard_Enhanced_PCI_to_USB_Host_Controller(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_7808&SUBSYS_81E5103C&REV_39\\3&2411E6FE&0&90')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Standard_Enhanced_PCI_to_USB_Host_Controller('status'))
def Standard_Enhanced_PCI_to_USB_Host_Controller(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_7808&SUBSYS_81E5103C&REV_39\\3&2411E6FE&0&98')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Standard_Enhanced_PCI_to_USB_Host_Controller('status'))
def hp_DVDRW_GUD1N_SATA_CdRom_Device(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'SCSI\\CDROM&VEN_HP&PROD_DVDRW_GUD1N\\4&1649041&0&010000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(hp_DVDRW_GUD1N_SATA_CdRom_Device('status'))
def Microsoft_Basic_Display_Driver(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ROOT\\BASICDISPLAY\\0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_Basic_Display_Driver('status'))
def HP_Wireless_Button_Driver(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\HPQ6001\\2&DABA3FF&1')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(HP_Wireless_Button_Driver('status'))
def Microsoft_IPv4_IPv6_Transition_Adapter_Bus(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'SWD\\IP_TUNNEL_VBUS\\IP_TUNNEL_DEVICE_ROOT')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_IPv4_IPv6_Transition_Adapter_Bus('status'))
def Generic_volume(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'STORAGE\\VOLUME\\{921B2214-F7BC-11E6-824B-806E6F6E6963}#0000000012D00000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Generic_volume('status'))
def Firmware_Resource(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'UEFI\\RES_{ABEAEA64-EF28-47E5-8CAB-132D53F42DAF}\\0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Firmware_Resource('status'))
def Phantom_TAP_Windows_Adapter_V9(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ROOT\\NET\\0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Phantom_TAP_Windows_Adapter_V9('status'))
def ACPI_Thermal_Zone(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\THERMALZONE\\TZ0_')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(ACPI_Thermal_Zone('status'))
def ACPI_Thermal_Zone(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\THERMALZONE\\TZ1_')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(ACPI_Thermal_Zone('status'))
def AMD_PSP_1_0_Device(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_1537&SUBSYS_15371022&REV_00\\3&2411E6FE&0&40')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(AMD_PSP_1_0_Device('status'))
def Microsoft_Windows_Management_Interface_for_ACPI(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0C14\\0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_Windows_Management_Interface_for_ACPI('status'))
def Generic_volume(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'STORAGE\\VOLUME\\{921B2214-F7BC-11E6-824B-806E6F6E6963}#0000000000100000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Generic_volume('status'))
def Numeric_data_processor(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0C04\\4&1E609E49&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Numeric_data_processor('status'))
def Generic_USB_Hub(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'USB\\VID_0438&PID_7900\\5&3B9196FD&0&1')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Generic_USB_Hub('status'))
def Generic_volume(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'STORAGE\\VOLUME\\{921B2214-F7BC-11E6-824B-806E6F6E6963}#00000041EB100000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Generic_volume('status'))
def PCI_standard_host_CPU_bridge(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_1566&SUBSYS_81E5103C&REV_00\\3&2411E6FE&0&00')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(PCI_standard_host_CPU_bridge('status'))
def AMD_SMBus(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_780B&SUBSYS_81E5103C&REV_42\\3&2411E6FE&0&A0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(AMD_SMBus('status'))
def Composite_Bus_Enumerator(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ROOT\\COMPOSITEBUS\\0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Composite_Bus_Enumerator('status'))
def Microsoft_Virtual_Drive_Enumerator(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ROOT\\VDRVROOT\\0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_Virtual_Drive_Enumerator('status'))
def Generic_USB_Hub(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'USB\\VID_0438&PID_7900\\5&9535BF8&0&1')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Generic_USB_Hub('status'))
def Microsoft_ISATAP_Adapter(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'SWD\\IP_TUNNEL_VBUS\\ISATAP_0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_ISATAP_Adapter('status'))
def Microsoft_AC_Adapter(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\ACPI0003\\2&DABA3FF&1')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_AC_Adapter('status'))
def Microsoft_Storage_Spaces_Controller(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ROOT\\SPACEPORT\\0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_Storage_Spaces_Controller('status'))
def Microsoft_Kernel_Debug_Network_Adapter(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ROOT\\KDNIC\\0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_Kernel_Debug_Network_Adapter('status'))
def Generic_volume(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'STORAGE\\VOLUME\\{921B2214-F7BC-11E6-824B-806E6F6E6963}#0000000021100000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Generic_volume('status'))
def Microsoft_XPS_Document_Writer(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'SWD\\PRINTENUM\\{D943D8D8-F7EB-4400-8EEE-A8CFF8C894B5}')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_XPS_Document_Writer('status'))
def Motherboard_resources(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0C02\\4&1E609E49&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Motherboard_resources('status'))
def System_speaker(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0800\\4&1E609E49&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(System_speaker('status'))
def Realtek_RTL8723BE_802_11_bgn_Wi_Fi_Adapter(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_10EC&DEV_B723&SUBSYS_81C1103C&REV_00\\4&23C471C0&0&0013')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Realtek_RTL8723BE_802_11_bgn_Wi_Fi_Adapter('status'))
def USB_Root_Hub(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'USB\\ROOT_HUB20\\4&1737DEEB&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(USB_Root_Hub('status'))
def ACPI_Lid(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0C0D\\2&DABA3FF&1')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(ACPI_Lid('status'))
def PCI_standard_host_CPU_bridge(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_1583&SUBSYS_00000000&REV_00\\3&2411E6FE&0&C3')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(PCI_standard_host_CPU_bridge('status'))
def Generic_volume(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'STORAGE\\VOLUME\\{921B2214-F7BC-11E6-824B-806E6F6E6963}#0000000019100000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Generic_volume('status'))
def USB_Composite_Device(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'USB\\VID_04F2&PID_B56C\\200901010001')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(USB_Composite_Device('status'))
def High_Definition_Audio_Device(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'HDAUDIO\\FUNC_01&VEN_10EC&DEV_0282&SUBSYS_103C81E5&REV_1000\\4&22C94DEF&0&0001')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(High_Definition_Audio_Device('status'))
def HID_compliant_wireless_radio_controls(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'HID\\HPQ6001\\3&3229B8BB&0&0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(HID_compliant_wireless_radio_controls('status'))
def High_precision_event_timer(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0103\\3&2411E6FE&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(High_precision_event_timer('status'))
def UMBus_Root_Bus_Enumerator(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ROOT\\UMBUS\\0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(UMBus_Root_Bus_Enumerator('status'))
def Microsoft_ACPI_Compliant_Embedded_Controller(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0C09\\4&1E609E49&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_ACPI_Compliant_Embedded_Controller('status'))
def Generic_volume(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'STORAGE\\VOLUME\\{921B2214-F7BC-11E6-824B-806E6F6E6963}#0000005CC6100000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Generic_volume('status'))
def System_timer(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0100\\4&1E609E49&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(System_timer('status'))
def PCI_standard_host_CPU_bridge(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_1580&SUBSYS_00000000&REV_00\\3&2411E6FE&0&C0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(PCI_standard_host_CPU_bridge('status'))
def Microsoft_Device_Association_Root_Enumerator(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'SWD\\MSDAS\\{CE958E9A-424F-4C88-86F4-11314821E75A}')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_Device_Association_Root_Enumerator('status'))
def ACPI_x64_based_PC(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ROOT\\ACPI_HAL\\0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(ACPI_x64_based_PC('status'))
def AMD_A6_7310_APU_with_AMD_Radeon_R4_Graphics(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\AUTHENTICAMD_-_AMD64_FAMILY_22_MODEL_48_-_AMD_A6-7310_APU_WITH_AMD_RADEON_R4_GRAPHICS____\\_0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(AMD_A6_7310_APU_with_AMD_Radeon_R4_Graphics('status'))
def AMD_A6_7310_APU_with_AMD_Radeon_R4_Graphics(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\AUTHENTICAMD_-_AMD64_FAMILY_22_MODEL_48_-_AMD_A6-7310_APU_WITH_AMD_RADEON_R4_GRAPHICS____\\_1')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(AMD_A6_7310_APU_with_AMD_Radeon_R4_Graphics('status'))
def AMD_A6_7310_APU_with_AMD_Radeon_R4_Graphics(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\AUTHENTICAMD_-_AMD64_FAMILY_22_MODEL_48_-_AMD_A6-7310_APU_WITH_AMD_RADEON_R4_GRAPHICS____\\_2')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(AMD_A6_7310_APU_with_AMD_Radeon_R4_Graphics('status'))
def AMD_A6_7310_APU_with_AMD_Radeon_R4_Graphics(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\AUTHENTICAMD_-_AMD64_FAMILY_22_MODEL_48_-_AMD_A6-7310_APU_WITH_AMD_RADEON_R4_GRAPHICS____\\_3')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(AMD_A6_7310_APU_with_AMD_Radeon_R4_Graphics('status'))
def PCI_Express_Root_Complex(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0A08\\1')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(PCI_Express_Root_Complex('status'))
def PCI_standard_PCI_to_PCI_bridge(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_1439&SUBSYS_12341022&REV_00\\3&2411E6FE&0&12')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(PCI_standard_PCI_to_PCI_bridge('status'))
def PCI_standard_PCI_to_PCI_bridge(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_1439&SUBSYS_12341022&REV_00\\3&2411E6FE&0&13')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(PCI_standard_PCI_to_PCI_bridge('status'))
def USB_Root_Hub__xHCI_(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'USB\\ROOT_HUB30\\4&B66B6AD&0&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(USB_Root_Hub__xHCI_('status'))
def ACPI_Power_Button(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0C0C\\2&DABA3FF&1')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(ACPI_Power_Button('status'))
def Microsoft_ACPI_Compliant_System(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI_HAL\\PNP0C08\\0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_ACPI_Compliant_System('status'))
def Microsoft_Basic_Render_Driver(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ROOT\\BASICRENDER\\0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_Basic_Render_Driver('status'))
def Fax(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'SWD\\PRINTENUM\\{9D7DBACD-D102-4149-B2DB-FFEC94371EAB}')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Fax('status'))
def Send_To_OneNote_2013(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'SWD\\PRINTENUM\\{193B718A-1E01-4D6B-A655-76E094414BFB}')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Send_To_OneNote_2013('status'))
def Microphone__High_Definition_Audio_Device_(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'SWD\\MMDEVAPI\\{0.0.1.00000000}.{5353BAF2-FAC1-4234-B93A-D052967BE086}')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microphone__High_Definition_Audio_Device_('status'))
def High_Definition_Audio_Controller(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_780D&SUBSYS_81E5103C&REV_02\\3&2411E6FE&0&A2')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(High_Definition_Audio_Controller('status'))
def Microsoft_UEFI_Compliant_System(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI_HAL\\UEFI\\0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_UEFI_Compliant_System('status'))
def AMD_USB_3_0_eXtensible_Host_Controller___0100__Microsoft_(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_7814&SUBSYS_81E5103C&REV_11\\3&2411E6FE&0&80')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(AMD_USB_3_0_eXtensible_Host_Controller___0100__Microsoft_('status'))
def AMD_SATA_Controller(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_7804&SUBSYS_81E5103C&REV_39\\3&2411E6FE&0&88')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(AMD_SATA_Controller('status'))
def PCI_standard_host_CPU_bridge(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_1585&SUBSYS_00000000&REV_00\\3&2411E6FE&0&C5')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(PCI_standard_host_CPU_bridge('status'))
def ACPI_Fixed_Feature_Button(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\FIXEDBUTTON\\2&DABA3FF&1')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(ACPI_Fixed_Feature_Button('status'))
def Generic_Bluetooth_Adapter(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'USB\\VID_0BDA&PID_B008\\00E04C000001')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Generic_Bluetooth_Adapter('status'))
def Motherboard_resources(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0C02\\90')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Motherboard_resources('status'))
def WDC_WD5000LPLX_60ZNT_SATA_Disk_Device(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'SCSI\\DISK&VEN_WDC&PROD_WD5000LPLX-60ZNT\\4&1649041&0&000000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(WDC_WD5000LPLX_60ZNT_SATA_Disk_Device('status'))
def PCI_standard_host_CPU_bridge(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_1582&SUBSYS_00000000&REV_00\\3&2411E6FE&0&C2')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(PCI_standard_host_CPU_bridge('status'))
def NDIS_Virtual_Network_Adapter_Enumerator(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ROOT\\NDISVIRTUALBUS\\0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(NDIS_Virtual_Network_Adapter_Enumerator('status'))
def Realtek_PCIe_GBE_Family_Controller(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_10EC&DEV_8168&SUBSYS_81E5103C&REV_15\\4&110AC11B&0&0012')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Realtek_PCIe_GBE_Family_Controller('status'))
def Generic_volume(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'STORAGE\\VOLUME\\{921B2214-F7BC-11E6-824B-806E6F6E6963}#0000001D4C100000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Generic_volume('status'))
def USB_Root_Hub(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'USB\\ROOT_HUB20\\4&175FD1E6&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(USB_Root_Hub('status'))
def Microsoft_Wi_Fi_Direct_Virtual_Adapter(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'{5D624F94-8850-40C3-A3FA-A4FD2080BAF3}\\VWIFIMP_WFD\\5&378A1F1D&0&01')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_Wi_Fi_Direct_Virtual_Adapter('status'))
def Microsoft_Hosted_Network_Virtual_Adapter(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'{5D624F94-8850-40C3-A3FA-A4FD2080BAF3}\\VWIFIMP_SAP\\5&378A1F1D&0&02')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_Hosted_Network_Virtual_Adapter('status'))
def System_CMOS_real_time_clock(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0B00\\4&1E609E49&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(System_CMOS_real_time_clock('status'))
def System_board(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0C01\\4&1E609E49&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(System_board('status'))
def PCI_standard_ISA_bridge(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_780E&SUBSYS_81E5103C&REV_11\\3&2411E6FE&0&A3')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(PCI_standard_ISA_bridge('status'))
def Microsoft_System_Management_BIOS_Driver(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ROOT\\MSSMBIOS\\0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Microsoft_System_Management_BIOS_Driver('status'))
def Programmable_interrupt_controller(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0000\\4&1E609E49&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Programmable_interrupt_controller('status'))
def HP_TrueVision_HD(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'USB\\VID_04F2&PID_B56C&MI_00\\7&4B046F5&0&0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(HP_TrueVision_HD('status'))
def Generic_PnP_Monitor(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'DISPLAY\\AUO2E3C\\4&7DBB3CD&0&UID256')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Generic_PnP_Monitor('status'))
def Plug_and_Play_Software_Device_Enumerator(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ROOT\\SYSTEM\\0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Plug_and_Play_Software_Device_Enumerator('status'))
def Motherboard_resources(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ACPI\\PNP0C02\\3&2411E6FE&0')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Motherboard_resources('status'))
def Remote_Desktop_Device_Redirector_Bus(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'ROOT\\RDPBUS\\0000')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(Remote_Desktop_Device_Redirector_Bus('status'))
def PCI_standard_host_CPU_bridge(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_156B&SUBSYS_00000000&REV_00\\3&2411E6FE&0&10')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(PCI_standard_host_CPU_bridge('status'))
def PCI_standard_host_CPU_bridge(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'PCI\\VEN_1022&DEV_1584&SUBSYS_00000000&REV_00\\3&2411E6FE&0&C4')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(PCI_standard_host_CPU_bridge('status'))
def High_Definition_Audio_Device(arg='status'):
   print('Argument: '+str(arg))
   if arg in ['status', 'find'] or is_admin(): 
      return subprocess.check_output('devcon '+arg+  ' @"'u'HDAUDIO\\FUNC_01&VEN_1002&DEV_AA01&SUBSYS_00AA0100&REV_1005\\4&27ECBAF2&0&0001')
   else:
      if (ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(caller_script), None, 0)) !=42:
         print('Authentication: failed')
      else:
         print('Authentication: successful')
      print('')
   time.sleep(2)
   return(High_Definition_Audio_Device('status'))
try:
    os.remove('devcon_win_copy.py')
except WindowsError:
    pass