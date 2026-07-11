import json

from ssllive.explorer import Explorer

explorer = Explorer()

frames = explorer.open("capture7.pcapng")

print()

print("Frames:", len(frames))

print()

for frame in frames:

    print(
        f"Frame {frame['index']:3} "
        f"Offset {frame['offset']:8} "
        f"Length {frame['length']:4}"
    )

    for s in frame["strings"]:

        print("   ", s)

print()

with open("frames.json", "w") as f:

    json.dump(
        frames,
        f,
        default=lambda x: x.hex()
        if isinstance(x, bytes)
        else x,
        indent=2
    )
