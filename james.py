import datetime
from googie import google_translator  
import random
import time
tetst=73


while tetst==73: 
	times=0

	menu=input("Menu? y/n")
	if menu=="y":
		midwant=input("Do you want a sample in the middle y/n")
		wantnum=int(input("Do you want a number. 1.Yes 2.No"))
		num2=int(input("How many times to run?  "))
		num1=num2/2
		num=int(num1)
	elif menu=="n":
		wantnum=1
		numinp=20
		numint=numinp/2
		num=int(numint)
		midwant="y"
	else:
		print("Err")
		exit()
	words=input()
	translator = google_translator()  
	print("translating...")
	for q in range(num):
		hi=random.choice(['fr', 'en', 'zh', 'mt','ga','he','af','cy'])
		translate_text = translator.					translate(words,lang_tgt=hi)
		words=translate_text
		times=times+1
		if wantnum==1:
			print(times,"out of", num*2)
	if midwant=="y":	
		print(".")
		res = translator.translate(words,lang_tgt='en')
		print("One result is", res)
		print(".")
	
	for q in range(num):
		hi=random.choice(['la', 'ig', 'zh', 'mt','ga','he','af','cy','tr','tt','uz'])
		translate_text = translator.					translate(words,lang_tgt=hi)
		words=translate_text
		times=times+1
		if wantnum==1:
			print(times,"out of", num*2)
	now = translator.translate(words,	lang_tgt='en')
	print("Done!")
	print( )
	print(now)
	print( )
	loc2="/storage/emulated/0/Pythontext/"
	ab=100
	rando=random.randint(1,827733834883)
	randostr=str(rando)
	text=".txt"
	x = datetime.datetime.now()
	x=str(x)
	texto=loc2+x+text
	wnttxt=input("Do you want a text file y/n")
	if wnttxt=="y":
		text_file = open(texto, "wt")
		n = text_file.write(now)
		text_file.close()
		print("Saved in", texto)
	

	ask=input("Want to mess it up more? y/n")
	if ask == "y":
		for q in range(num):
			hi=random.choice(['la', 'ig', 'zh', 'mt','ga','he','af','cy','tr','tt','uz'])
			translate_text = translator.					translate(words,lang_tgt=hi)
			words=translate_text
			times=times+1
			if wantnum==1:
				numext=(num*2)+num
				numextint=int(numext)
				print(times,"out of", numextint)
		now = translator.translate(words,	lang_tgt='en')
		print("Done!")
		print( )
		print(now)
		print( )
		x = datetime.datetime.now()
		x=str(x)
		texto=loc2+x+text
		wnttxt=input("Do you want a text file y/n")
		if wnttxt=="y":
			text_file = open(texto, "wt")
			n = text_file.write(now)
			text_file.close()
			print("Saved in", texto)
	
	rest=input("Restart y/n")
	if rest=="n":
		exit()
	else:
		print( )
		print( )
		print( )
		print( )
