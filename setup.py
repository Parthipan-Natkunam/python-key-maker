import sys
from cx_Freeze import setup,Executable
base=None
if sys.platform == 'win32': base = 'Win32GUI'
opts={'include_files':['logo.gif','favicon.ico'],'includes':['re']}
setup(name = 'Key Maker', version='1.0', description = "Key Maker",publisher='Parthipan Natkunam',author='Parthipan Natkunam',options={'build_exe':opts},executables=[Executable('KM.py',base=base)])
