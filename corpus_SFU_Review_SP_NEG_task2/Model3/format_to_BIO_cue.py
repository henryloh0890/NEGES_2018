import string
import re

def clean(word):
	x = word
	x = x.replace('<scp>','')
	x = x.replace('</scp>','')
	x = x.replace('<dis>','')
	x = x.replace('</dis>','')
	return x

def parse_word (word,flag):
	ori = clean(word)
	if flag == "B":
		ori = ori+"|B-C"
	elif flag == "I":
		ori = ori+"|I-C"
	else:
		ori = ori+"|O"
	return ori

def parse_sent (sentence):
	s = sentence.split()
	punc = [".","?",":","!",",",";"]
	for id,x in enumerate(s):
		if x[-1:] in punc and len(x) > 1:
			s[id] = x[:-1]
			s.insert(id+1,x[-1:])
	res = ""
	ins = False
	flag = "O"
	for id,w in enumerate(s):
		if "<neg>" in w and "</neg>" in w:
			ins = True
			flag = "B"
			s[id] = parse_word(w,flag)
			s[id]  = s[id] .replace('<neg>','')
			s[id]  = s[id] .replace('</neg>','')
			flag = "O"
			ins  = False
		elif "<neg>" in w:
			ins = True
			flag = "B"
			s[id] = parse_word(w,flag)
			s[id]  = s[id] .replace('<neg>','')
		elif ins and not "</neg>" in w:
			flag = "I"
			s[id] = parse_word(w,flag)
			s[id]  = s[id] .replace('</neg>','')
		elif ins and "</neg>" in w:
			flag = "I"
			s[id] = parse_word(w,flag)
			s[id]  = s[id] .replace('</neg>','')
			ins = False
			flag = "O"
		else:
			s[id] = parse_word(w,flag)
	
	for i in s:
		if i in string.punctuation:
			res = res + i
		else:
			res = res+" "+i
	
	return res.strip()
	
result = open("diann_esp_train_BIO_c.txt","w")

with open("diann_esp_train.txt") as f:
	for line in f:
		result.write(parse_sent(line)+"\n")
