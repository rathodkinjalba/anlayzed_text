from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def analyze(request):
    if request.method == 'POST':
        djtext=request.POST.get('text','default')
        removepunc=request.POST.get('removepunc','off')
        fullcaps=request.POST.get('fullcaps','off')
        newlineremove=request.POST.get('newlineremove','off')
        extraspaceremove=request.POST.get('extraspaceremove','off')
 
        if removepunc == "on":
            Punctuations="~!@#$%^&*(){}[]<>,./?:"";'=-"
            analyzed=""
            for char in djtext:
                if char not in Punctuations:
                    analyzed = analyzed + char
            params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
            djtext=analyzed
        
        if fullcaps == "on":
            analyzed=""
            for char in djtext:
                analyzed = analyzed + char.upper()
            params={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
            djtext=analyzed

        if newlineremove == "on":
            analyzed=""
            for char in djtext:
                if char!="\n" and char!="\r":
                    analyzed = analyzed + char
            params={'purpose':'Removed NewLines','analyzed_text':analyzed}
            djtext=analyzed
        
        if extraspaceremove == "on":
            analyzed=""
            for index, char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index+1]==" "):
                    analyzed = analyzed + char
            params={'purpose':'Removed NewLines','analyzed_text':analyzed}
        if removepunc=="on"and fullcaps=="on"and newlineremove=="on"and extraspaceremove=="on":
            params={'purpose':'your Text is sucssesfully Analyzed','analyzed_text':analyzed}
        if removepunc != "on" and fullcaps != "on" and newlineremove != "on" and extraspaceremove != "on":
            return HttpResponse("please select any operation and try again")
        return render(request,'analyze.html',params) 
    

