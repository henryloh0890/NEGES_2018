import string
import re

neg = 0
ns = 0
cuelist = set()
tokenlist = set()

def get_freq_cue(item):
	freq = 0
	with open("neges_train_all_inBS.txt") as f:
		for line in f:
			if item in line.lower():
				x =re.findall("<neg>"+item+"</neg>",line.lower())
				freq+=len(x)
	return freq
	
def get_freq_token(item):
	freq = [0,0]
	with open("neges_train_all_inBS.txt") as f:
		for line in f:
			if item in line.lower():
				to = line.lower().replace("<neg>","").replace("</neg>","").split().count(item)
				x = re.findall('<neg>.*?</neg>',line)
				n = 0
				for i in x:
					a = i.lower().replace("<neg>","").replace("</neg>","").split()
					n+=a.count(item)
				freq[0]+=n
				freq[1]+=to-n
	return freq


cue = open("statcue.txt","w")
sent = open("statsent.txt","w")

sentwithcue = 0
sentnocue = 0
senttotal = 0

with open("neges_train_all_inBS.txt") as f:
	for line in f:
		senttotal+=1
		if "<neg>" in line:
			sentwithcue+=1
			#sent.write(line+"\n")
			x =re.findall('<neg>.*?</neg>',line)
			for i in x:
				cuelist.add(i.lower().replace("<neg>","").replace("</neg>",""))
				tokenlist.update(i.lower().replace("<neg>","").replace("</neg>","").split())
		else:
			sentnocue+=1
sent.write("Number total of sentences= "+str(senttotal)+"\n")
sent.write("Number of sentences with cue= "+str(sentwithcue)+"\n")
sent.write("Number of sentences without cue= "+str(sentnocue)+"\n")
sent.write("Percentage of sentences with cue= "+str(sentwithcue*100/senttotal)+"\n\n")

sent.write("Sentences contains cue tokens but not annotated as negation:\n")
sent.write("==========================================\n")
with open("neges_train_all_inBS.txt") as f:
	for line in f:
		if not "<neg>" in line:
			temp = []
			for t in tokenlist:
				if t in line.lower().split():
					temp.append(t)
			if len(temp) != 0:
				sent.write(line)
				sent.write("Tokens not annotated= "+str(temp)+"\n")
				sent.write("==========================================\n")
		else:
			temp = []
			for t in tokenlist:
				x = re.findall('<neg>.*?</neg>',line)
				to = line.lower().replace("<neg>","").replace("</neg>","").split().count(t)
				n=0
				for i in x:
					a = i.lower().replace("<neg>","").replace("</neg>","").split()
					n+=a.count(t)
				if to > n:
					temp.append(t)
			if len(temp) != 0:
				sent.write(line)
				sent.write("Tokens not annotated= "+str(temp)+"\n")
				sent.write("==========================================\n")

#print(cuelist)
#print(tokenlist)
cue.write("List of cues in the training + frequency"+"\n\n")
for c in cuelist:
	cue.write(c+"\t"+str(get_freq_cue(c))+"\n")
	
cue.write("================================================================================\n")
cue.write("List of cue tokens in the training + #in cues + #outside cues"+"\n\n")
for t in tokenlist:
	f = get_freq_token(t)
	cue.write(t+"\t"+str(f[0])+"\t"+str(f[1])+"\n")