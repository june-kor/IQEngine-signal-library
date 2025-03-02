# Copyright (c) 2022 Microsoft Corporation
# Copyright (c) 2023 Marc Lichtman
# Licensed under the MIT License

import io
import json
import os

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

num_bytes = 1000000
offset = 0
fftSize = 1024

# Allow to work on linux as well
if (os.name == "posix"):
    sep = "/"
else:
    sep = "\\"


def spectro_maker(directory, basename):
    metaname = basename + ".sigmf-meta"
    dataname = basename + ".sigmf-data"
    metaFile = directory + sep + metaname
    dataFile = directory + sep + dataname

    if (not os.path.exists(metaFile)) or (not os.path.exists(dataFile)):
        # print("Either meta or data file does not exist")
        return

    print("Creating png for", directory, basename)

    with open(metaFile, "r") as f:
        meta_data = json.loads(f.read())
    with open(dataFile, "rb") as f:
        bytes = f.read()
    meta_data_global = meta_data.get("global", {})
    datatype = meta_data_global.get("core:datatype", "cf32_le")
    sample_rate = float(meta_data_global.get("core:sample_rate", 0)) / 1e6  # MHz
    center_freq = (
        float(meta_data.get("captures", [])[0].get("core:frequency", 0)) / 1e6
    )  # MHz

    if datatype == "cf32_le":
        samples = np.frombuffer(bytes, dtype=np.complex64)
    elif datatype == "rf32_le" or datatype == "f32_le" or datatype == "f32":
        samples = np.frombuffer(bytes, dtype=np.float32)
    elif datatype == "ci16_le":
        samples = np.frombuffer(bytes, dtype=np.int16)
        samples = samples[::2] + 1j * samples[1::2]
    elif datatype == "ri16_le" or datatype == "i16_le":
        samples = np.frombuffer(bytes, dtype=np.int16)
    elif datatype == "ci8_le" or datatype == "ci8":
        samples = np.frombuffer(bytes, dtype=np.int8)
        samples = samples[::2] + 1j * samples[1::2]
    elif datatype == "ri8_le" or datatype == "i8_le" or datatype == "i8":
        samples = np.frombuffer(bytes, dtype=np.int8)
    else:
        print("Datatype not implemented")
        samples = np.zeros(1024)

    # Generate spectrogram
    num_rows = int(np.floor(len(samples) / fftSize))
    spectrogram = np.zeros((num_rows, fftSize))
    for i in range(num_rows):
        spectrogram[i, :] = np.log10(
            np.abs(
                np.fft.fftshift(np.fft.fft(samples[i * fftSize: (i + 1) * fftSize]))
            )
            ** 2
        )

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(
        spectrogram,
        aspect="auto",
        extent=[
            sample_rate / -2 + center_freq,
            sample_rate / 2 + center_freq,
            0,
            len(samples) / sample_rate,
        ],
    )
    plt.axis("off")
    plt.grid(False)
    img_buf = io.BytesIO()
    plt.savefig(img_buf, bbox_inches="tight", pad_inches=0)
    img_buf.seek(0)
    im = Image.open(img_buf)

    img_byte_arr = io.BytesIO()
    im.convert("RGB").save(directory + sep + basename + '.jpg', quality=95, optimize=True) # save image as jpg with options
    output = f"{basename}.png"
    im.save(directory + sep + output)
    # print("New image saved")

    # Cleanup
    im.close()
    del bytes
    del spectrogram
    del img_buf
    del img_byte_arr


def file_parsing(dir, filename):
    extension = filename.split(".")[1]
    basename = filename.split(".")[0]
    if (extension != "sigmf-meta") and (extension != "sigmf-data"):
        # print("extension not correct")
        return
    elif extension == "sigmf-meta":
        spectro_maker(dir, basename)


def sub_dir_check(directory):
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # print(f)
        if os.path.isdir(f):
            sub_dir_check(directory + sep + filename)
        elif os.path.isfile(f):
            file_parsing(directory, filename)
        else:
            return


directory = input("Enter your desired directory: ")
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isdir(f):
        sub_dir_check(directory + sep + filename)
    else:
        file_parsing(directory, filename)
