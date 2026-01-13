C:\Users\nastk>echo "Hello desktop" > "%HOMEPATH%\OneDrive\Desktop\desktopcmd.txt"

C:\Users\nastk>echo Hello desktop > "%USERPROFILE%\OneDrive\Desktop\desktopcmd.txt"

C:\Users\nastk>echo Hello desktop > "%USERPROFILE%\OneDrive\Desktop\desktopcmd.txt"

C:\Users\nastk>echo Hello Dow > "%USERPROFILE%\OneDrive\Downloads\downloadcmd.txt"
The system cannot find the path specified.

C:\Users\nastk>echo Hello Dow > "%USERPROFILE%\Downloads\downloadcmd.txt"

C:\Users\nastk>move "%USERPROFILE%\OneDrive\Desktop\desktopcmd.txt" > "%USERPROFILE%\Downloads
Access is denied.

C:\Users\nastk>move "%USERPROFILE%\OneDrive\Desktop\desktopcmd.txt" > "%USERPROFILE%\Downloads"
Access is denied.

C:\Users\nastk>move "%USERPROFILE%\OneDrive\Desktop\desktopcmd.txt" "%USERPROFILE%\Downloads"
        1 file(s) moved.

C:\Users\nastk>mkdir "%USERPROFILE%\Desktop\NetstatOutput"

C:\Users\nastk>netstat > "%USERPROFILE%\Desktop\NetstatOutput\netstat_output.txt"

C:\Users\nastk>dir "%USERPROFILE%\Desktop\NetstatOutput"
 Volume in drive C is OS
 Volume Serial Number is 304C-1DE6

 Directory of C:\Users\nastk\Desktop\NetstatOutput

24/10/2025  19:29    <DIR>          .
24/10/2025  19:29    <DIR>          ..
24/10/2025  19:30             6,706 netstat_output.txt
               1 File(s)          6,706 bytes
               2 Dir(s)  132,748,623,872 bytes free

C:\Users\nastk>echo @echo off > my_script.bat

C:\Users\nastk>echo echo Hello Dow ^> "%USERPROFILE%\Downloads\downloadcmd.txt" >> my_script.bat

C:\Users\nastk>echo echo Hello desktop ^> "%USERPROFILE%\Desktop\desktopcmd.txt" >> my_script.bat

C:\Users\nastk>dir "%USERPROFILE%\Downloads\downloadcmd.txt"
 Volume in drive C is OS
 Volume Serial Number is 304C-1DE6

 Directory of C:\Users\nastk\Downloads

24/10/2025  18:27                12 downloadcmd.txt
               1 File(s)             12 bytes
               0 Dir(s)  132,748,398,592 bytes free

C:\Users\nastk>echo @echo off > my_script.bat

C:\Users\nastk>
C:\Users\nastk>C:\Users\nastk>echo echo Hello Dow ^> "%USERPROFILE%\Downloads\downloadcmd.txt" >> my_script.bat
'C:\Users\nastk' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\nastk>
C:\Users\nastk>C:\Users\nastk>echo echo Hello desktop ^> "%USERPROFILE%\Desktop\desktopcmd.txt" >> my_script.bat
'C:\Users\nastk' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\nastk>echo @echo off > my_script.bat

C:\Users\nastk>echo echo Hello Dow ^> "%USERPROFILE%\Downloads\downloadcmd.txt" >> my_script.bat

C:\Users\nastk>echo echo Hello desktop ^> "%USERPROFILE%\Desktop\desktopcmd.txt" >> my_script.bat

C:\Users\nastk>dir my_script.bat
 Volume in drive C is OS
 Volume Serial Number is 304C-1DE6

 Directory of C:\Users\nastk

24/10/2025  19:44               137 my_script.bat
               1 File(s)            137 bytes
               0 Dir(s)  132,745,961,472 bytes free

C:\Users\nastk>my_script.bat

C:\Users\nastk>
