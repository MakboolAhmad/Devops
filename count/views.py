
from django.http import HttpResponse
from django.shortcuts import render




def home(request):
	return render (request,'mk.html')

def count(request):
	fulltext = request.GET['fulltext']
	print(fulltext)
	worlist=fulltext.split()
	worddict={}
	for word in worlist:
		if word in worddict:
			worddict[word]+=1
		else:
			worddict[word]=1

	return render(request,'count.html',{'fulltext':fulltext,'count':len(worlist),'worddict':worddict})
