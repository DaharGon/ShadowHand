from django.shortcuts import render, HttpResponseRedirect
from main.forms import RecruitForm, SelectSith
from main.models import Planet, Questions, Recruit, Replys, Sith


def main(request):
    return render(request, 'main.html')


def set_recruit(request):
    if request.method == 'GET':
        form = RecruitForm()
        form.fields['planet'].queryset=Planet.objects.all()
        return render(request, 'set_recruit.html', {'form':form})
    elif request.method == 'POST':
        form = RecruitForm(request.POST)
        if form.is_valid():
            a = form.save()
            return HttpResponseRedirect('/questions/{id}'.format(id=a.id))

def questions(request, id):
    recruit = Recruit.objects.get(id=id)
    allquestions = Questions.objects.all()
    if request.method=='GET':
        return render(request, 'replys.html', {'recruit':recruit, 'allquestions':allquestions})
    elif request.method=='POST':
        print(request.POST)
        for i in allquestions:
            try:
                print(request.POST.keys())
                if str(i.id) in request.POST.keys():
                    newreplay = Replys(recruit=recruit, question=i, answer=1)
                    newreplay.save()
                else:
                    newreplay = Replys(recruit=recruit, question=i, answer=0)
                    newreplay.save()
            except Exception:
                continue
        return HttpResponseRedirect('/')


def get_sith(request):
    if request.method == 'GET':
        siths = Sith.objects.all()
        return render(request, 'get_sith.html', {'siths':siths})
    elif request.method == 'POST':
        sith = Sith.objects.get(name=request.POST['siths'])
        return HttpResponseRedirect('/get_recruits/{id}'.format(id=sith.id))

def get_recruits(request, id):
    recruits = Recruit.objects.filter(master__isnull=True)
    return render(request, 'get_recruit.html', {'recruits':recruits})

def view_recrut_details(request, id):
    recrut = Recruit.objects.get(id=id)
    print(recrut)
    replys = Replys.objects.filter(recruit=recrut)
    print(replys)
    return render(request, 'recrut_details.html', {'recrut':recrut, 'replys':replys})

