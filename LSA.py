#coding : utf-8
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from numpy.linalg import svd as NumpySVD
#import nltk as NLTK
import numpy as Numpy
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize

class LSA:
	def __init__(self):
		theIndex = {}
		self.theVectorizer = CountVectorizer(stop_words='english')
		pass
	def sumDoc(self,aDoc):
		mySents = sent_tokenize(aDoc);
		myMatrix = self.theVectorizer.fit_transform(mySents).transpose().todense()
		U,E,V = NumpySVD(myMatrix)
		E = Numpy.diag(E)
		mySentMatrix = Numpy.dot(E,V)
		mySentScores = []
		for i in range(mySentMatrix.shape[1]):
			mySentScores.append(Numpy.linalg.norm(mySentMatrix[:,i]))
		myRanks =  Numpy.argsort(Numpy.array(mySentScores)).tolist()
		myRanks.reverse()
		myStr = ""
		for i in myRanks[0:5]:
			myStr = myStr + mySents[i] + "<br/>"
		return myStr

if __name__ == '__main__':
	myVectorizer = CountVectorizer(stop_words='english')

	myStory = args[1]
	mySents = sent_tokenize(myStory);
	myMatrix = myVectorizer.fit_transform(mySents).transpose().todense()
	U,E,V = NumpySVD(myMatrix)

	E = Numpy.diag(E)

	mySentMatrix = Numpy.dot(E,V)
	mySentScores = []
	for i in range(mySentMatrix.shape[1]):
		mySentScores.append(Numpy.linalg.norm(mySentMatrix[:,i]))
	myRanks =  Numpy.argsort(Numpy.array(mySentScores)).tolist()
	myRanks.reverse()
	print myRanks
	for i in myRanks[0:5]:
		print mySents[i]
		print "\n"