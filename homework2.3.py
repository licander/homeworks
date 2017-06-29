# -*- coding: utf-8 -*-
import chardet
import json

def read_from_file(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
        coding = chardet.detect(data)
        data = data.decode(coding['encoding'])         
        data = json.loads(data)
    return data['rss']['channel']['items']
        
def find_popular_words(list_of_data):
    dictionary = {}
    for new in list_of_data:
        print(new['title'])

data = read_from_file('newsafr.json')
find_popular_words(data)