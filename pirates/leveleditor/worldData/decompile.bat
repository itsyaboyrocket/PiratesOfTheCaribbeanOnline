@echo off
for /r %%f in (*.pyo) do (C:/pythons/Python2715/Scripts/uncompyle6.exe -o "%%~df%%~pf%%~nf.py" "%%~df%%~pf%%~nf.pyo")
pause