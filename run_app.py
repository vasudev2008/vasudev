"""
Desktop Application Launcher for Locktite India Pvt Ltd.
Starts local server and opens a dedicated desktop window using Edge/Chrome app mode.
"""

import sys
import os
import time
import socket
import webbrowser
import subprocess
import threading
import uvicorn

APP_PORT = 8000
APP_HOST = "127.0.0.1"


def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((APP_HOST, port)) == 0


def find_browser_executable():
    """Finds Chrome or Edge executable on Windows for standalone --app window mode."""
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
    ]
    for p in candidates:
        if os.path.exists(p):
            return p
    return None


def launch_desktop_window(url: str):
    """Launches the app in a dedicated frameless/clean desktop window."""
    time.sleep(1.2)  # Wait for uvicorn to initialize
    browser_exe = find_browser_executable()
    if browser_exe:
        try:
            cmd = [
                browser_exe,
                f"--app={url}",
                "--window-size=1366,860",
                "--app-id=locktite_leave_management"
            ]
            subprocess.Popen(cmd)
            print(f"[OK] Launched standalone desktop window using {os.path.basename(browser_exe)}")
            return
        except Exception as e:
            print(f"[WARN] Failed to launch in app mode: {e}")

    # Fallback to default browser
    webbrowser.open(url)
    print(f"[OK] Opened in default system browser: {url}")


def main():
    global APP_PORT
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Find free port if 8000 is occupied
    while is_port_in_use(APP_PORT):
        APP_PORT += 1

    app_url = f"http://{APP_HOST}:{APP_PORT}"
    print("=" * 70)
    print(" LOCKTITE INDIA PVT LTD")
    print(" EMPLOYEE LEAVE MANAGEMENT SYSTEM")
    print("=" * 70)
    print(f" Starting offline local service on: {app_url}")
    print(" Press Ctrl+C in this console window to stop the service.")
    print("=" * 70)

    # Launch desktop window in separate thread
    threading.Thread(target=launch_desktop_window, args=(app_url,), daemon=True).start()

    # Run uvicorn server
    uvicorn.run("app.main:app", host=APP_HOST, port=APP_PORT, log_level="warning")


if __name__ == "__main__":
    main()
