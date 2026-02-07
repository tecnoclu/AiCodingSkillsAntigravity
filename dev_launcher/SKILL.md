---
name: Dev Launcher
description: Analyzes the project and generates a tailored 'run-dev.bat' script with a DOS-like interactive menu to launch development servers.
---

# Dev Launcher Instructions

Use this skill to create a `run-dev.bat` that provides a "classic" interactive menu for launching various parts of the development environment.

## Workflow

1.  **Analyze Project & Identify Modes**:
    *   Scan `package.json`, `composer.json`, `requirements.txt`, etc.
    *   Identify all distinct services (e.g., Laravel Backend, Vite Frontend, queue worker, DB container).
    *   **Dependency Strategy**:
        *   **Frontend (Node/NPM)**: Always local (`node_modules`).
        *   **Backend (Python)**: **ALWAYS use a Virtual Environment (`venv`)**.
            *   Check if `venv` exists.
            *   If not, create it: `python -m venv venv`.
            *   Activate it before running commands: `call venv\Scripts\activate`.
    *   Define logical **Launch Modes**:
        *   **All**: Everything running together.
        *   **Frontend Only**: e.g., `npm run dev`.
        *   **Backend Only**: e.g., `venv\Scripts\activate && uvicorn main:app`.
        *   **Custom**: Any other relevant combination.

2.  **Generate Interactive `run-dev.bat`**:
    *   Create a batch script using `CHOICE` or `set /p` to create a retro DOS-style menu.
    *   **Style Requirements**: Use ASCII borders/headers.
    *   **Venv Helper**: Include a helper label `:check_venv` to auto-create venv if missing.

    ### Template Structure

    ```batch
    @echo off
    cls
    :menu
    cls
    echo ==================================================
    echo           DEV LAUNCHER :: [Project Name]
    echo ==================================================
    echo.
    echo   [1] Launch ALL (Frontend + Backend)
    echo   [2] Launch Backend Only (Laravel)
    echo   [3] Launch Frontend Only (Vite)
    echo   [4] Launch Queue Worker Only
    echo   [5] Exit
    echo.
    echo ==================================================
    set /p choice="Select an option: "

    if "%choice%"=="1" goto launch_all
    if "%choice%"=="2" goto launch_backend
    if "%choice%"=="3" goto launch_frontend
    if "%choice%"=="4" goto launch_queue
    if "%choice%"=="5" exit

    echo Invalid choice.
    pause
    goto menu

    :launch_all
    echo Launching ALL...
    :: Use 'start' for separate windows or 'concurrently' if available
    start "Backend" php artisan serve
    start "Frontend" npm run dev
    goto end

    :launch_backend
    echo Launching Backend...
    php artisan serve
    goto end

    :launch_frontend
    echo Launching Frontend...
    npm run dev
    goto end

    :launch_queue
    echo Launching Queue...
    php artisan queue:listen
    goto end

    :end
    ```

3.  **Command Execution Strategy**:
    *   For "All" or multi-process modes, prefer `npx concurrently` if installed, or use `start "Title" command` to open separate terminal windows.
    *   For single-process modes, run the command directly in the current window (blocking) so Ctrl+C works normally.

4.  **Verification**:
    *   Write the file to `run-dev.bat`.
    *   Tell the user: "I've created the launcher with a retro menu. Run `.\run-dev.bat` to try it."
