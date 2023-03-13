from elevenlabs.voices.audiofile import AudioFile

import requests

class Voice:
    def __init__(self, voices, obj):
        self._voices = voices
        self._obj = obj

        self._request = self._voices._request

    @property
    def id(self):
        """ Returns the UUID of this Voice """
        return self._obj["voice_id"]

    @property
    def name(self):
        """ Returns the name of this Voice """
        return self._obj["name"]

    @property
    def category(self):
        """ Returns the category of this Voice """
        return self._obj["category"]

    @property
    def preview_url(self):
        """ Returns a URL pointing to a sample audio file using this voice """
        return self._obj["preview_url"]

    @property
    def preview(self):
        """ Returns an AudioFile object containing a preview of this voice """
        request = requests.get(self.preview_url)

        return AudioFile(request)

    @property
    def settings(self):
        """ Returns all possible settings that you can configure with
        this voice """
        request = self._request(
            "GET",
            "voices/%s/settings" % self.id
        )

        return request.json()

    def generate(self, text, voice_settings=None):
        """ Generate a text-to-speech with the provided text and settings """
        if not voice_settings:
            voice_settings = self.settings

        request = self._request(
            "POST",
            "text-to-speech/%s" % self.id,
            {
                "text": text,
                "voice_settings": voice_settings
            }
        )

        return AudioFile(request)
