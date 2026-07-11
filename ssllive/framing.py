import struct

MAGIC = b"\xef\xbc\x51\x00"


def split_frames(data: bytes):

    frames = []

    offset = 0
    index = 0

    while True:

        pos = data.find(MAGIC, offset)

        if pos == -1:
            break

        if pos + 8 > len(data):
            break

        length = struct.unpack("<I", data[pos + 4:pos + 8])[0]

        end = pos + 8 + length

        if end > len(data):
            break

        payload = data[pos + 8:end]

        frames.append(
            {
                "index": index,
                "offset": pos,
                "length": length,
                "payload": payload
            }
        )

        offset = end
        index += 1

    return frames
