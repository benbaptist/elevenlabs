from tempfile import SpooledTemporaryFile

import mimetypes

class AudioFile:
    def __init__(self, request):
        self._request = request

        self._file = SpooledTemporaryFile()
        self._file.write(request.content)

    def save(self, filename):
        """ Saves the resulting audio file to *filename*, with the
        appropriate file extension automatically appended to the end of
        the path. Returns the actual filename & path. """

        content_type = self._request.headers["content-type"]
        extension = mimetypes.guess_extension(content_type)

        filename = "%s%s" % (filename, extension)

        self._file.seek(0)

        with open(filename, "wb") as f:
            f.write(
                self._file.read()
            )

        return filename
