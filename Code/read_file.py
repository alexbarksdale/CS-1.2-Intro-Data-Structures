# TODO: Add cleanup text


def read_file(source):
    with open(source, 'r') as file:
        source_file = file.read().split()

        return source_file
