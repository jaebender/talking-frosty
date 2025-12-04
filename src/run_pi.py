from __future__ import annotations
from signal import pause
from gpiozero import Button
from app import Speaker

BUTTON_PIN = 17  # BCM pin number

def main() -> None:
    speaker = Speaker()
    button = Button(BUTTON_PIN, pull_up=True, bounce_time=0.1)

    def handle_press() -> None:
        speaker.say_random_phrase()

    button.when_pressed = handle_press

    print("Talking button on Raspberry Pi is ready. Press the button!")
    pause()

if __name__ == "__main__":
    main()
