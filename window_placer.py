import pygetwindow as gw
import re


def resize_discord_chrome():
    # Windows that will be placed on second monitor
    target_windows = []

    windows = gw.getAllTitles()

    for window_name in windows:
        if "Google Chrome" in window_name:
            target_windows.append(window_name)
            current_window = gw.getWindowsWithTitle(window_name)[0]
            current_window.resizeTo(1096, 950)
            current_window.moveTo(-1088, -383)
        elif "Discord" in window_name:
            target_windows.append(window_name)
            current_window = gw.getWindowsWithTitle(window_name)[0]
            current_window.resizeTo(1080, 850)
            current_window.moveTo(-1080, 559)

    print(target_windows)

if __name__ == "__main__":
    print("Hello World")
    resize_discord_chrome()