from django.shortcuts import render
from django.shortcuts import get_object_or_404,HttpResponseRedirect

# Create your views here.

from .models import gateModel
from .forms import gateForm


def create_view(request):

    context = {}

    # add the dictionary during initialization
    form = gateForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    context = {}


    context["dataset"] = gateModel.objects.all()

    return render(request, "list_view.html", context)


def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = gateModel.objects.get(id=id)

    return render(request, "detail_view.html", context)


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(gateModel, id=id)

    # pass the object as instance in form
    form = gateForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(gateModel, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)