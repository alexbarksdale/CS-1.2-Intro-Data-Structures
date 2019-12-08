import re


def read_file(source):
    with open(source, 'r') as file:
        source_file = file.read().lower()
        filtered_file = re.sub(r'[^a-zA-Z\s]', '', source_file)

        return filtered_file.replace('\n', ' ')
