from django.shortcuts import render
import nltk
nltk.download()
from templates import dict
from nltk.corpus import wordnet
from PyDictionary import PyDictionary
from .models import *

# Create your views here.
def dictionary(request):
    if request.method == 'GET':
        return render(request, 'dict/main.html')
    elif request.method == 'POST':
        search = request.POST['search']
        dictionary = PyDictionary(search)
        meaning = dictionary.getMeanings()
        total  = []
        
       
        for i in meaning.values():
            if i == '' or i == None:
                mean = None
            else:
                for j in i.items():
                    
                    total += j
                print(total)
                if total == [] or total == None:
                    mean = ''
                else:
                    mean = ','.join(total[1])
                    save_data = Dictionary()
                    save_data.search = search
                    save_data.save()
        
        syn = wordnet.synsets(search)
        synonym = set()
        antonym = set()
        for i in syn:
            for j in i.lemmas():
                if j.antonyms():
                    antonym.add(j.antonyms()[0].name())
                synonym.add(j.name())
        
        syno = ','.join(synonym)
        anto = ','.join(antonym)
    
        if anto == '' or anto == None:
            anto = search
        if syno == '' or syno == None:
            syno = search


        
        context = {'synonym':syno,'total':mean,'anto': anto}
        return render(request, 'dict/main.html',context)