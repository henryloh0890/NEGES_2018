with open("diann_esp_train.txt") as x:
	text = x.read()
	text = text.replace("<dis>","")
	text = text.replace("</dis>","")
	
with open("diann_esp_train.txt", "w") as f:
	f.write(text)