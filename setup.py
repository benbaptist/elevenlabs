from setuptools import setup, find_packages

# Not gonna lie; I used ChatGPT to generate this setup.py. Nifty.

setup(
    name='elevenlabs',
    version='0.1',
    description='A Python library for integrating with ElevenLabs.io\'s API',
    author='Ben Baptist',
    author_email='me@benbaptist.com',
    url='https://github.com/benbaptist/elevenlabs',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
