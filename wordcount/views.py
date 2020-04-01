from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
  return render(request,'home.html')

def count(request):
    text=request.GET["text"]
    words=text.split()
    worddict={}
    for word in words:
        if word in worddict:worddict[word]+=1
        else:worddict[word]=1
    sorted_list=sorted(worddict.items(),key=lambda freq: (-freq[1],freq[0]))
    return render(request,'count.html',{'length':len(words),'sorted_list':sorted_list})

def about(request):
    return render(request,'about.html')

