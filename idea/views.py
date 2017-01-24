from django.shortcuts import render, redirect
from django.contrib import auth
from idea.forms import IdeaForm
# Create your views here.
from idea.models import IdeaUser


def addIdea(request):

    args = {}
    args['username'] = auth.get_user(request).username
    args['form'] = IdeaForm()
    args['on'] = 0
    if request.POST:
        args['on'] = 1
        sort_idea = request.POST.get('sort', '')
        if sort_idea == 'name':
            args['ideas'] = IdeaUser.objects.order_by("idea_name")
            args['ideas_sort'] = 1
        sort_idea=request.POST.get('sort','')
        if sort_idea=='name':
            args['ideas'] = IdeaUser.objects.order_by("idea_name")
            args['ideas_sort'] =1
        else:
            args['ideas'] = IdeaUser.objects.order_by("idea_rank")
            args['ideas_sort'] = 2
        filtr_idea = request.POST.get('ideafiltr', '')
        filtr_idea=request.POST.get('ideafiltr','')
        try:
            args['ideas_filtr'] = IdeaUser.objects.filter(idea_rank=filtr_idea)
        except ValueError:
            args['ideas_filtr'] = IdeaUser.objects.filter(idea_rank=1)
        form = IdeaForm(request.POST)
        if form.is_valid():
            add_to_db = form.save(commit=False)
            add_to_db.idea_name = request.POST.get('ideaname', '')
            add_to_db.idea_text = request.POST.get('ideatext', '')
            try:
                add_to_db.idea_rank = request.POST.get('idearank', '')
            except ValueError:
                pass
            # idea.idea_author = request.user
            if add_to_db.idea_name != '' or add_to_db.idea_text !='' or add_to_db.idea_rank != '':
                add_to_db.save()
        else:
            form = IdeaForm()
            print("Валідація полів не пройдена")
    else:
        return render(request, 'addidea.html', args)
    return render(request, 'addidea.html', args)
        form=IdeaForm(request.POST)
        if form.is_valid():
            add_to_db=form.save(commit=False)
            add_to_db.idea_name=request.POST.get('ideaname','')
            add_to_db.idea_text =request.POST.get('ideatext','')
            add_to_db.idea_rank =request.POST.get('idearank','')
            #idea.idea_author = request.user
            add_to_db.save()
            return redirect('idea/')
        else:
            form = IdeaForm()
    else:
        return render(request, 'addidea.html',args)
    return render(request, 'addidea.html',args)

