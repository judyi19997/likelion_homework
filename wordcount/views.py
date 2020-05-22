from django.shortcuts import render

# Create your views here.

def wordcount(request):
    return render(request, 'wordcount.html')

def result(request):
    text = request.GET['fullText']
    words_list = text.replace("(", "").replace(")","").split()
    length = len(words_list)
    word_dict = {}
    number = 0
    for word in words_list:
        word = word.lower()
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word] = 1

    word_dict = sorted(word_dict.items(), reverse=True, key=lambda item: item[1])
    final_length = range(len(word_dict))
    # print(word_dict)
    # print(word_dict.keys())
    # key_list = list(word_dict.keys())
    # value_list = list(word_dict.values())
    # print(key_list)
    return render(request, 'result.html', {'text':text , 'words':words_list, 'length' : length,
    'word_dict': word_dict, 'final_length':final_length})

