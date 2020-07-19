from PIL import Image
from numpy import array
# Open the image form working directory
image = Image.open(r"E:\Personal and Games\Personal\Vijay\YOUTUBE\Research\code\example.jpg")
# summarize some details about the image
print(image.format)
print(image.size)
print(image.mode)
# convert image to numpy array
data = array(Image.open("E:\Personal and Games\Personal\Vijay\YOUTUBE\Research\code\colorfulBird.jpg"))

for i in range(len(data)):
    for j in range(len(data[i])):
        r = int(data[i][j][0])
        g = int(data[i][j][1])
        b = int(data[i][j][2])
        avg = round((r + g + b) / 3)
        data[i][j][0] = avg
        data[i][j][1] = avg
        data[i][j][2] = avg
img = Image.fromarray(data, 'RGB')
img.save('my1.png')
img.show()