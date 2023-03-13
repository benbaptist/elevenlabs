from elevenlabs.endpoint import Endpoint
from elevenlabs.voices.voice import Voice
from elevenlabs.voices.voices_iter import VoicesIter

import time

class Voices(Endpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._voices = {}

    def __iter__(self):
        """ Return a unique Iterator for iterating through all voices """
        return VoicesIter(self)

    def __getitem__(self, voice_identifier):
        """ Returns a Voice object by voice name, UUID, or index """

        # If int, return a voice by index on list
        if type(voice_identifier) == int:
            return self.list[voice_identifier]

        # Otherwise, iter through all voices and find first matching voice
        # by name or UUID.
        for voice in self.list:
            # Match by UUID
            if voice.id == voice_identifier:
                return voice

            # Match by name - non-case sensitive
            if voice.name.lower() == voice_identifier.lower():
                return voice

        raise KeyError(voice_identifier)

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
        self._throttle(
            "voicelist",
            60,
            self._refresh_voice_list
        )

        return [self._voices[voice_id] for voice_id in self._voices]
