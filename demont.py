import pandas
from textblob import TextBlob
pos_arr = []
neg_arr = []
neu_arr = []

positive = 0
neutral = 0
negative = 0

k = pandas.read_json("demonov.json")
for i in k["text"]:
    blob = TextBlob(i)
    polarity = blob.sentiment.polarity
    if polarity>0:
        positive+=1
    elif polarity==0:
        neutral+=1
    else:
        negative+=1

no_tweets = len(k["text"])

print (1.0*positive/no_tweets)*100, (1.0*negative/no_tweets)*100, (1.0*neutral/no_tweets)*100

pos_arr.append((1.0*positive/no_tweets)*100)
neg_arr.append((1.0*negative/no_tweets)*100)
neu_arr.append((1.0*neutral/no_tweets)*100)

positive = 0
neutral = 0
negative = 0

k = pandas.read_json("demodec.json")
for i in k["text"]:
    blob = TextBlob(i)
    polarity = blob.sentiment.polarity
    if polarity>0:
        positive+=1
    elif polarity==0:
        neutral+=1
    else:
        negative+=1

no_tweets = len(k["text"])

print (1.0*positive/no_tweets)*100, (1.0*negative/no_tweets)*100, (1.0*neutral/no_tweets)*100

pos_arr.append((1.0*positive/no_tweets)*100)
neg_arr.append((1.0*negative/no_tweets)*100)
neu_arr.append((1.0*neutral/no_tweets)*100)

positive = 0
neutral = 0
negative = 0

k = pandas.read_json("demojan.json")
for i in k["text"]:
    blob = TextBlob(i)
    polarity = blob.sentiment.polarity
    if polarity>0:
        positive+=1
    elif polarity==0:
        neutral+=1
    else:
        negative+=1

no_tweets = len(k["text"])

print (1.0*positive/no_tweets)*100, (1.0*negative/no_tweets)*100, (1.0*neutral/no_tweets)*100

pos_arr.append((1.0*positive/no_tweets)*100)
neg_arr.append((1.0*negative/no_tweets)*100)
neu_arr.append((1.0*neutral/no_tweets)*100)

positive = 0
neutral = 0
negative = 0

k = pandas.read_json("demofeb.json")
for i in k["text"]:
    blob = TextBlob(i)
    polarity = blob.sentiment.polarity
    if polarity>0:
        positive+=1
    elif polarity==0:
        neutral+=1
    else:
        negative+=1

no_tweets = len(k["text"])

print (1.0*positive/no_tweets)*100, (1.0*negative/no_tweets)*100, (1.0*neutral/no_tweets)*100

pos_arr.append((1.0*positive/no_tweets)*100)
neg_arr.append((1.0*negative/no_tweets)*100)
neu_arr.append((1.0*neutral/no_tweets)*100)

positive = 0
neutral = 0
negative = 0

k = pandas.read_json("demomar.json")
for i in k["text"]:
    blob = TextBlob(i)
    polarity = blob.sentiment.polarity
    if polarity>0:
        positive+=1
    elif polarity==0:
        neutral+=1
    else:
        negative+=1

no_tweets = len(k["text"])

print (1.0*positive/no_tweets)*100, (1.0*negative/no_tweets)*100, (1.0*neutral/no_tweets)*100

pos_arr.append((1.0*positive/no_tweets)*100)
neg_arr.append((1.0*negative/no_tweets)*100)
neu_arr.append((1.0*neutral/no_tweets)*100)

positive = 0
neutral = 0
negative = 0

k = pandas.read_json("demoapril.json")
for i in k["text"]:
    blob = TextBlob(i)
    polarity = blob.sentiment.polarity
    if polarity>0:
        positive+=1
    elif polarity==0:
        neutral+=1
    else:
        negative+=1

no_tweets = len(k["text"])

print (1.0*positive/no_tweets)*100, (1.0*negative/no_tweets)*100, (1.0*neutral/no_tweets)*100

pos_arr.append((1.0*positive/no_tweets)*100)
neg_arr.append((1.0*negative/no_tweets)*100)
neu_arr.append((1.0*neutral/no_tweets)*100)

positive = 0
neutral = 0
negative = 0

k = pandas.read_json("demomay.json")
for i in k["text"]:
    blob = TextBlob(i)
    polarity = blob.sentiment.polarity
    if polarity>0:
        positive+=1
    elif polarity==0:
        neutral+=1
    else:
        negative+=1

no_tweets = len(k["text"])

print (1.0*positive/no_tweets)*100, (1.0*negative/no_tweets)*100, (1.0*neutral/no_tweets)*100

pos_arr.append((1.0*positive/no_tweets)*100)
neg_arr.append((1.0*negative/no_tweets)*100)
neu_arr.append((1.0*neutral/no_tweets)*100)

positive = 0
neutral = 0
negative = 0

k = pandas.read_json("demojune.json")
for i in k["text"]:
    blob = TextBlob(i)
    polarity = blob.sentiment.polarity
    if polarity>0:
        positive+=1
    elif polarity==0:
        neutral+=1
    else:
        negative+=1

no_tweets = len(k["text"])

print (1.0*positive/no_tweets)*100, (1.0*negative/no_tweets)*100, (1.0*neutral/no_tweets)*100

pos_arr.append((1.0*positive/no_tweets)*100)
neg_arr.append((1.0*negative/no_tweets)*100)
neu_arr.append((1.0*neutral/no_tweets)*100)

positive = 0
neutral = 0
negative = 0

k = pandas.read_json("demojuly.json")
for i in k["text"]:
    blob = TextBlob(i)
    polarity = blob.sentiment.polarity
    if polarity>0:
        positive+=1
    elif polarity==0:
        neutral+=1
    else:
        negative+=1

no_tweets = len(k["text"])

print (1.0*positive/no_tweets)*100, (1.0*negative/no_tweets)*100, (1.0*neutral/no_tweets)*100

pos_arr.append((1.0*positive/no_tweets)*100)
neg_arr.append((1.0*negative/no_tweets)*100)
neu_arr.append((1.0*neutral/no_tweets)*100)


print pos_arr
print neg_arr
print neu_arr
