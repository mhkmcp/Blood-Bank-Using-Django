from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    return render(request, 'info/all_blood_records.html')