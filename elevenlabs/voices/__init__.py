from elevenlabs.endpoint import Endpoint
from elevenlabs.voices.voice import Voice

import time

class Voices(Endpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._voices = {}

    def _refresh_voice_list(self):
        r = self._request("GET", "voices/")
        payload = r.json()

        for voice_obj in payload["voices"]:
            voice_id = voice_obj["voice_id"]

            if voice_id not in self._voices:
                voice = Voice(self, voice_obj)

                self._voices[voice_id] = voice

    @property
    def list(self):
        # this is so ew, I'm sorry. I don't know why I am writing this code
        # the way I am. and yet, I continue to do it. even after apologizing.

        self._throttle(
            "voicelist",
            60,
            self._refresh_voice_list
        )

        return [self._voices[voice_id] for voice_id in self._voices]
