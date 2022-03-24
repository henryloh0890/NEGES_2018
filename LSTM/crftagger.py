import nltk
import io
from nltk.tag import CRFTagger
import glob
import os
import codecs
import re
import unicodedata
from nltk.tag.util import tuple2str
from nltk.tag.perceptron import PerceptronTagger

def get_pos(token):
	temp=token.split("$")
	return temp[1]

def get_word(token):
	temp=token.split("$")
	return temp[0]

def get_features(tokens, idx):
	#print("used")
	token = tokens[idx]
	wsize = 6
	before = []
	after = []
	neg = ["sin","no","tampoco"]
	special1 = ["nada","ni","nunca","ningun",u"ning\u00FAn","ninguno","ninguna","alguna","apenas","para_nada","ni_siquiera"]
	special2 = ["mucho","muchos","mucha","muy","en_absoluto","demasiado","tan","tanto","tanta","del_todo","siquiera",u"m\u00E1s"]
	punc = [":",",",";","(",")"]
	specw = []
	bias = 0.0
	
	for s in range(wsize):
		s+=1
		if idx-s >= 0:
			before.append(tokens[idx-s])
		#if idx+s <= len(tokens)-1:
		#	after.append(tokens[idx+s])
			
	for a in range(idx):
		a+=1
		if idx-a >= 0:
			specw.append(get_word(tokens[idx-a]))
		if get_word(tokens[idx-a]) in punc:
			break
	
	feature_list = []
	
	"""if idx > 0:
		before.append(tokens[idx-1])
	if idx < len(tokens)-1:
		after.append(tokens[idx+1])
	print(token)
	print("before = "+str(before))
	print("after = "+str(after))
	print("----------------------------------")"""
		
	# Capitalization 
	if token[0].isupper():
		feature_list.append('INIT_CAP')
	
	# Number 
	#print(token)
	if bool(re.search(r'\d', get_word(token))):
		feature_list.append('HAS_NUM') 
	
	if bool(re.search(r'[A-Z]+', get_word(token))):
		feature_list.append('HAS_CAP') 
	
	if bool(re.search(r'.*-.*', get_word(token))):
		feature_list.append('HAS_DASH')
	
	if bool(re.search(r'.*_.*', get_word(token))):
		feature_list.append('HAS_US')
	
	if bool(re.search(r'.*[A-Za-z].*[0-9].*', get_word(token))) or bool(re.search('.*[0-9].*[A-Za-z].*',get_word(token))):
		feature_list.append('ALPHANUM') 
	
	# Punctuation
	punc_cat = set(["Pc", "Pd", "Ps", "Pe", "Pi", "Pf", "Po"])
	if all (unicodedata.category(x) in punc_cat for x in get_word(token)):
		feature_list.append('PUNCTUATION')
	
	# Suffix up to length 4
	if len(get_word(token)) >= 2: 
		feature_list.append('SUF2_' + get_word(token)[-2:])
	else:
		feature_list.append('SUF2_' + get_word(token))
	if len(get_word(token)) >= 3: 
		feature_list.append('SUF3_' + get_word(token)[-3:])
	else:
		feature_list.append('SUF3_' + get_word(token))
	if len(get_word(token)) >= 4: 
		feature_list.append('SUF4_' + get_word(token)[-4:])
	else:
		feature_list.append('SUF4_' + get_word(token))
	
	# prefix up to length 4
	if len(get_word(token)) >= 2: 
		feature_list.append('PREF2_' + get_word(token)[:2])
	else:
		feature_list.append('PREF2_' + get_word(token))
	if len(get_word(token)) >= 3: 
		feature_list.append('PREF3_' + get_word(token)[:3])
	else:
		feature_list.append('PREF3_' + get_word(token))
	if len(get_word(token)) >= 4: 
		feature_list.append('PREF4_' + get_word(token)[:4])
	else:
		feature_list.append('PREF4_' + get_word(token))
	
	c=0
	while c < len(before)-1:
		feature_list.append('2GRAMBEFORE'+str(c)+'_'+get_word(before[c+1])+'&'+get_word(before[c]))
		#feature_list.append('NGRAMBEFOREPOS'+str(c)+'_'+get_pos(before[c+1])+'&'+get_pos(before[c]))
		c+=1
	"""d=0
	while d < len(before)-2:
		feature_list.append('3GRAMBEFORE'+str(d)+'_'+get_word(before[d+2])+'&'+get_word(before[d+1])+'&'+get_word(before[d]))
		#feature_list.append('NGRAMBEFOREPOS'+str(c)+'_'+get_pos(before[c+1])+'&'+get_pos(before[c]))
		d+=1"""
	for x in range(len(before)):
		feature_list.append('BEFORE'+str(x)+'_'+get_word(before[x]))
		feature_list.append('BEFOREPOS'+str(x)+'_'+get_pos(before[x]))
	
	if idx < len(tokens)-1:
		feature_list.append('2GRAMAFTER_'+get_word(tokens[idx])+'&'+get_word(tokens[idx+1]))
		#feature_list.append('NGRAMAFTERPOS_'+get_pos(tokens[idx])+'&'+get_pos(tokens[idx+1]))
		feature_list.append('AFTER_'+get_word(tokens[idx+1]))
		feature_list.append('AFTERPOS_'+get_pos(tokens[idx+1]))
	
	if idx > 0:
		feature_list.append('2GRAMBEFORE_'+get_word(tokens[idx-1])+'&'+get_word(tokens[idx]))
	#if idx > 1:
	#	feature_list.append('3GRAMBEFORE_'+get_word(tokens[idx-2])+'&'+get_word(tokens[idx-1])+'&'+get_word(tokens[idx]))
	
	have_n = False
	for a in specw:
		if a.lower() in special1 or a.lower() in neg:
			have_n=True
	
	if get_word(token).lower() in special1 and have_n or any(x in get_word(token).lower() for x in special1):
		feature_list.append('SPECIAL1')
		bias += 0.5
	
	if (get_word(token).lower() in special2 or any(x in get_word(token).lower() for x in special2))and have_n:
		feature_list.append('SPECIAL2')
		bias+=0.3
	
	if have_n:
		feature_list.append('NEG_BEFORE')
	
	if get_word(token).lower() in neg:
		bias+=0.5
	
	feature_list.append('WORD_' + get_word(token))
	feature_list.append('POS_' + get_pos(token))
	feature_list.append('BIAS_' + str(bias))
	
	#print(feature_list)
	return feature_list

