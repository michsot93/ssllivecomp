from .capture import load_tcp_stream
from .framing import split_frames
from .strings import extract_strings


class Explorer:

    def open(self, filename):

        tcp = load_tcp_stream(filename)

        frames = split_frames(tcp)

        for frame in frames:

            frame["strings"] = extract_strings(
                frame["payload"]
            )

        return frames
