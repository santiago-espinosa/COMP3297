
from django.shortcuts import redirect
from .models import *
from django.contrib import messages
from django.template import loader
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import *

def homepage(request):

    template = loader.get_template('pages/home.html')
    context = {}

    if request.method == 'POST':

        form = Homepage(request.POST)
        
        if form.is_valid():
            
            locations = Location.objects.filter(date_of_event__range=[form.cleaned_data["date_from_range"], form.cleaned_data["date_to_range"]])

            context.update({'locations': locations })
            context.update({'form': form})

            return HttpResponse(template.render(context, request))

        else:
            
            messages.error(request, "Invalid dates!")

    form = Homepage()
    locations = Location.objects.all()

    context.update({'form': form })
    context.update({'locations': locations})
    
    return HttpResponse(template.render(context, request))



def add_location(request):

    template = loader.get_template('pages/new_location.html')
    context={}

    if request.method == 'POST':
        form = New_location(request.POST)

        # check if the form is valid
        if form.is_valid():

            # Extract data from form
            name = form.cleaned_data['location_name']
            loc = form.cleaned_data['location']
            addr = form.cleaned_data['address']
            date = form.cleaned_data['date_of_event']
            description = form.cleaned_data['description_of_event']

            # Create new instance of model Case
            new_loc = Location(
                name=name,
                location=loc,
                address=addr,
                date_of_event=date,
                description_of_event=description,
            )

            #Try to save data
            try:
                new_loc.save()

            #Show error message if not saved successfully 
            except Exception as e:

                print(e)
                messages.error(request, "Internal server error! Please reload page.")

                context.update({'form': form})
                return HttpResponse(template.render(context, request))
            
            #Redirect to location_details if successfully added
            messages.success(request, "Details successfully saved.")
            return HttpResponseRedirect('/location/'+new_loc.name)

        # If form invalid, render this page w/ submitted details
        else:
            messages.error(request, "Please enter valid details.")
            context.update({'form': form})
            return HttpResponse(template.render(context, request))

    # If method is not POST, render this page w/ empty form
    form = New_location()
    context.update({'form': form})

    return HttpResponse(template.render(context, request))



def add_case(request):

    template = loader.get_template('pages/new_case.html')
    context={}

    if request.method == 'POST':
        form = New_case(request.POST)

        # check if the form is valid
        if form.is_valid():

            # Extract data from form
            name     = form.cleaned_data['case_name']
            num_case = form.cleaned_data['case_number']
            pid      = form.cleaned_data['personal_id']
            dob      = form.cleaned_data['date_of_birth']
            doo      = form.cleaned_data['date_of_onset']
            dot      = form.cleaned_data['date_of_test']
            event    = form.cleaned_data['case_event']

            # Create new instance of model Case
            new_case = Case(
                name=name,
                case_number=num_case,
                personal_id=pid,
                date_of_birth=dob,
                date_of_onset=doo,
                date_of_test=dot,
                event=event,
            )

            # Try to save data
            try:
                new_case.save()

            # If can't save data, handle and reload page w/ same details
            except Exception as e:
                print(e)
                messages.error(request, "Internal server error! Please reload page.")

                context.update({'form': form})
                return HttpResponse(template.render(context, request))
            
            # If successfully saved, redirect to case_details
            messages.success(request, "Details successfully saved.")
            return HttpResponseRedirect('/case/'+new_case.case_number)

        # If form is invalid show error message but keep details
        else:
            messages.error(request, "Please enter valid details.")
            context.update({'form': form})
            return HttpResponse(template.render(context, request))
    

    # Otherwise show render this page with empty form
    form = New_case()
    context.update({'form':form})

    return HttpResponse(template.render(context, request))



def location_details(request, loc_name):

    template = loader.get_template('pages/location_details.html')
    context = {}
    
    # we assume that there's only 1 location with the same name. Specified in Project req doc I think

    location    = Location.objects.filter(name = loc_name)[0] 
    cases       = Case.objects.filter(event__name__contains = loc_name)
    
    context.update({'location': location, 'cases': cases})

    return HttpResponse(template.render(context, request))



def case_details(request, case_num):
    
    template = loader.get_template('pages/case_details.html')
    context = {}

    try:
        case = Case.objects.get(case_number=case_num)
    except:
        messages.error(request, "Case not found!")
        return HttpResponse(template.render(context, request))

    context.update(case.get_details())

    return HttpResponse(template.render(context, request))



def proxy(request):
    return
