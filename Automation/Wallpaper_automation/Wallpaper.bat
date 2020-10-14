cd C:\Users\Sri\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets\
set _TMP=
for /f "delims=" %%a in ('dir /b %1') do set _TMP=%%a
pause
IF {%_TMP%}=={} (set _empty=Empty) 
ELSE (
ren *.* *.jpg
copy *.* E:\Wallpaper
)
goto start

:start
start /k conda activate base & C:/Users/Sri/Anaconda3/python.exe "E:\py projects\imageInfo.py"
exit



