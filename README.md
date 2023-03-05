# elevenlabs #
elevenlabs is an unofficial Python library that provides an easy-to-use interface for elevenlabs.io' API. With this library, you can easily integrate with the API to generate voices.

# Installation #
To install elevenlabs, run:

```
pip install --upgrade elevenlabs
```

# Basic Usage #
Here's an example of how you can use elevenlabs to retrieve data from the API:

```
from elevenlabs import ElevenLabs

eleven = ElevenLabs(api_key)

voice = eleven.voices.list[0]

audio_file = voice.generate("Hey buddy!")
audio_file.save("my_first_tts")
```

See example.py for more. For more advanced usage, refer to the (currently non-existent!) documentation and the API reference.

See [the official ElevenLabs documentation](https://api.elevenlabs.io/docs) for more information.

# Real World Example #
I'm currently using this library to produce fully-automated weather reports on my radio station, [BMIX94](https://listen.bmix.live). For a sample of how it sounds, [here's link to the latest weather report](https://listen.bmix.live/streams/benmixer/weather.wav) that will actually be broadcasting at various times throughout the day. That link is always pointing to the most recent weather report generated.
