#By Justin Serowik
from nltk.corpus import stopwords
from collections import Counter

# Function that outputs occurrence lists
def textCount(data):
	# Create list of characters to delete
	charDel = [".",",","/","?","<",">",":",";","[","]","{","}","-","_","+","=","|",'"',"!","@","#","$","%","^","&","*","(",")"]
	for char in charDel:
		data = data.replace(char,"")
	numDel = list(range(10))
	for num in numDel:
		data = data.replace(str(num),"")
	# Splits data into a list
	datAr = data.split()
	# Creates a list of stopwords to delete using the NLTK library
	stopDel = list(str(stopwords.words('english')))
	# Adding extra words not covered above
	ex = ["the", "The", "to","and", "of", "for", "is"]
	for w in ex:
		stopDel.append(w)
	for word in datAr:
		if word in stopDel:
			datAr.remove(word)
	# Uses Counter to make an occurrence list which is stored in a dictionary
	counts = Counter(datAr)
	index_terms = counts.items()
	return index_terms
# Function to create a trie using a list of words
end = 'last'
def create_trie(words):
	root = {}
	ind = 0
	for word in words:
		current_dict = root
		for letter in word:
			current_dict = current_dict.setdefault(letter, {})
		current_dict[end] = ind
		ind = ind + 1
	return root
# Function to find and return the index value from a trie
def test_trie(trie, word):
	current_dict = trie
	for letter in word:
		if letter in current_dict:
			current_dict = current_dict[letter]
		else:
			return 0
	else:
		if end in current_dict:
			return current_dict[end]
		else:
			return 0

# Function that gets tries from all 8 sources
trie = []
indexTerms = []
def trieForm():
	for i in range(0,8):
		# Opens Text file with text from a scraped webpage
		file = "Data/"+(str(i))+".txt"
		logr_file = open(file)
		dt = logr_file.read()
		logr_file.close()
		# returns text count
		iterms = textCount(dt)
		indexTerms.append(textCount(dt))
		# creates list of words from the dictionary to make a trie out of
		wordList=[]
		for w in iterms:
			wordList.append(w[0])
		trie.append(create_trie(wordList))
#Creates tries and occurance lists for each webpage
trieForm()
# creates the rank list for searching
rank = []
def search(term):
	# create temp list to split search term into
	temp = []
	temp = term.split()
	print "Search terms:"
	print temp
	# iterate through every trie
	for i in range(0,8):
		sum = 0
		#iterate through every search term
		for t in temp:
			# If search finds the term, it adds the occurrences to the rank
			if test_trie(trie[i], t) > 0:
				# Uses index at the bottom of trie to find number of occurrences in the index terms
				sum = sum + int(indexTerms[i][test_trie(trie[i], t)][1])
		rank.append(sum)
	return rank

#Test the search terms to return the ranks from the search
test = search("Atlanta Obama unemployment")
# Iterate through the ranks and output
for it in range(0,7):
	print "Webpage "+str(it)+" rank:"
	print test[it]