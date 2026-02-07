@echo off
echo ===========================================
echo   A I   S K I L L S   D E P L O Y E R
echo ===========================================

echo.
echo 🔄 Updating README with latest skills...
python update_readme.py

if ERRORLEVEL 1 (
    echo ❌ Python script failed!
    pause
    exit /b
)

echo.
echo 📦 Staging changes...
git add .

echo.
echo ✍️  Committing (Automated)...
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set timestamp=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2% %datetime:~8,2%:%datetime:~10,2%

git commit -m "style: auto-update skills docs @ %timestamp%"

echo.
echo 🚀 Pushing to GitHub...
git push

if ERRORLEVEL 1 (
    echo ❌ Push failed! Check your connection or token.
    pause
    exit /b
)

echo.
echo ✅ Deployment Complete!
pause
