import glob
import os.path,subprocess
from subprocess import STDOUT,PIPE


goldlist = glob.glob("/home/loharja/PhD/NEGES_2018/task2/lingscope/dev/*_task2.txt")
systemlist = glob.glob("/home/loharja/PhD/NEGES_2018/task2/lingscope/Baseline/specific/20/*_conll.txt")

for i in goldlist:
	print("processing "+i)
	fn = os.path.basename(i).replace("dev_","").replace(".txt","")
	#print(fn)
	mn = ""
	for m in systemlist:
		if fn in os.path.basename(m):
			mn = m
			print(mn)
	os.system("perl scorer_task2.pl -g "+i+" -s "+mn)