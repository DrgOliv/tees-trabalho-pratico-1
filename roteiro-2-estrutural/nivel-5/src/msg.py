import re

def mensagem(s):

	with open(s, 'r') as text:
		arq = [line for line in text]

	pontTotal = 0
	consTotal = 0
	vogsTotal = 0

	for line in arq:
		html = re.search(r'''(</{0,1}head.*>)|(</{0,1}body.*>)|(</{0,1}img.*>)|
						 (</{0,1}alt.*>)|(</{0,1}href.*>)''', line)
		susp = re.search(r'''([Mm][Ii][Ll][Ii][Oo][Nn][AÁaá][Rr][Ii][Oo])|
						 ([Ee][Mm][Pp][Rr][EÉeé][Ss][Tt][Ii][Mm][Oo])|
						 ([Ll][Oo][Tt][Ee][Rr][Ii][Aa])|
						 ([Bb][Aa][Nn][Cc][Oo])|
						 ([Ss][Oo][Rr][Tt][Ee][Ii][Oo])|
						 ([Ss][Ee][Gg][Uu][Ii][Dd][Oo][Rr])|
						 ([Dd][Ee][Ss][Cc][Oo][Nn][Tt][Oo])''', line)
		pont = re.findall(r'[\.\,\;\?\!]', line)
		cons = re.findall(r'[BCDEFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz]', line)
		vogs = re.findall(r'[^BCDEFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz0-9\W]', line)
		
		if html or susp:
			return 'spam'
		
		if pont:
			# print(len(pont))
			pontTotal += len(pont)
		
		if cons:
			# print(len(cons))
			consTotal += len(cons)
		
		if vogs:
			# print(len(vogs))
			vogsTotal += len(vogs)
	
	if pontTotal > 15 or consTotal > vogsTotal*2 or len(arq) <= 0:
		return 'spam'

	return 'ham'

