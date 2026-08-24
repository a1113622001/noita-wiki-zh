@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

:: 设置 UTF-8 编码防止 Windows 控制台乱码
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1

:: 定位项目根目录与 Python 脚本路径
set "SCRIPT_DIR=%~dp0"
set "MCP_SCRIPT=%SCRIPT_DIR%rag\mcp_server.py"

:: 优先检测 Python 环境
if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python311\python.exe"
) else if exist "%LOCALAPPDATA%\Programs\Python311\python.exe" (
    set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Python311\python.exe"
) else (
    where python >nul 2>&1
    if !errorlevel! equ 0 (
        set "PYTHON_EXE=python"
    ) else (
        where py >nul 2>&1
        if !errorlevel! equ 0 (
            set "PYTHON_EXE=py"
        ) else (
            echo [错误] 未找到 Python 运行环境，请先安装 Python 3.10+。 >&2
            exit /b 1
        )
    )
)

:: 启动 MCP Server (stdio 模式)
"%PYTHON_EXE%" "%MCP_SCRIPT%" %*
