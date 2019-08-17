from UserInterface import get_num_faces, get_name
from Training import train
from Generation import generate
from Testing import test

import numpy as np

MAX_IMAGES = 500
labels = []
faces = []
names = []

# Face Generation
get_num_faces()
file = open('data.txt', 'r+')
N = int(file.readline())
for i in range(N):
    get_name()
    names.append(file.readline())
    faces.extend(generate(MAX_IMAGES // N))
    labels.extend([i for x in range(MAX_IMAGES // N)])

# Training
model = train(np.array(faces), np.array(labels))

# Testing
test(model, names)
file.close()
