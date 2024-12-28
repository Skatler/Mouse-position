from pyautogui import position
from time import sleep


def track_cursor():
    print("Press Ctrl+C to stop tracking.")
    last_position = None
    try:
        while True:
            x, y = position()
            if last_position != (x, y):
                print(f"Pointer is at ({x}, {y})", end="\r", flush=True)
                last_position = (x, y)
            sleep(0.1)
    except KeyboardInterrupt:
        print("\nTracking stopped.")


if __name__ == "__main__":
    track_cursor()
