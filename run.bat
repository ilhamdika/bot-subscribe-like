@echo off
:menu
echo Pilih opsi:
echo 1. Like subscribe watch
echo 2. Like
echo 3. Watch
echo 4. Subscribe
set /p choice=Masukkan pilihan Anda (1/2/3/4):

if "%choice%"=="1" (
    python like_subscribe_watch.py
) else if "%choice%"=="2" (
    python like.py
) else if "%choice%"=="3" (
    python watch.py
) else if "%choice%"=="4" (
    python subscribe.py
) else (
    echo Pilihan tidak valid, coba lagi.
    goto menu
)
pause
