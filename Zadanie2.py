powitania = {"kl":"nuqneH!","pl":"witaj!","en":"welcome!","it":"ciao!"} #tworzę słownik z czterema podstawowymi językami
yes = ["Yes","Y","y","yes"]

def tekstPowitania(język):
	if język in powitania:#jeśli język jest w podstawowym słowniku tłumaczę
		print(powitania[język])
	else:#jeśli języka nie ma w podstawowym słowniku
		#sprawdzam czy w systemie komputera jest zainstalowana biblioteka googletrans
		import sys
		import subprocess
		import pkg_resources
		if 'googletrans' in {pkg.key for pkg in pkg_resources.working_set}:	#jesli jest zainstalowana:
			try:	
				import googletrans
				from googletrans import Translator
				if język in googletrans.LANGUAGES:#oraz jeśli taki język istnieje w bazie języków google translate
					translator = Translator()
					result = translator.translate('Hello!',src='en',dest=język) #tłumaczę słowo "Hello!" na wybrany język
					print(result.text)
				else:
					print("sorry, i don't know the language " + język)
			except:
				print("sorry, something went wrong, I don't know the language " + język)
		elif input('do you want to pip install googletrans library? (Y/N)') in yes : # jeśli nie jest zainstalowana pytam się czy zainstalować
			#w wypadku odpowiedzi twierdzącej instaluję oraz wykonuję to samo co wyżej
			try:
				python = sys.executable
				subprocess.check_call([python, '-m', 'pip', 'install', 'googletrans'], stdout=subprocess.DEVNULL)
				import googletrans
				from googletrans import Translator
				if język in googletrans.LANGUAGES:
					translator = Translator()
					result = translator.translate('Hello!',src='en',dest=język)
					print(result.text)
				else:
					print("sorry, i don't know the language " + język)
			except:
				print("sorry, something went wrong, I don't know the language " + język)

def Powitanie():
	print("Here are all the available languages:")
	for i in powitania:
		print(i)
	x = input("Please choose the language of your choice:")
	print("chosen language: " + x)
	tekstPowitania(x)
	input("press enter to exit")

Powitanie()