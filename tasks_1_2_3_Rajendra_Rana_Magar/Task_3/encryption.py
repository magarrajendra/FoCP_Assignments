import codecs


def rot13(text):
    """Encrypts the passwords"""
    return codecs.encode(text, 'rot_13')
