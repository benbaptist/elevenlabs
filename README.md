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
import elevenlabs

# create a client
client = elevenlabs.Client(api_key='your_api_key')

# retrieve data
data = client.get('/data')
print(data)
```

For more advanced usage, refer to the (currently non-existant!) documentation and the API reference.

See https://api.elevenlabs.io/docs for details on the official documentation.
