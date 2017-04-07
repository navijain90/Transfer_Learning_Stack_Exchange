import numpy as np
import pandas as pd
from nltk.corpus import stopwords
import re
cachedStopWords = stopwords.words("english")

def readTestFile():
  file = './data/test.csv'
  data_frame = pd.read_csv(file, names=['id', 'title', 'content'])
  print('finished reading files ... ')
  data_frame['title'] = data_frame['title'].apply(lambda x : removestopword(x))
  data_frame['title'] = data_frame['title'].apply(lambda x : replace_special_character(x))
  data_frame['content'] = data_frame['content'].apply(lambda x: removestopword(x))
  data_frame['content'] = data_frame['content'].apply(lambda x: replace_special_character(x))
  print('finished cleaning...')
  return data_frame

def replace_special_character(document):
    result = re.sub('[^a-zA-Z\n\.]', ' ', document).replace(".", "")
    result = ' '.join(result.split())
    result = "".join(result.splitlines())
    result=re.sub(r'\b\w{1,3}\b', '', result)
    return result.strip()

def removestopword(document):
  text = ' '.join([word for word in document.lower().split() if word not in cachedStopWords])
  return text


def readTrain(file):
  data_frame = pd.read_csv(file, names = ['id','title','content','tags'])
  print('finished reading files ... ')

  data_frame['title'] = data_frame['title'].apply(lambda x : removestopword(x))
  data_frame['title'] = data_frame['title'].apply(lambda x : replace_special_character(x))

  data_frame['content'] = data_frame['content'].apply(lambda x: removestopword(x))
  data_frame['content'] = data_frame['content'].apply(lambda x: replace_special_character(x))

  print('finished cleaning...')
  return data_frame

def readTrainingDataSet():
  # files = ['./data/biology.csv','./data/cooking.csv','./data/crypto.csv','./data/diy.csv','./data/robotics.csv','./data/travel.csv']
  files = ['./data/biology.csv','./data/cooking.csv']
  train_data_frames = []
  for f in files:
    train_data_frames.append(readTrain(f))

  return pd.concat(train_data_frames)

def main():
  train_data_frames = readTrainingDataSet()

  count = 0
  for index, row in train_data_frames.iterrows():
    if (count == 3):
      break
    print(row['tags'])
    count += 1

  test = readTestFile()
  print('=========================TEST=========================')
  count = 0
  for index, row in test.iterrows():
    if (count == 3):
      break
    print(row['title'])
    count += 1


if __name__ == '__main__':
  main()