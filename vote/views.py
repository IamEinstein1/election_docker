from django.shortcuts import render
from .models import ASPL, SPL
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate


def index(request):
    global spl_done
    global aspl_done
    spl_done = False
    aspl_done = False
    candidates = SPL.objects.all()
    return render(request, 'vote/index.html', context={"candidates": candidates})


def spl(request):
    if request.method == "GET":
        return render(request, "vote/error.html", context={"text": "Invalid method", "type": "primary"})
    else:
        global spl_done
        global aspl_done
        try:
            selected_candidate = SPL.objects.get(pk=request.POST['SPL'])
        except(KeyError, SPL.DoesNotExist):
            candidates = SPL.objects.all()
            error = "You have not selected a candidate."
            return render(request, 'vote/index.html', {'candidates': candidates, 'error_message': error})
        else:
            selected_candidate.votes += 1
            selected_candidate.save()
            spl_done = True
            return HttpResponseRedirect(reverse('voting:voted'))


def aspl(request):
    if request.method == "GET":
        return render(request, "vote/error.html", context={"text": "Invalid method", "type": "info"})
    else:
        global aspl_done
        try:
            selected_candidate = ASPL.objects.get(pk=request.POST['ASPL'])
        except(KeyError, ASPL.DoesNotExist):
            candidates = ASPL.objects.all()
            error = "You have not selected a candidate"
            return render(request, 'vote/voted.html', {'candidates': candidates, 'error_message': error})
        else:
            selected_candidate.votes += 1
            selected_candidate.save()
            aspl_done = True
            return HttpResponseRedirect(reverse('voting:thanks'))


def voted(request):
    global spl_done
    global aspl_done
    try:
        if spl_done == False:
            return render(request, "vote/index.html", context={"candidates": SPL.objects.all()})
        elif aspl_done == False:
            return render(request, "vote/voted.html", context={"candidates": ASPL.objects.all()})
        elif spl_done == True and aspl_done == True:
            return render(request, "vote/thanks.html")
        else:
            return HttpResponse("<h1>Some Server Error</h1>")
    except(ValueError, NameError):
        return render(request, "vote/error.html", context={"text": "Invalid method", "type": "info"})

    # candidates = ASPL.objects.all()
    # return render(request, 'vote/voted.html', context={"candidates": candidates})


def thanks(request):
    global spl_done
    global aspl_done
    spl_done = False
    aspl_done = False
    return render(request, 'vote/thanks.html')


def result(request):
    if request.method == "GET":
        return render(request, "vote/error.html", context={"type": "danger", "text": "You are not authorized to see the results"})
    elif request.method == "POST":

        aspl_can = ASPL.objects.order_by('-votes')[:]
        spl_can = SPL.objects.order_by('-votes')[:]
        password = request.POST['password']
        username = request.POST['username']
        user = authenticate(username=username, password=password)
        if user != None:
            return render(request, "vote/result.html", context={"spl_can": spl_can, "aspl_can": aspl_can})
        else:
            return render(request, "vote/error.html", context={"type": "danger", "text": "You are not authorized to see the results"})


def login(request):
    return render(request, "vote/login.html")


# logic for :
#       quitting in between
num = 1


def logic(request):
    global num
    if num == 1:
        num += 1
        print(num)
        return HttpResponseRedirect(reverse("voting:index"))
    else:
        global spl_done
        global aspl_done
        if spl_done == False:
            return render(request, "vote/index.html", context={"candidates": SPL.objects.all()})
        elif aspl_done == False:
            return render(request, "vote/voted.html", context={"candidates": ASPL.objects.all()})
        elif spl_done == True and aspl_done == True:
            return render(request, "vote/thanks.html")
        else:
            return HttpResponse("<h1>Some Server Error</h1>")