import json

# Using readlines()
file1 = open('data_tweets/51-themarksman.txt', 'r')
Lines = file1.readlines()
  
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    obj = json.loads(line.strip())
    print('line' + str(count) + ':')
    print(obj['content'])