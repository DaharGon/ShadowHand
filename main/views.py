from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
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
        values = {}
        for i in siths:
            values[i.name]=Recruit.objects.filter(master=i).count()
        # sqlite не поддерживает distinct, поэтому так:
        siths_with_recruits = Recruit.objects.filter(master__isnull=False)
        siths_distinct = set()
        for i in siths_with_recruits:
            siths_distinct.add(i.master)
        return render(request, 'get_sith.html', {'siths':siths, 'siths_distinct':siths_distinct, 'values':values})
    elif request.method == 'POST':
        sith = Sith.objects.get(name=request.POST['siths'])
        return HttpResponseRedirect('/get_recruits/{id}'.format(id=sith.id))

def get_recruits(request, id, recid=False):
    if request.method == 'GET':
        recruits_all = Recruit.objects.filter(master__isnull=True)
        my_recruits = Recruit.objects.filter(master=Sith.objects.get(id=id))
        return render(request, 'get_recruit.html', {'recruits':recruits_all, 'my_recruits':my_recruits, 'sith':id})
    elif request.method == 'POST':
        try:
            # конечно тут лучше сделать отправку через Celery, но это будет в будущем по средствам интергалактичекской связи
            send_message(recid)
        except Exception:
            HttpResponse('Этот рекрут дефективный')
        sith = Sith.objects.get(id=id)
        recrut = Recruit.objects.get(id=recid)
        len_recruts = Recruit.objects.filter(master=sith).count()
        if len_recruts<=3:
            recrut.master = sith
            recrut.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('У вас уже есть 3 ученика в руке тени!')


def view_recrut_details(request, id):
    recrut = Recruit.objects.get(id=id)
    replys = Replys.objects.filter(recruit=recrut)
    return render(request, 'recrut_details.html', {'recrut':recrut, 'replys':replys})


def send_message(id):
    recruit = Recruit.objects.get(id=id)
    subject = 'Рука тени'
    message = '{name}, Вы зачислены в Руку тени'.format(name=recruit.name)
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recruit.email])
    return


