import pyautogui

# Set a one-second pause after each function call
pyautogui.PAUSE = 1
# Enable the fail-safe feature
pyautogui.FAILSAFE = True

width, height = pyautogui.size()

while (1 == 1):
        pyautogui.moveTo(100, 100, duration = 1)
        pyautogui.moveTo(200, 100, duration = 1)
        pyautogui.moveTo(200, 200, duration = 1)
        pyautogui.moveTo(100, 200, duration = 1)