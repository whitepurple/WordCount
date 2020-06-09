from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    text = request.GET['fulltext']
    text_split = text.split(' ')
    wd = {}

    for w in text_split:
        if w in wd.keys():
            wd[w] += 1
        else:
            wd[w] = 1

    return render(request, 'count.html', {
                                            'length' : len(text_split),
                                            'full' : text_split,
                                            'text' : text,
                                            'dic' : wd.items(),
                                            })
