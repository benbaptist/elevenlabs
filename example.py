from elevenlabs import ElevenLabs

from config import api_key

import os

"""
This example does not work without creating a config.py
containing the variable 'api_key', which can be retrieved on
the 'Profile' tab on elevenlabs.io.

See https://api.elevenlabs.io/docs#/ for details.
"""

if __name__ == "__main__":
    el = ElevenLabs(
        api_key
    )

    if not os.path.exists("output"):
        os.mkdir("output")

    print("Fetching the first available voice...")
    voice = el.voices.list[0]

    print("Generating some text...")

    voice \
        .generate("Hey there. My name is Python and I'm a great little snake.") \
        .save("output/test")
