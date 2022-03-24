class Word:
	def __init__(self):
		self.dom = ""
		self.sen = ""
		self.tok = ""
		self.word = ""
		self.lemma = ""
		self.pos = ""
		self.postype = ""
		self.neg = []


import string
import os

def check_neg(n):
	res = -1
	#for x in n.neg:
	#	if x!="-" and x!="***":
	#		res = True
	#		break
	if not n.word in ["-","***"] and n.word in n.neg:
		res = n.neg.index(n.word)
	return res

def parse_line (li):
	ls = li.split('\t')
	res = ""
	w = Word()
	w.dom = ls[0]
	w.sen = ls[1]
	w.tok = ls[2]
	w.word = ls[3]
	w.lemma = ls[4]
	w.pos = ls[5]
	w.postype = ls[6]
	for x in ls[7:]:
		w.neg.append(x)
	return w

dom = input("Domain? ")
input = "train_"+dom+"_task2.txt"
sentence = []
with open(input) as f:
	fn = os.path.basename(input)
	result  = open(fn[:-4]+"_inBIO.txt","w")
	#s = open(fn[:-4]+"_sentstat.txt","w")
	#sent = ""
	pointer = -1
	for line in f:
		
		if line != "\n":
			#print(line)
			t = parse_line(line)
			#print(t.neg)
			sentence.append(t)
		else:
			cue = 0
			for id,w in enumerate(sentence):
				if not id == 0:
					result.write(" ")
					#sent+=" "
				
				result.write(sentence[id].word+"$"+sentence[id].pos)
				#sent+=sentence[id].word
				
				
				if check_neg(sentence[id]) != -1 and check_neg(sentence[id]) > pointer:
					result.write("|B-C")
					#sent+="|B-C"
					pointer = check_neg(sentence[id])
				elif check_neg(sentence[id]) != -1 and check_neg(sentence[id]) == pointer:
					result.write("|I-C")
					#sent+="|I-C"
					pointer = check_neg(sentence[id])
				else:
					result.write("|O")
					#sent+="|O"
				
			if not "***" in sentence[0].neg:
				cue+= (len(sentence[0].neg)-1)/3
			result.write("\n")
			#sent+="\n"
			#sent+="number of cues= "+str(cue)+"\n"
			#sent+="number of tokens= "+str(len(sentence))+"\n"
			#sent+="====================================================\n"
			#if cue > 0:
			#	s.write(sent)
			#s.write(sentence[0].dom+'\t'+sentence[0].sen+'\n')
			sentence.clear()
			#sent=""
			pointer = -1
			