# elevenlabs #
elevenlabs is a Python library that provides an easy-to-use interface for elevenlabs.io' API. With this library, you can easily integrate with the API to generate voices.

# Installation #
To install elevenlabs, simply run:

```
pip install elevenlabs
```

# Basic Usage #
Here's an example of how you can use elevenlabs to retrieve data from the API:

```
from elevenlabs import ElevenLabs

eleven = ElevenLabs(
    api_key
)

voice = eleven.voices.list[0]
audio_file = voice.generate("Hey buddy!")

```

See example.py for more. For more advanced usage, refer to the (currently non-existent!) documentation and the API reference.

See https://api.elevenlabs.io/docs for details on the official documentation.
