# elevenlabs #
[![PyPI - Downloads](https://img.shields.io/pypi/dm/elevenlabs?style=for-the-badge)](https://pypi.org/project/elevenlabs/)
![PyPI - Status](https://img.shields.io/pypi/status/elevenlabs?style=for-the-badge)
[![PyPI](https://img.shields.io/pypi/v/elevenlabs?style=for-the-badge)](https://pypi.org/project/elevenlabs/)

NOTE: The official elevenlabs library is now available! Check it out [here at this link](https://github.com/elevenlabs/elevenlabs-python). The PyPi package `elevenlabs` will now point to their official library moving forward. Just in case you need this library still, I went ahead and re-uploaded it to [benbaptist-elevenlabs](https://pypi.org/project/benbaptist-elevenlabs/0.1.1/).

elevenlabs is an unofficial Python library that provides an easy-to-use interface for elevenlabs.io' API. With this library, you can easily integrate with the API to generate voices.

# Installation #
To install this unofficial elevenlabs library, run:

```
pip install --upgrade benbaptist-elevenlabs
```

This library requires no special dependencies, and is written in pure Python.

# Basic Usage #
Here's an example of how you can use elevenlabs to retrieve data from the API:

```
from elevenlabs import ElevenLabs

eleven = ElevenLabs(api_key)

# Get a Voice object, by name or UUID
voice = eleven.voices["Arnold"]

# Generate the TTS
audio = voice.generate("Hey buddy! It's a beautiful day.")

# Save the TTS to a file named 'my_first_tts' in the working directory
audio.save("my_first_tts")
```

See example.py for more. For more advanced usage, refer to the (currently non-existent!) documentation and the API reference.

See [the official ElevenLabs documentation](https://api.elevenlabs.io/docs) for more information.

# Real World Example #
I'm currently using this library to produce fully-automated weather reports on my radio station, [BMIX94](https://listen.bmix.live). For a sample of how it sounds, [here's link to the latest weather report](https://listen.bmix.live/streams/benmixer/weather.wav) that will actually be broadcasting at various times throughout the day. That link is always pointing to the most recent weather report generated.
