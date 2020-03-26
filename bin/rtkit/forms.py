import mimetypes
import os
import re
import urllib

CRLF = '\r\n'
BOUNDARY = 'xXXxXXyYYzzz'


class MultipartForm(object):
    """Represents an encoded Form"""
    def __init__(self, params, boundary):
        self.boundary = boundary
        self.tboundary = "--%s--%s" % (boundary, CRLF)
        self.boundaries = []
        self._clen = None

        if hasattr(params, 'items'):
            params = params.items()

        for param in params:
            name, value = param
            if hasattr(value, "read"):
                fname = getattr(value, 'name')
                if fname is not None:
                    filetype = ';'.join(filter(None, mimetypes.guess_type(fname)))
                else:
                    filetype = None
                if not isinstance(value, file) and self._clen is None:
                    value = value.read()

                boundary = BoundaryItem(name, value, fname, filetype)
            else:
                boundary = BoundaryItem(name, value)
            self.boundaries.append(boundary)

    def get_size(self):
        if self._clen is None:
            self._clen = 0
            for boundary in self.boundaries:
                self._clen += boundary.size
                self._clen += len(boundary.encode_hdr(self.boundary))
                self._clen += len(CRLF)
            self._clen += len(self.tboundary)
        return int(self._clen)

    def __iter__(self):
        for boundary in self.boundaries:
            for block in boundary.iter_encode(self.boundary):
                yield block
        yield self.tboundary


class BoundaryItem(object):
    def __init__(self, name, value, fname=None, filetype=None, filesize=None):
        self.name = url_quote(name)
        if value is not None and not hasattr(value, 'read'):
            value = self.encode_unreadable_value(value)
            self.size = len(value)
        self.value = value
        if fname is not None:
            if isinstance(fname, unicode):
                fname = fname.encode("utf-8").encode("string_escape").replace('"', '\\"')
            else:
                fname = fname.encode("string_escape").replace('"', '\\"')
        self.fname = fname
        if filetype is not None:
            filetype = to_bytestring(filetype)
        self.filetype = filetype

        if isinstance(value, file) and filesize is None:
            try:
                value.flush()
            except IOError:
                pass
            self.size = int(os.fstat(value.fileno())[6])

        self._encoded_hdr = None
        self._encoded_bdr = None

    def encode_hdr(self, boundary):
        """:return: The header of the encoding of this parameter"""
        if not self._encoded_hdr or self._encoded_bdr != boundary:
            boundary = url_quote(boundary)
            self._encoded_bdr = boundary
            headers = ["--%s" % boundary]
            if self.fname:
                disposition = 'form-data; name="%s"; filename="%s"' % (
                    self.name,
                    self.fname,
                )
            else:
                disposition = 'form-data; name="%s"' % self.name
            headers.append("Content-Disposition: %s" % disposition)
            if self.filetype:
                filetype = self.filetype
            else:
                filetype = "text/plain; charset=utf-8"
            headers.append("Content-Type: %s" % filetype)
            headers.append("Content-Length: %i" % self.size)
            headers.append("")
            headers.append("")
            self._encoded_hdr = CRLF.join(headers)
        return self._encoded_hdr

    def encode(self, boundary):
        """ :returns: A string encoding of this parameter. """
        value = self.value
        if re.search("^--%s$" % re.escape(boundary), value, re.M):
            raise ValueError("boundary found in encoded string")

        return "%s%s%s" % (self.encode_hdr(boundary), value, CRLF)

    def iter_encode(self, boundary, blocksize=16384):
        if not hasattr(self.value, "read"):
            yield self.encode(boundary)
        else:
            yield self.encode_hdr(boundary)
            while True:
                block = self.value.read(blocksize)
                if not block:
                    yield CRLF
                    return
                yield block

    def encode_unreadable_value(self, value):
        if self.name == 'content':
            return _content_encode(value)
        else:
            return url_quote(value)


def encode(value, headers):
    if len(value) == 1 and 'content' in value:
        value = 'content={0}'.format(_content_encode(value['content'], quote=True))
        headers.setdefault('Content-Type', 'application/x-www-form-urlencoded; charset=utf-8')
    else:
        mf = MultipartForm(value, BOUNDARY)
        value = ''.join(list(mf))
        headers['Content-Type'] = "multipart/form-data; boundary=%s" % BOUNDARY
        headers['Content-Length'] = str(mf.get_size())
    return value


def _content_encode(value, quote=False):
    r"""
    >>> _content_encode({
    ...     'Action' : 'comment',
    ...     'Text' : 'Comment\nwith\nseveral\nlines',
    ... }, quote=True)
    'Action: comment\nText: Comment%0A+with%0A+several%0A+lines'
    >>> _content_encode({
    ...     'Action' : 'comment',
    ...     'Text' : 'Comment\nwith\nseveral\nlines',
    ... })
    'Action: comment\nText: Comment\n with\n several\n lines'
    """
    if 'Text' in value:
        value['Text'] = '\n '.join(value['Text'].splitlines())
        if quote:
            value['Text'] = url_quote(value['Text'])
    return '\n'.join(['{0}: {1}'.format(k, v) for k, v in value.iteritems()])


def url_quote(s, charset='utf-8', safe='/:'):
    """URL encode a single string with a given encoding."""
    if isinstance(s, unicode):
        s = s.encode(charset)
    elif not isinstance(s, str):
        s = str(s)
    return urllib.quote_plus(s, safe=safe)


def to_bytestring(s):
    if not isinstance(s, basestring):
        raise TypeError("value should be a str or unicode")

    if isinstance(s, unicode):
        return s.encode('utf-8')
    return s
