from elevenlabs import ElevenLabs

from config import api_key

import os
import time

"""
This example does not work without creating a config.py
containing the variable 'api_key', which can be retrieved on
the 'Profile' tab on elevenlabs.io.

See https://api.elevenlabs.io/docs for details.
"""

if __name__ == "__main__":
    el = ElevenLabs(
        api_key
    )

    if not os.path.exists("output"):
        os.mkdir("output")

    print("Fetching voices...")

    voice = None
    while not voice:
        for i, _voice in enumerate(el.voices.list):
            print("[%s] %s" % (i, _voice.name))

        voice_index = input("Pick the voice you'd like: ")

        try:
            voice_index = int(voice_index)
            voice = el.voices.list[voice_index]
        except ValueError:
            print("Invalid selection '%s' - must be a number." % voice_index)
        except IndexError:
            print("Invalid selection '%s'." % voice_index)

    message = input("Write some text for your voice to say: ")

    # Print out the settings used to generate this voice
    voice_settings = voice.settings

    for setting in voice_settings:
        value = voice_settings[setting]

        print("- %s = %s" % (setting, value))

    print("Generating TTS...")

    voice \
        .generate(message, voice_settings=voice_settings) \
        .save("output/%s_%s" % (voice.name, time.time()))
