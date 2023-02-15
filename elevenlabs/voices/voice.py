from elevenlabs.voices.audiofile import AudioFile

import requests

class Voice:
    def __init__(self, voices, obj):
        self._voices = voices
        self._obj = obj

        self._request = self._voices._request

    @property
    def id(self):
        return self._obj["voice_id"]

    @property
    def name(self):
        return self._obj["name"]

    @property
    def category(self):
        return self._obj["category"]

    @property
    def preview_url(self):
        return self._obj["preview_url"]

    @property
    def preview(self):
        request = requests.get(self.preview_url)

        return AudioFile(request)

    def generate(self, text):
        request = self._request(
            "POST",
            "text-to-speech/%s" % self.id,
            {
                "text": text
            }
        )

        return AudioFile(request)
