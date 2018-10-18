from django.shortcuts import render
from productions.models import Production
from django.http import HttpResponse

# Create your views here.
def production_detail(request,production_id): #detail view
    production = Production.objects.get(id=production_id)
    response = render(request,'productions/production_detail.html',{
        'production':production
    })

    #return HttpResponse('%s</br>%s'%(production.name, production.description))
    return response

def production_list(request): #list view
    productions = Production.objects.all()
    output = 'Productions</br>'
    for p in productions:
        output+='%s. %s</br>'%(p.id,p.name)

    return HttpResponse(output)
