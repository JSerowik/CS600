
# Opens Text file with text from a scraped webpage
logr_file = open("Data/cnbcE_adjusted-for-inflation-the-federal-minimum-wage-is-worth-less-than-50-years-ago.html.txt")
data = logr_file.read()
logr_file.close()
# Create list of characters to delete
charDel = [".",",","/","?","<",">",":",";","[","]","{","}","-","_","+","=","|",'"',"!","@","#","$","%","^","&","*","(",")"]
for char in charDel:
	data = data.replace(char,"")
numDel = list(range(10))
for num in numDel:
	data = data.replace(str(num),"")
# Splits data into a list
datAr = data.split()
wordList = []
for word in datAr:
	if word not in wordList:
		wordList.append(word)
		 
print wordList