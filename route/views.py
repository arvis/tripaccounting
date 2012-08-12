# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseServerError
from django.shortcuts import render_to_response, get_object_or_404
from route.models import Trip,TripForm
from django.template import RequestContext

def trip_list(request):
    latest_trips = Trip.objects.all()
    return render_to_response('index.html', {'latest_trips': latest_trips})

def trip_add(request):
    if request.method == 'POST': 
        form = TripForm(request.POST) 
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/') 
    else:
        form = TripForm()

    variables = RequestContext(request, {
        'form': form
    })
    
    return render_to_response('form.html', variables)    
    #return render_to_response(request, 'form.html', {'form': form,})    
    

def trip_edit(request,trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    if request.method == 'POST': 
        form = TripForm(request.POST, instance=trip ) 
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/') 

    else:
        form = TripForm(instance=trip ) 

    variables = RequestContext(request, {
        'form': form
    })
    
    return render_to_response('form.html', variables)    

