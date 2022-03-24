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
	res = False
	#for x in n.neg:
	#	if x!="-" and x!="***":
	#		res = True
	#		break
	if not n.word in ["-","***"] and n.word in n.neg:
		res = True
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
	result  = open(fn[:-4]+"_inBS.txt","w")
	d = open(fn[:-4]+"_domdict.txt","w")
	for line in f:
		if line != "\n":
			#print(line)
			t = parse_line(line)
			#print(t.neg)
			sentence.append(t)
		else:
			for id,w in enumerate(sentence):
				if not id == 0:
					result.write(" ")
				#if check_neg(sentence[id]) == True:
				#	resultneg.write("<neg>")
				#result.write(sentence[id].word)
				#resultneg.write(sentence[id].word)
				#if  check_neg(sentence[id]) == True:
				#	resultneg.write("</neg>")
				
				
				if id == 0 and check_neg(sentence[id]) == True:
					result.write("<neg>")
				elif id != 0 and check_neg(sentence[id-1]) == False and check_neg(sentence[id]) == True:
					result.write("<neg>")
				
				result.write(sentence[id].word+"$"+sentence[id].pos)
				
				if id == len(sentence)-1 and check_neg(sentence[id]) == True:
					result.write("</neg>")
				elif id != len(sentence)-1 and check_neg(sentence[id+1]) == False and check_neg(sentence[id]) == True:
					result.write("</neg>")
			result.write("\n")
			d.write(sentence[0].dom+'\t'+sentence[0].sen+'\n')
			sentence.clear()
