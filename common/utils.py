from os.path import exists as file_exists

from magic import from_buffer, from_file


def get_mime_type_of_file(file: str | bytes):
    if isinstance(file, bytes):
        return from_buffer(file, mime=True)
    elif isinstance(file, str) and file_exists(file):
        return from_file(file, mime=True)
    else:
        raise ValueError("Invalid file type.")
