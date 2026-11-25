# pip install pillow numpy
from PIL import Image
import numpy as np

img = Image.open("download.jpg").convert("L")   # ubah ke grayscale
arr = np.array(img).astype(float)
h, w = arr.shape

frames = []
total_frames = 40
xs = np.arange(w)

for i in range(total_frames):
    phase = 2 * np.pi * i / total_frames
    # gelombang cahaya yang bergerak dari kiri ke kanan
    wave = 0.5 + 0.5 * np.sin(xs / 35.0 - phase)
    shimmer = arr * (0.35 + 0.65 * wave[None, :])
    frames.append(Image.fromarray(np.clip(shimmer, 0, 255).astype(np.uint8)))

frames[0].save(
    "animated.gif",
    save_all=True,
    append_images=frames[1:],
    duration=70,   # kecepatan per frame (ms), makin kecil makin cepat
    loop=0,        # 0 = loop terus-menerus
    optimize=True,
)
print("Selesai: animated.gif")
