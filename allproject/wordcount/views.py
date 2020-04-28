from django.shortcuts import render

def wcmain(request):
    return render(request, "wcmain.html")

def result(request):
    text = request.GET["text"]
    word_dic = {}
    for word in text.split(" "):
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

    context = {
        "text": text,
        "splittext": text.split(" "),
        "word_dic":word_dic.items()
    }
    return render(request, "wcresult.html", context)