import pygetwindow as gw


def resize_discord_chrome():
    # Windows that will be placed on second monitor
    # Get all open windows
    target_windows = []
    windows = gw.getAllTitles()

    for window_name in windows:
    #   if window is Google Chrome or Discord
        if "Google Chrome" in window_name:
            target_windows.append(window_name)
            current_window = gw.getWindowsWithTitle(window_name)[0]
#           If window is on second screen
#           If window is not maximized
            if (current_window.top < 0 and current_window.left < 0):
                if current_window.isMaximized == True:
                    current_window.minimize()

                current_window.resizeTo(1096, 950)
                current_window.moveTo(-1088, -383)

        elif "Discord" in window_name:
            target_windows.append(window_name)
            current_window = gw.getWindowsWithTitle(window_name)[0]
            current_window.resizeTo(1080, 850)
            current_window.moveTo(-1080, 559)


if __name__ == "__main__":
    resize_discord_chrome()
