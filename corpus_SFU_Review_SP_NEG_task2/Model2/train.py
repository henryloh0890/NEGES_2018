import glob
import os.path,subprocess
from subprocess import STDOUT,PIPE

#fnlist = glob.glob("/home/loharja/PhD/DIANN/Test/lingscope3/esp_raw/tkn/*.txt")
fnlist = glob.glob("/home/loharja/PhD/NEGES_2018/task2/corpus_SFU_Review_SP_NEG_task2/Model2/*_inBIO.txt")
os.system("javac -cp .:abner.jar train.java")

for i in fnlist:
	print("processing "+i)
	fn = os.path.basename(i)
	#cmd = ['java', "-cp", ".:oldlingscope.jar", "testcue", i, ">", os.path.join('/home/loharja/PhD/DIANN/Test/lingscope3/esp_res',"res"+os.path.basename(i))]
	#os.system("java -cp .:oldlingscope.jar testcue "+i+" > "+os.path.join('/home/loharja/PhD/DIANN/Test/lingscope3/esp_res',"res"+os.path.basename(i)))
	os.system("java -cp .:abner.jar train "+i+" "+fn[:-10]+".model")