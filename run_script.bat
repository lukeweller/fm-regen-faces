@echo on
:start
py regen_faces.py
timeout /t 600 > NUL
goto start