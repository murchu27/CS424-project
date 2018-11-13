from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from productions.models import Production
from productions.forms import ProductionForm

def production_detail(request,production_id): #detail view
    production = Production.objects.get(id=production_id)
    return render(request,'productions/production_detail.html',{
        'production':production
    })


def production_list(request): #list view
    productions = Production.objects.all()
    return render(request,'productions/production_list.html', {
        'productions':productions
    })


@login_required
def production_update(request,production_id):
    production = Production.objects.get(id=production_id)
    if request.user != production.owner:#prevent users that don't own this production instance from updating it
        return render(request,'productions/production_update_denied.html', {
            'production':production                
        })
    if request.method == "POST":
        form = ProductionForm(request.POST, instance=production)
        if form.is_valid():
            form.save() #update current production object in db
            return HttpResponseRedirect(reverse('production_detail',kwargs={'production_id':production_id})) 
        else:
            return HttpResponseRedirect('/')
    form = ProductionForm(instance=production)
    return render(request,'productions/production_update.html', {
        'form':form
    })

