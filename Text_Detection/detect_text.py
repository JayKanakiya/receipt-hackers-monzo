#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 11:51:20 2019

@author: phypoh
"""
from google.cloud import vision
import argparse
import io

def detect_text(content):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    output = []

    for text in texts:
        print('\n"{}"'.format(text.description))
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        print('bounds: {}'.format(','.join(vertices)))

        output.append([text.description,vertices])
    
    return output

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('detect_file', help='The image for text detection.')
    args = parser.parse_args()

    path = args.detect_file

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    detect_text(content)
    