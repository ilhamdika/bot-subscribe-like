@echo off
color 0A

cls
echo ============================================
echo               Hallo
echo ============================================
echo.

:menu
echo Pilih opsi:
echo 1. Like, Subscribe, Watch
echo 2. Like
echo 3. Watch
echo 4. Subscribe
echo.

set /p choice=Masukkan pilihan sesuai dengan angka (1/2/3/4):

if "%choice%"=="1" (
    set script=like_subscribe_watch.py
) else if "%choice%"=="2" (
    set script=like.py
) else if "%choice%"=="3" (
    set script=watch.py
) else if "%choice%"=="4" (
    set script=subscribe.py
) else (
    echo.
    echo [ERROR] Pilihan tidak valid, coba lagi.
    echo.
    goto menu
)

:confirm
echo ============================================
echo Anda memilih untuk menjalankan %script%.
echo ============================================
echo Apakah Anda yakin? (y/n)
echo.

echo Jika ya isi(y) jika tidak isi(n)
set /p confirm=Masukkan pilihan (y/n):

if "%confirm%"=="y" (
    echo.
    echo Get data dulu ya ....
    python api.py
    
    echo.
    echo Menjalankan %script%...
    python %script%
    
    echo.
    echo Proses selesai.
    echo.
    exit
) else if "%confirm%"=="n" (
    echo.
    echo Anda membatalkan pilihan. Kembali ke menu...
    echo.
    cls
    goto menu
) else (
    echo.
    echo [ERROR] Pilihan tidak valid, coba lagi.
    echo.
    goto confirm
)
