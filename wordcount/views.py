from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    text = request.GET['fullText']
    words_list = text.split()
    # for word in words_list:
    #     if word in '(':
    #         word = word[1:]
    #         print(word)
    length = len(words_list)
    word_dict = {}
    for word in words_list:
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word] = 1
    return render(request, 'result.html', {'text':text , 'words':words_list, 'word_dict':word_dict.items(), 'length':length})

