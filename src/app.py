from __future__ import annotations
import random
from typing import List
import pyttsx3


PHRASES: List[str] = [
    "Happy holidays! May your inbox be light and your coffee strong.",
    "Season's greetings! Wishing you smooth meetings and even smoother days.",
    "Warm holiday vibes! Hope you get a break longer than your last email thread.",
    "Happy holidays! May all your projects wrap up neatly… unlike gift wrapping.",
    "Season's greetings! Remember: snacks in the break room count as self-care.",
    "Sending cheer! May your week be productive but not too productive.",
    "Happy holidays! You deserve a moment of calm… right after this button press.",
    "Cheers to the season! May your tasks stay manageable and your Wi-Fi stay strong.",
    "Wishing you good vibes and low-stress days this holiday season.",
    "Happy holidays! Hope your day is as bright as the office fluorescent lights… but nicer.",
]


class Speaker:

    def __init__(self) -> None:
        self._engine = pyttsx3.init()
        rate = self._engine.getProperty("rate")
        self._engine.setProperty("rate", int(rate * 0.75))  # 25% slower

    def say_random_phrase(self) -> None:
        phrase = random.choice(PHRASES)
        print(f"[TTS] {phrase}")
        self._engine.say(phrase)
        self._engine.runAndWait()
