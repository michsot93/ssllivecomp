import re

PRINTABLE = re.compile(rb"[\x20-\x7E]{4,}")


def extract_strings(data):

    strings = []

    for m in PRINTABLE.finditer(data):

        try:
            strings.append(
                m.group().decode("utf8")
            )

        except:

            pass

    return strings
