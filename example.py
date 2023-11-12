from elevenlabs import ElevenLabs

# Try to read the api_key from config.py
try:
    from config import api_key
except ImportError:
    api_key = None

import os
import time

import argparse
import sys

"""
This example does not work without creating a config.py
containing the variable 'api_key', which can be retrieved on
the 'Profile' tab on elevenlabs.io.

See https://api.elevenlabs.io/docs for details.
"""

if __name__ == "__main__":
    # Parse cmd arguments with argparse
    parser = argparse.ArgumentParser(
        prog = "elevenlabs example",
        description = "An example of the elevenlabs library")

    parser.add_argument("-o", "--output",
        help="Specify the output directory for the generated audio file",
        default="output")
    parser.add_argument("-t", "--text",
        help="Text to convert to speech")
    parser.add_argument("-v", "--voice",
        help="Specify the name or UUID of a voice on your ElevenLabs account")
    parser.add_argument("-l", "--voices",
        help="List all voices assocaited with your ElevenLabs account",
        action="store_true")
    parser.add_argument("-p", "--parameter",
        help="Change a voice parameter. Use the format setting=value",
        action="append")
    parser.add_argument("-k", "--api-key",
        help="Specify an API key to use with ElevenLabs",
        dest="api_key")

    parser.add_argument("-f", "--output-format",
        help="Output format from ElevenLabs",
        dest="output_format",
        default="mp3_44100_128")

    args = parser.parse_args()

    # If --api-key is specified, use this instead of relying on config.py
    if args.api_key:
        api_key = args.api_key

    # If no API key is specified or imported from config.py, fail
    if not api_key:
        print("Error: No API key was specified. Either use --api-key, or \
        create a file named 'config.py' and set the var api_key containing\
        the API key.")

        sys.exit(1)

    # Create an ElevenLabs instance
    elevenlabs = ElevenLabs(api_key)

    # If --voices is specified, list all the voices avaialbe
    if args.voices:
        print("Voices: ")
        for voice in elevenlabs.voices.list:
            print("- %s" % voice.name)

        sys.exit(0)

    # Create the output path, if it doesn't already exist
    if not os.path.exists(args.output):
        os.mkdir(args.output)

    # If --voice is specified, use that, or interactively ask for a voice
    if args.voice:
        try:
            voice = elevenlabs.voices[args.voice]
        except KeyError:
            print("Could not find voice '%s'" % args.voice)
            sys.exit(1)
    else:
        print("Fetching voices...")

        voice = None
        while not voice:
            for i, _voice in enumerate(elevenlabs.voices.list):
                print("[%s] %s" % (i, _voice.name))

            voice_identifier = input("Pick the voice you'd like: ")

            try:
                voice_identifier = int(voice_identifier)
            except ValueError:
                pass

            try:
                voice = elevenlabs.voices[voice_identifier]
            except IndexError:
                print("Invalid selection '%s'." % voice_identifier)

    # If --text is specified, use that, otherwise interactively ask for text
    if args.text:
        text = args.text
    else:
        text = input("Write some text for your voice to say: ")

    # Get the settings used for this voice
    voice_settings = voice.settings

    # If any --parameter arguments are specified, apply them
    if args.parameter:
        for parameter in args.parameter:
            name, val = parameter.split("=")
            name.lower()

            try:
                float(val)
            except ValueError:
                pass

            voice_settings[name] = val

    # Print out the settings to be used to generate this TTS
    for setting in voice_settings:
        value = voice_settings[setting]

        print("- %s = %s" % (setting, value))

    print("Generating TTS...")

    # Do the thing!
    voice \
        .generate(text, voice_settings=voice_settings, output_format=args.output_format) \
        .save("%s/%s_%s" % (args.output, voice.name, time.time()))
