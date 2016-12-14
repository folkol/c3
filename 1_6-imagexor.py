from PIL import Image
import numpy

# imarray = numpy.ones((600, 600, 3), numpy.uint8) * 125
imarray = numpy.random.rand(600, 600, 3) * 100 + 155

keys = [0b10101010] * 150 + [0b01010101] * 150
orig = imarray.copy()

im = Image.fromarray(imarray.astype(numpy.uint8)).convert('L')
im.show()

n = 0
for it in numpy.nditer(imarray, op_flags=['readwrite']):
    it[...] = int(it) ^ keys[n % 300]
    n += 1

im = Image.fromarray(imarray.astype(numpy.uint8)).convert('L')
im.show()

difference = imarray - orig

im = Image.fromarray(difference.astype(numpy.uint8)).convert('L')
im.show()

n = 0
for it in numpy.nditer(imarray, op_flags=['readwrite']):
    it[...] = int(it) ^ keys[n % 300]
    n += 1

im = Image.fromarray(imarray.astype(numpy.uint8)).convert('L')
im.show()
