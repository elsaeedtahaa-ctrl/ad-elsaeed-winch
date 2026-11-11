@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul
color 0B
title UPLOAD EL SAEED WINCH TO GITHUB

cd /d "%~dp0"

echo ===============================================================================
echo               رفع موقع ونش السعيد إلى GITHUB بنجاح 100%%
echo   المستودع: https://github.com/elsaeedtahaa-ctrl/ad-elsaeed-winch.git
echo   الحساب: elsaeedtahaa-ctrl
echo ===============================================================================
echo.

echo [1/3] فحص حالة الملفات...
git status
echo.

echo [2/3] جاري رفع التحديثات إلى GitHub (الصور، المقالات، صفحات الفيديو، التصميم)...
git push origin main

if %errorlevel% equ 0 (
    echo.
    echo ===============================================================================
    echo [3/3] تم رفع الموقع بنجاح 100%% إلى GitHub!
    echo       رابط الموقع المباشر: https://elsaeedwinch.com/
    echo ===============================================================================
    goto :end
)

echo.
echo ===============================================================================
echo   تنبيه: لم يتم الرفع تلقائياً بسبب تسجيل الدخول على GitHub (elsaeedtahaa-ctrl)
echo ===============================================================================
echo.
echo إذا كان لديك GitHub Personal Access Token (PAT):
echo انسخه والصقه هنا ثم اضغط Enter:
echo.
set /p TOKEN="GitHub Token (اضغط كليك يمين للصق): "

if not "!TOKEN!"=="" (
    echo.
    echo جاري الرفع باستخدام التوكن...
    git push https://elsaeedtahaa-ctrl:!TOKEN!@github.com/elsaeedtahaa-ctrl/ad-elsaeed-winch.git main
    if !errorlevel! equ 0 (
        echo.
        echo ===============================================================================
        echo [3/3] تم رفع الموقع بنجاح 100%% إلى GitHub!
        echo ===============================================================================
        goto :end
    )
)

:end
echo.
pause
