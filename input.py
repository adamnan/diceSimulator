def int_input(sentence):
	while True:
		number = raw_input(sentence)
		try:
			number = int(number)
		except ValueError:	
			raise ValueError("Sorry that's not a number, pleace try again.")
			continue
		return number
		break