train_data = []
param = {'max_iterations':'500','linesearch':'Backtracking','feature.possible_states':'1','feature.possible_transitions':'1'}
ct = CRFTagger(get_features,True,param)
with io.open("neges_train_task2_inBIO3.txt",encoding='utf-8') as f:
	for line in f:
		tagged_sent = []
		for t in line.split():
			if t[0] != "|":
				tagged_sent.append(nltk.tag.str2tuple(t,'|')) 
				
		train_data.append(tagged_sent)
#print(train_data)
ct.train(train_data,"crfPOS.model")

fnlist = glob.glob("/home/loharja/PhD/NEGES_2018/task2/corpus_SFU_Review_SP_NEG_task2/test/*_raw.txt")

#ct = CRFTagger()
mn = "/home/loharja/PhD/NEGES_2018/task2/nltk/crfPOS.model"
#ct.set_model_file(mn)
print("Model: "+mn)
for fn in fnlist:
	i = os.path.basename(fn)
	result = codecs.open(os.path.join('/home/loharja/PhD/NEGES_2018/task2/nltk/testresult',i).replace("raw","res"),"w","utf-8")
	print("Processing: "+i)
	with io.open(fn,encoding='utf-8') as f:
		test_sents = []
		for line in f:
			sent = []
			for t in line.split():
				sent.append(t) 
			#print(sent)
			test_sents.append(sent)
		tagged_sents = ct.tag_sents(test_sents)
			
		for x in tagged_sents:
			s=""
			for y in x:
				s+= tuple2str(y,"|")+" "
			result.write(s.strip()+"\n")