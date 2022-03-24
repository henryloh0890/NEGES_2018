import nltk
import io
import glob
import os
import codecs
import re
import unicodedata
import numpy as np
import pandas as pd
from nltk.tag.util import tuple2str


train_data = []
train_words = set()
train_tags  = set()

with io.open("neges_train_task2_inBIO.txt",encoding='utf-8') as f:
	for line in f:
		tagged_sent = []
		for t in line.split():
			if t[0] != "|":
				tagged_sent.append(nltk.tag.str2tuple(t,'|')) 
				
		train_data.append(tagged_sent)
#print(train_data)

for s in train_data:
	for w in s:
		train_words.add(w[0])
		train_tags.add(w[1])
		if w[1] is None:
			print(w[0])

train_words = list(train_words)
train_tags = list(train_tags)
train_words.append("ENDPAD")
#print(train_words)
#print(train_tags)
n_words = len(train_words)
n_tags = len(train_tags)


import matplotlib.pyplot as plt
"""plt.style.use("ggplot")
plt.hist([len(s) for s in train_data], bins=100)
plt.show()"""

max_len = 185
word2idx = {w: i for i, w in enumerate(train_words)}
print(word2idx)
tag2idx = {t: i for i, t in enumerate(train_tags)}

from keras.preprocessing.sequence import pad_sequences
X = [[word2idx[w[0]] for w in s] for s in train_data]
X = pad_sequences(maxlen=max_len, sequences=X, padding="post", value=n_words - 1)
y = [[tag2idx[w[1]] for w in s] for s in train_data]
y = pad_sequences(maxlen=max_len, sequences=y, padding="post", value=tag2idx["O"])

from keras.utils import to_categorical
y = [to_categorical(i, num_classes=n_tags) for i in y]

from sklearn.model_selection import train_test_split
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.1)

from keras.models import Model, Input
from keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional
input = Input(shape=(max_len,))
model = Embedding(input_dim=n_words, output_dim=max_len, input_length=max_len)(input)
model = Dropout(0.1)(model)
model = Bidirectional(LSTM(units=100, return_sequences=True, recurrent_dropout=0.1))(model)
out = TimeDistributed(Dense(n_tags, activation="softmax"))(model)  # softmax output layer
model = Model(input, out)
model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])
history = model.fit(X_tr, np.array(y_tr), batch_size=32, epochs=5, validation_split=0.1, verbose=1)

"""hist = pd.DataFrame(history.history)
plt.figure(figsize=(12,12))
plt.plot(hist["acc"])
plt.plot(hist["val_acc"])
plt.show()"""

i = 8
#print(X_te[i])
p = model.predict(np.array([X_te[i]]))
p = np.argmax(p, axis=-1)
print("{:15} ({:5}): {}".format("Word", "True", "Pred"))
for w, pred in zip(X_te[i], p[0]):
	if (train_words[w] == "ENDPAD"):
		break
	print("{:15}: {}".format(train_words[w], train_tags[pred]))