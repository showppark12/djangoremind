from django.shortcuts import render

def wcmain(request):
    return render(request, "wcmain.html")

def result(request):
    text = request.GET["text"]
    context = {
        "text": text,
        "splittext": text.split(" ")
    }
    return render(request, "wcresult.html", context)