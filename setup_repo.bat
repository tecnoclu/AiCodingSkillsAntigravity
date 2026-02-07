@echo off
echo ===========================================
echo   A I   S K I L L S   S E T U P
echo ===========================================

echo.
echo 🔧 Initializing Git Repository...
git init

echo.
echo 🔗 Linking to GitHub Repo...
git remote add origin https://github.com/tecnoclu/AiCodingSkillsAntigravity.git

echo.
echo 🌿 Setting branch to 'main'...
git branch -M main

echo.
echo 📦 Adding all files...
git add .

echo.
echo ✍️  Initial Commit...
git commit -m "feat: Initial commit of Antigravity Skills Library"

echo.
echo 🚀 Pushing to GitHub...
git push -u origin main

if ERRORLEVEL 1 (
    echo.
    echo ❌ Push failed! Check if:
    echo 1. The repository URL is correct.
    echo 2. You have permission to push.
    echo 3. The repository is empty (if not, you might need to pull first).
    pause
    exit /b
)

echo.
echo ✅ Repository Setup Complete!
echo You can now use 'deploy.bat' for future updates.
pause
