from __future__ import annotations
import random
import subprocess
from app import PHRASES

# Words per minute; lower = slower.
SPEECH_RATE = 160

def main() -> None:
    print("Local test mode.")
    print("Press Enter to simulate a button press, or type 'q' and Enter to quit.")

    while True:
        user_input = input("> ").strip().lower()
        if user_input == "q":
            print("Goodbye!")
            break

        phrase = random.choice(PHRASES)
        print(f"[say @ {SPEECH_RATE} wpm] {phrase}")
        subprocess.run(["say", "-r", str(SPEECH_RATE), phrase])


if __name__ == "__main__":
    main()
