from django.http import HttpResponseRedirect
from django.shortcuts import render

from main.forms import ModularCapsuleForm, ModulesFormSet
from main.models import Capsule, Module


def createModularCapsule(request):
    conversion_to_seconds = [60, 86400, 2592000, 31536000]
    if request.method == 'POST':
        form = ModularCapsuleForm(request.POST)
        formSet = ModulesFormSet(request.POST, request.FILES)
        if form.is_valid() and formSet.is_valid():
            #Datos de una cápsula
            title = form.cleaned_data["title"]

            emails = form.cleaned_data["emails"]
            capsule_type = "M"
            private = form.cleaned_data["private"]
            try:
                time_unit = int(form.cleaned_data['deadman_time_unit'])
                dead_man_switch = form.cleaned_data['deadman_switch']
                dead_man_counter = form.cleaned_data['deadman_counter'] * conversion_to_seconds[time_unit]
            except:
                dead_man_switch = False
                dead_man_counter = 0
                time_unit = 0
            price = 11.99
            twitter = form.cleaned_data['twitter']
            facebook = form.cleaned_data['facebook']
            capsule = Capsule.objects.create(title=title, emails=emails, capsule_type=capsule_type, private=private,
                                             dead_man_switch=dead_man_switch, dead_man_counter=dead_man_counter,
                                             dead_man_initial_counter=dead_man_counter, time_unit=time_unit,
                                             twitter=twitter, facebook=facebook,
                                             price=price)
            for moduleForm in formSet:
                description = moduleForm.cleaned_data['description']
                print(description)
                release_date = moduleForm.cleaned_data['release_date']
                module = Module.objects.create(description=description, release_date=release_date,
                                               capsule_id=capsule.id)

                print(moduleForm)
                print(request.FILES.getlist("form-0-file"))

            return HttpResponseRedirect('/displaycapsule/' + str(capsule.id))
    else:
        form = ModularCapsuleForm()
        formSet = ModulesFormSet()
        print(formSet.management_form)

    return render(request, 'form.html', {"form": form, "formset": formSet})
