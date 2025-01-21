from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def analyze(request):
    text=request.POST.get('text','default')
     
    removePunc=request.POST.get('removePunc','off')
    charCount=request.POST.get('charCount','off')
    spaceCount=request.POST.get('spaceCount','off')
    newLineRemover=request.POST.get('newLineRemover','off')
    spaceRemover=request.POST.get('spaceRemover','off')
    upperCase=request.POST.get('upperCase','off')
    lowerCase=request.POST.get('lowerCase','off')

    analyzedText=""
    params={}

    if removePunc=='on':
        punctuation=".,;:!?\"'()-[]{}<>/\\|@#$%^&*_~`"
        for char in text:
          if char not in punctuation:
             analyzedText+=char
        params={'originalText':text,'purpose':'Removed Punctuation','analyzeText':analyzedText,'removePunc':True}
        return render(request,'analyze.html',params) 
    
    
    if charCount=='on':
        numChar=int(0)
        for char in text:
          numChar+=1
        params={'originalText':text,'purpose':'count Character ','analyzeText':numChar,'charCount':True}
        return render(request,'analyze.html',params) 
    
    if spaceCount=='on':
        numSpace=int(0)
        for char in text:
          if char==' ':
             numSpace+=1
        params={'originalText':text,'purpose':'count Character ','analyzeText':numSpace,'spaceCount':True}
        return render(request,'analyze.html',params)    
     
    if upperCase == 'on':
        for char in text:
          analyzedText+=char.upper()
        params={'originalText':text,'purpose':'upperCase ','analyzeText':analyzedText,'upperCase':True}
        return render(request,'analyze.html',params)   
    
    if lowerCase == 'on':
        for char in text:
          analyzedText+=char.lower()
        params={'originalText':text,'purpose':'lowereCase ','analyzeText':analyzedText,'lowerCase':True}
        return render(request,'analyze.html',params)    
    
    if newLineRemover == 'on':
        for char in text:
          if char!='\n':
             analyzedText+=char
        params={'originalText':text,'purpose':'newLineRemover','analyzeText':analyzedText,'newLineRemover':True}
        return render(request,'analyze.html',params)    
    
    if spaceRemover == 'on':
        for index,char in enumerate(text):
           if not( text[index]==' ' and text[index+1]==' '):
              analyzedText+=char
        params={'originalText':text,'purpose':'spaceRemover','analyzeText':analyzedText,'spaceRemover':True} 
        return render(request,'analyze.html',params)    
    return HttpResponse("Please Select Any Option Given Below in the form of check Box!!!")     


    
    
    
