import pyautogui
import requests
import time

# Replace with the URL of your Replit server
server_url = "https://your-replit-server-url/trigger-event"

def capture_and_send_screenshot():
    try:
        global server_url

        # Capture screenshot using pyautogui
        screenshot = pyautogui.screenshot()

        # Save the screenshot on the server
        screenshot_path = 'path/to/your/server/screenshotted/vm_screenshot.png'
        screenshot.save(screenshot_path)

        # Send the screenshot path and request click position from the Replit server
        files = {'file': ('screenshot_path.txt', screenshot_path)}
        response = requests.post(server_url, files=files)

        if response.status_code == 200:
            print("Screenshot path sent successfully.")
        else:
            print("Failed to send screenshot path. Status code:", response.status_code)
            return

        # Request the click position from the Replit server
        click_response = requests.get("https://your-replit-server-url/get-click-position")
        click_position = click_response.json().get("click_position")

        if click_position:
            # Perform a click event at the specified position
            click_position = eval(click_position)  # Convert string to tuple
            pyautogui.click(click_position)
            print(f"Clicked at position: {click_position}")

    except Exception as e:
        print("Error:", str(e))

if __name__ == '__main__':
    # Capture and send a screenshot with click event every 5 seconds (adjust as needed)
    while True:
        capture_and_send_screenshot()
        time.sleep(1)