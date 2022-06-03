import os
import json

def process_file(filename):
    # Using readlines()
    file1 = open('raw_tweets/' + filename, 'r')
    file2 = open('processed_tweets/' + filename, 'a')
    Lines = file1.readlines()
    
    count = 0
    # Strips the newline character
    file2.write("tweet\n")
    for line in Lines:
        count += 1
        obj = json.loads(line.strip())
        content = obj['content']
        content = content.replace(",", "")
        content = content.replace("\n", "")
        content = content.replace("\r", "")
        file2.write(content + '\n')
    
    file1.close()
    file2.close()

yourpath = './raw_tweets/'
for root, dirs, files in os.walk(yourpath, topdown=True):
    for name in files:
        process_file(name)