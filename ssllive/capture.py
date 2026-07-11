import pyshark


def load_tcp_stream(filename):

    cap = pyshark.FileCapture(filename)

    stream = bytearray()

    for pkt in cap:

        try:

            if "TCP" not in pkt:
                continue

            payload = pkt.tcp.payload

            payload = bytes.fromhex(
                payload.replace(":", "")
            )

            stream.extend(payload)

        except:

            pass

    return bytes(stream)
