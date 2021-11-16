from PIL import Image
from pwn import xor

img1 = Image.open("lemur_ed66878c338e662d3473f0d98eedbd0d.png")
img2 = Image.open("flag_7ae18c704272532658c10b5faad06d74.png")

key_bytes = xor(img1.tobytes(), img2.tobytes())
key = Image.frombytes(img2.mode, img2.size, key_bytes)

key.save('flag.png')