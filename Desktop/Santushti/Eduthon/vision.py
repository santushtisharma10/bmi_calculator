import os, io
from google.cloud import vision
from google.cloud.vision import types

print("module imported")

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'My First Project-4952a6844337.json'

client = vision.ImageAnnotatorClient()

File_Path = r"gina-berreca-1561481686.png"

with io.open(File_Path, 'rb') as img:
    content = img.read()

image = vision.types.Image(content= content)

response = client.text_detection(image= image)
print("Success")