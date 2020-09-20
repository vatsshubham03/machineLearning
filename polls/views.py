from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
from django.shortcuts import render

import pickle

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
def index(request):
    #return  HttpResponse('<h1>hello</h1>')
    #return render(request, 'home_page.html')
    return render(request, 'home_page.html', {
        'foo': 'bar',
    })

def form(request):
    return render(request, 'form_page.html')

def login(request):
    if(request.method == 'POST'):
        cv = pickle.load(open('./transform.pkl', 'rb'))

        classifier = pickle.load(open('./nlp_model.pk','rb'))
        new_review = request.POST.get('review')
        new_review = re.sub('[^a-zA-Z]', ' ', new_review)
        new_review = new_review.lower()
        new_review = new_review.split()
        ps = PorterStemmer()
        all_stopwords = stopwords.words('english')
        all_stopwords.remove('not')
        new_review = [ps.stem(word) for word in new_review if not word in set(all_stopwords)]
        new_review = ' '.join(new_review)
        new_corpus = [new_review]
        new_X_test = cv.transform(new_corpus).toarray()
        new_y_pred = classifier.predict(new_X_test)
        print(new_y_pred)
        lis = []
        lis.append(request.POST.get('review'))
        print("value of list",lis)
        print(request.POST.get('review'),"value of request")
        return render(request, 'form_page.html',{"value":new_y_pred[0]})
    else:
        return HttpResponse('not post method')