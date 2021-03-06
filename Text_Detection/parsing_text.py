#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 11:51:20 2019

@author: phypoh
"""
from google.cloud import vision
import argparse
import io
import ast


def parse_text(text_list):

    information = {}

    merchant = text_list[0][0].split('\n', 1)[0]

    information['Merchant'] = merchant

    #print('Merchant: ', merchant)

    item_list = []

    for text in text_list:
        if check_if_price(text[0]):
            value = float(text[0])

        elif check_if_price(text[0][1:]):
            value = float(text[0][1:])

        else:
            continue

        #print(value)

        item = ""

        value_index = text_list.index(text)
        y_position = ast.literal_eval(text[1][0])[1]

        while value_index > 0:
            value_index -= 1
            previous_text = text_list[value_index]
            previous_y_position = ast.literal_eval(previous_text[1][0])[1]

            if previous_y_position < y_position + 10 and previous_y_position > y_position - 10:
                item = previous_text[0] + " " + item

        if value == 0 or item == "":
            continue
            
        item_list.append([item, value])


    #print(item_list)

    total = 0

    tax = 0

    to_remove = []

    for item in item_list:
        uppercase = item[0].upper()
        if "TOTAL" in uppercase:
            total = item[1]
            to_remove.append(item)

        elif "VAT" in uppercase or "TAX" in uppercase:
            tax = item[1]
            to_remove.append(item)

    for item in to_remove:
        item_list.remove(item)

    information['Item List'] = item_list

    information['Total'] = total

    information['Tax'] = tax

    return information


def check_if_price(text_input):
    try: 
        if text_input.isdigit():
            raise ValueError
        value = float(text_input)
        deci2 = str(value).split('.')
        if len(deci2[-1]) != 2 and len(deci2[-1]) != 1:
            raise ValueError
        return True

    except ValueError:
        return False

