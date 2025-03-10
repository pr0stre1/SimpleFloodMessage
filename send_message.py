import pyautogui
import time
import keyboard
import clipboard

def main():
    # Wait a few seconds to give you time to focus on the correct window
    # time.sleep(5)

    # The message to send
    message = input("Message to send: ")

    if not message:
        message = 'Alo'


    # Number of times to send the message
    # count = 10
    
    try:
        delay = float(input("Seconds between messages: "))
    except ValueError:
        delay = float(0.5)

    print("\n3 seconds before start..\n")
    time.sleep(5)

    # for _ in range(count):
    while True:
        if keyboard.is_pressed("esc"):
            print("Quiting..")
            break
	
        clipboard.copy(message)  # Copy Message to clipboard
        pyautogui.hotkey('ctrl', 'v')  # Insert message in window
        # pyautogui.typewrite(message)  # Types the message
        pyautogui.press("enter")  # Presses the Enter key
        time.sleep(delay)  # Optional: Wait a little between each message

if __name__ == '__main__':
    main()
