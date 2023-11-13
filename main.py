import pyautogui
import pygetwindow as gw
import requests
import time

# Set the pyautogui backend explicitly to use Xlib (which doesn't rely on DISPLAY)
pyautogui._pyautogui_x11 = None

# Replace with the URL of your Replit server
server_url = "https://robloxvminputting.tl6nh.repl.co/trigger-event"

def capture_and_send_screenshot():
    try:
        global server_url

        # Capture screenshot using pyautogui
        screenshot = pyautogui.screenshot()

        # Save the screenshot in PNG format
        screenshot_path = '/latest-screenshot/vm_screenshot.png'
        with open(screenshot_path, 'wb') as f:
            screenshot.save(f, format='PNG')

        # Send the screenshot path and request click position from the Replit server
        files = {'file': ('screenshot_path.txt', open(screenshot_path, 'rb'))}
        response = requests.post(server_url, files=files)

        if response.status_code == 200:
            print("Screenshot path sent successfully.")
        else:
            print("Failed to send screenshot path. Status code:", response.status_code)
            return

        # Request the click position from the Replit server
        click_response = requests.get("https://robloxvminputting.tl6nh.repl.co/get-click-position")
        click_position = click_response.json().get("click_position")

        if click_position:
            # Perform a click event at the specified position
            click_position = eval(click_position)  # Convert string to tuple
            print(f"Clicked at position: {click_position}")

    except Exception as e:
        print("Error:", str(e))

if __name__ == '__main__':
    # Capture and send a screenshot with a click event every 5 seconds (adjust as needed)
    while True:
        capture_and_send_screenshot()
        time.sleep(5)
