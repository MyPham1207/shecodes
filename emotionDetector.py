import cv2
import os
import pygame
import numpy as np
import random

from deepface import DeepFace
from hsemotion.facial_emotions import HSEmotionRecognizer

face_img = cv2.imread('Images\DH.jpg', 1)
img = cv2.cvtColor(img, cv2.RGB2GRAY)
face = DeepFace.detectFace(face_img, target_size=(224,224), detector_backend='mtcnn')
face = (face * 255).astype(np.uint8)

model_name='enet_b0_8_best_afew'
fer = HSEmotionRecognizer(model_name=model_name, device='cpu')
emotion, _ = fer.predict_emotions(face, logits=True)
print(emotion)

positive = ['Happiness', 'Surprise']
negative = ['Anger', 'Contempt', 'Disgust', 'Fear']

positive_songs = os.listdir('Songs/Positive')
negative_songs = os.listdir('Songs/Negative')
neutral_songs = os.listdir('Songs/Neutral')

pygame.mixer.init()

def play(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def stop():
    pygame.mixer.music.stop()

if emotion in positive:
    play('Songs/Positive/' + random.choice(positive_songs))
elif emotion in negative:
    play('Songs/Negative/' + random.choice(negative_songs))
else:
    play('Songs/Neutral/' + random.choice(neutral_songs))

while True: 
    print("Press:", "'p' to pause", "'u' to unpause", "'s' to stop", sep='\n')
    query = input()
      
    if query == 'p':
        pause() 
    elif query == 'u':
        unpause()
    elif query == 's':
        stop()
        break
