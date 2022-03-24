class Word:
	def __init__(self):
		self.dom = ""
		self.sen = ""
		self.tok = ""
		self.word = ""
		self.lem = ""
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
	w.lem = ls[4]
	w.pos = ls[5]
	w.postype = ls[6]
	return w

#dom = input("Domain? ")
domain = ("coches","hoteles","lavadoras","libros","musica","moviles","ordenadores","peliculas")
for dom in domain:
	input = "/home/loharja/PhD/NEGES_2018/task2/corpus_SFU_Review_SP_NEG_task2/dev/dev_"+dom+"_task2.txt"
	input2 = "/home/loharja/PhD/NEGES_2018/task2/nltk/result/dev_"+dom+"_task2_res.txt"

	sentence = []
	sentence2 = []
	doc2 = []
	words2 = []

	with open(input) as f, open(input2) as f2:
		fn = os.path.basename(input)
		result  = open(fn[:-4]+"_conll.txt","w")
		
		doc2 = f2.readlines()
		#print(doc2)
		for x in doc2:
			words2.extend(x.split())
			

		count = 0
		neg = 0
		for line in f:
			if line != "\n":
				#print(line)
				t = parse_line(line)
				#print(t.neg)
				#print(str(count)+"_"+str(len(words2)))
				
				o = words2[count].split("|")[0]
				
				for _ in range(neg):
					t.neg.extend(["-","-","-"])
				if t.word == o and "|B-C" in words2[count]:
					for x in sentence:
						x.neg.extend(["-","-","-"])
					t.neg.extend([t.word,"-","-"])
					neg+=1
				elif t.word == o and "|I-C" in words2[count]:
					if neg == 0:
						for x in sentence:
							x.neg.extend(["-","-","-"])
						t.neg.extend([t.word,"-","-"])
						neg+=1
					else:
						t.neg[(neg-1)*3] = t.word
				
				elif t.word != o:
					print("WARNING!\n"+t.word+"\n"+o)
				sentence.append(t)
				#sentence2.append(words2[count])
				count+=1
			else:
				for id,w in enumerate(sentence):
					result.write(w.dom+"\t"+w.sen+"\t"+w.tok+"\t"+w.word+"\t"+w.lem+"\t"+w.pos+"\t"+w.postype+"\t")
					if len(w.neg) == 0:
						result.write("***")
					else:
						t = ""
						for n in w.neg:
							t = t + n + "\t"
						result.write(t.rstrip("\t"))
					result.write("\n")
					neg = 0
				sentence.clear()
				result.write("\n")
				#sentence2.clear()
