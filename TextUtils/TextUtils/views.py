# custom file - Samrat Adhikari

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Samrat',
              'address': 'Nepal'}

    return render(request, 'index.html', params)

def analyze(request):
    # extract text from textarea
    formText = request.POST.get('text', 'default')

    # check if Remove Punctuations feature is on
    remove_punc = request.GET.get('removePunc', 'default')

    # check if Capitalize Letters feature is on
    capitalize = request.GET.get('capitalize', 'default')

    # check if Remove Spaces feature is on
    spaceRmv = request.GET.get('spaceRmv', 'default')

    # check if Remove New Line feature is on
    charCount = request.GET.get('charCount', 'default')

    # check if Uppercase Letters feature is on
    uppercase = request.GET.get('uppercase', 'default')

    # check if Lowercase Letters feature is on
    lowercase = request.GET.get('lowercase', 'default')

    count = 0
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
    analyzed = ""

    if remove_punc == 'on':
        analyzed = ""
        for char in formText:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}

        formText = analyzed
        # return render(request, 'analyze.html', params)
    

    if uppercase == 'on':
        analyzed = formText.upper()
        params = {'purpose': 'Uppercase characters', 'analyzed_text': analyzed}
        formText = analyzed

        # return render(request, 'analyze.html', params)
    

    if lowercase == 'on':
        analyzed = formText.lower()
        params = {'purpose': 'Lowercase characters', 'analyzed_text': analyzed}
        formText = analyzed

        # return render(request, 'analyze.html', params)
    

    if capitalize == 'on':
        analyzed = formText[0].upper() + formText[1:]
        params = {'purpose': 'Capitalize string', 'analyzed_text': analyzed}
        formText = analyzed


        # return render(request, 'analyze.html', params)
    

    if spaceRmv == 'on':
        analyzed = ""
        for char in formText:
            if char != ' ':
                analyzed = analyzed + char
        params = {'purpose': 'Removed spaces', 'analyzed_text': analyzed}
        formText = analyzed

        # return render(request, 'analyze.html', params)
    
    
    if charCount == 'on':
        for char in formText:
            count += 1
        params = {'purpose': 'Counted characters', 'analyzed_text': f'{analyzed}\nTotal no of characters: {count}'}
        # formText = analyzed
    return render(request, 'analyze.html', params)

