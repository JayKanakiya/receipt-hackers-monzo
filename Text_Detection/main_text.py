import argparse
import numpy as np
from preprocessing import preprocess
from detect_text import detect_text
from parsing_text import parse_text
import cv2
import io

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('input_file', help='The image for text detection.')
	args = parser.parse_args()

	preprocessed_image = preprocess(args.input_file)

	cv2.imwrite("temp.jpg", preprocessed_image);

	#work on changing this later ^^^

	with io.open("temp.jpg", 'rb') as image_file:
		content = image_file.read()

	text_list = detect_text(content)

	if text_list == []:

		with io.open(args.input_file, 'rb') as image_file:
			content = image_file.read()

		text_list = detect_text(content)

	information = parse_text(text_list)

	print(information)




