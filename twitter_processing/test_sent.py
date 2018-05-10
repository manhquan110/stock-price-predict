import os
import csv
import numpy as np
from textblob import TextBlob
import re

date = []
sentiments = []
for i in range(2010, 2018):
    indir = 'C:\\Users\\IEUser\\PycharmProjects\\text_sentiment\\' + str(i)
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            with open(indir+'\\'+f) as fi:
                stock_list = []
                reader = csv.reader(fi)
                for row in reader:
                    stock_list.append(list(row))
# 'username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink'
                sentiment = []
                count = 1
                sent_temp = 0
                tweet_count = 0
                for i in stock_list[1:]:
                    count += 1
                    temp2 = ' '.join(i)
                    temp = temp2.split(';')
                    retweet = temp[2]
                    date.append(temp[1])
                    sent = TextBlob(re.sub(r'[^\x00-\x7f]', r'', temp2))
                    sent_score = sent.sentiment.polarity - sent.sentiment.subjectivity
                    sent_temp += sent_score
                    tweet_count += int(retweet)
                sentiment.append(sent_temp / float(count))
                sentiment.append(tweet_count)
                sentiments.append(sentiment)
final_list = np.asarray(sentiments)


def normalize_column(A, col):
    print(np.mean(A[:, col]))
    print(np.std(A[:, col]))
    A[:, col] = (A[:, col] - np.mean(A[:, col]))/np.std(A[:, col])
    print(np.mean(A[:, col]))
    print(np.std(A[:, col]))


normalize_column(final_list, 0)
final_list = final_list.tolist()
with open("final.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(final_list)
