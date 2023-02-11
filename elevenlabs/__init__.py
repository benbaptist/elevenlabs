import requests
import time
import os

from elevenlabs.exceptions import *

from elevenlabs.voices import Voices

class ElevenLabs:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://api.elevenlabs.io/v1/"

        self.voices = Voices(self)

        self._throttles = {}

    def _throttle(self, id, freq, callback):
        if id not in self._throttles:
            self._throttles[id] = time.time()

            callback()
            return

        duration = time.time() - self._throttles[id]

        if duration < freq:
            callback()

    def _request(self, method, path, body=None):
        url = self.endpoint + path

        request = requests.request(
            method,
            url,
            json=body,
            headers={
                "xi-api-key": self.api_key
            }
        )

        if request.status_code != 200:
            # TODO: throw a proper exception here, add more specific handling

            print(request.content)
            
            raise Exception("%s" % (
                request.status_code
            ))

        return request
