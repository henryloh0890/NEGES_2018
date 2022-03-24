import nltk
import io
import re
import unicodedata
from nltk.tag import CRFTagger		

def get_features(tokens, idx):
	#print("used")
	token = tokens[idx]
	wsize = 1
	before = []
	after = []
	
	for s in range(wsize):
		s+=1
		if idx-s >= 0:
			before.append(tokens[idx-s])
		if idx+s <= len(tokens)-1:
			after.append(tokens[idx+s])
	#before.append(tokens[idx-1])
	#after.append(tokens[idx+1])
	#print(before)
	#print(after)
	feature_list = []
	
	if not token:
		return feature_list
		
	# Capitalization 
	if token[0].isupper():
		feature_list.append('CAPITALIZATION')
	
	# Number 
	#print(token)
	if bool(re.search(r'\d', token)):
		feature_list.append('HAS_NUM') 
	
	# Punctuation
	punc_cat = set(["Pc", "Pd", "Ps", "Pe", "Pi", "Pf", "Po"])
	if all (unicodedata.category(x) in punc_cat for x in token):
		feature_list.append('PUNCTUATION')
	
	# Suffix up to length 3
	if len(token) > 1:
		feature_list.append('SUF_' + token[-1:])
	else:
		feature_list.append('SUF_' + token)
	if len(token) > 2: 
		feature_list.append('SUF_' + token[-2:])
	else:
		feature_list.append('SUF_' + token)
	if len(token) > 3: 
		feature_list.append('SUF_' + token[-3:])
	else:
		feature_list.append('SUF_' + token)
	
	# prefix up to length 3
	if len(token) > 1:
		feature_list.append('PREF_' + token[1:])
	else:
		feature_list.append('PREF_' + token)
	if len(token) > 2: 
		feature_list.append('PREF_' + token[2:])
	else:
		feature_list.append('PREF_' + token)
	if len(token) > 3: 
		feature_list.append('PREF_' + token[3:])
	else:
		feature_list.append('PREF_' + token)
	
	for x in range(len(before)):
		feature_list.extend(get_features(before,x))
	for y in range(len(after)):
		feature_list.extend(get_features(after,y))
	
	feature_list.append('WORD_' + token )
	
	return feature_list

train_data = []
ct = CRFTagger(get_features,True)
with io.open("neges_train_task2_inBIO.txt",encoding='utf-8') as f:
	for line in f:
		tagged_sent = []
		for t in line.split():
			if t[0] != "|":
				tagged_sent.append(nltk.tag.str2tuple(t,'|')) 
				
		train_data.append(tagged_sent)
#print(train_data)
ct.train(train_data,"crf.model")	