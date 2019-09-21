from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth import authenticate
from .forms import BloodInfoForm
from .models import BloodInfo


def index(request):
    all_blood_info = BloodInfo.objects.all()
    if request.method == 'POST':
        query = request.POST.get('query')
        if query == 'Male':
            query = 'M'
        elif query == 'Female':
            query = 'F'

        all_blood_info = all_blood_info.filter(
            Q(blood_group__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(location__icontains=query) |
            Q(age__iexact=query) |
            Q(sex__icontains=query)
        ).distinct()
    context = {
        'all_blood_info': all_blood_info
    }
    return render(request, 'info/all_blood_records.html', context=context)


def blood_entry(request):
    if request.method == "POST":
        donor_form = BloodInfoForm(data=request.POST)
        # print(request.POST)
        if donor_form.is_valid():
            first_name = donor_form.cleaned_data['first_name']
            last_name = donor_form.cleaned_data['last_name']
            sex = donor_form.cleaned_data['sex']
            age = donor_form.cleaned_data['age']
            location = donor_form.cleaned_data['location']
            donor_form.save()

            return redirect('info:blood-entry')

        else:
            print(donor_form.errors)
            return redirect('info:blood-entry')
        print("POSTING")
    else:
        form = BloodInfoForm
        context = {
            'form': form
        }
        print("GETTING")
        return render(request, "info/add_donor.html", context=context)

