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

            # user = authenticate(first_name=first_name, last_name=last_name)

            # if user:
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


# # @login_required(login_url='info:login')
# def blood_entry(request):
#     if request.method == "POST":
#         # user = request.user
#         blood_record = BloodRecord
#         form1 = BloodRecordForm(data=request.POST)
#         form2 = UserInfoForm(data=request.POST)
#         if form1.is_valid():
#             blood_group = form1.cleaned_data['blood_group']
#             if request.user.is_authenticated:
#                 u = get_object_or_404(UserInfo, pk=request.user.id)
#                 blood_record.user = u
#                 blood_record.blood_group = blood_group
#
#                 blood_record.save()
#                 return redirect('info:home')
#         else:
#             # print("Error!!!")
#             return redirect('info:blood-entry')
#
#     elif request.method == "GET":
#         form1 = BloodRecordForm()
#         form2 = UserInfoForm()
#         context = {
#             'form1': form1,
#             'form2': form2
#         }
#         # print("GETTING")
#         return render(request, "info/add_blood_record.html", context=context)
#     # if request.method == "POST":
#     #     # user = request.user
#     #     blood_record = BloodRecord
#     #     form1 = BloodRecordForm(data=request.POST)
#     #     form2 = UserInfoForm(data=request.POST)
#     #
#     #     if request.session[request.user.username]:
#     #         blood_record.user = UserInfo.get(username__iexact=request.POST.user.username)
#     #
#     #     # print(user.username)
#     #
#     #     if form1.is_valid():
#     #         blood_group = form1.cleaned_data['blood_group']
#     #
#     #         # first_name = form2.cleaned_data['first_name']
#     #         # last_name = form2.cleaned_data['last_name']
#     #         # username = form2.cleaned_data['username']
#     #         # password = form2.cleaned_data['password']
#     #         # sex = form2.cleaned_data['sex']
#     #         # location = form2.cleaned_data['location']
#     #
#     #         # blood_record = form1.save()
#     #         # user_info = form2.save()
#     #         #
#     #         # user_info.set_password(password)
#     #         # blood_record.save()
#     #         # user_info.save()
#     #         # blood_record.user = user
#     #         blood_record.blood_group = blood_group
#     #         blood_record.save()
#     #         return redirect('info:home')
#     #     else:
#     #         # print("Error!!!")
#     #         return redirect('info:blood-entry')
#     #
#     # elif request.method == "GET":
#     #     form1 = BloodRecordForm()
#     #     form2 = UserInfoForm()
#     #     context = {
#     #         'form1': form1,
#     #         'form2': form2
#     #     }
#     #     # print("GETTING")
#     #     return render(request, "info/add_blood_record.html", context=context)
#
#
# def login_user(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = UserInfo.objects.filter(username__iexact=username, password__iexact=password)
#
#             if user:
#                 user = authenticate(username=username, password=password)
#                 login(request, user)
#                 # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#                 # return redirect('info:blood-entry')
#                 return HttpResponseRedirect(reverse('info:blood-entry'))
#
#         else:
#             message = "Wrong Username or Password"
#             return redirect('info:login')
#
#     elif request.method == 'GET':
#         form = LoginForm
#         context = {
#             'form': form
#         }
#         return render(request, 'info/donor_login.html', context=context)
