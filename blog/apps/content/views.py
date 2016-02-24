from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from .models import Entrada

def main(request):
    entradas = Entrada.objects.all().order_by('-fecha')
    paginator = Paginator(entradas, 3 )

    try:
    	pagina =  int(request.GET.get('page','1'))
    except ValueError:
    	pagina = 1
    try:
    	entrada = paginator.page(pagina)
    except (InvalidPage, EmptyPage):
    	entrada = paginator.pagina(paginator.num_pages)

    return render_to_response('listado.html', dict(entrada = entrada , usuario = request.user))