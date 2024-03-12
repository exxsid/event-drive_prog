from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
import random

from . import util


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Search Encyclopedia"}), label="")


class NewPageForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "File name"}), label="Title")

    content = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': "Enter your content here"}), label="Content")


class EditPageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': "Enter your content here"}), label="Content")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "search_form": SearchForm()
    })


def entry_page(request, title):
    edit_page_url = reverse("encyclopedia:edit_page", kwargs={"title": title})
    return render(request, "encyclopedia/entrypage.html", {
        "title": title,
        "entry": util.get_entry(title.upper()),
        "search_form": SearchForm(),
        "edit_page_url": edit_page_url
    })


def search_page(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data["search"]
            lists = util.list_entries()
            search_result = []

            for list in lists:
                if search.upper() in list.upper():
                    search_result.append(list)

            return render(request, "encyclopedia/searchpage.html", {
                "search_form": form,
                "search_result": search_result,
                "count": len(search_result)
            })
        else:
            return render(request, "encyclopedia/searchpage.html", {
                "search_form": SearchForm(),
                "search_result": None,
                "count": 0
            })

    return render(request, "encyclopedia/searchpage.html", {
        "search_form": SearchForm(),
        "search_result": None,
        "count": 0
    })


def create_new_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            # to check if title is already existing
            titles = util.list_entries()
            try:
                # when the title is not in list it will raise an exception
                # it will return the form again
                titles.index(title)

                return render(request, "encyclopedia/createnewpage.html", {
                    "new_page_form": form,
                    "search_form": SearchForm(),
                    "error_message": True
                })
            except:
                # when the title is not used
                util.save_entry(title, content)

                url = reverse("encyclopedia:entry_page",
                              kwargs={"title": title})

                return HttpResponseRedirect(url)

        else:
            return render(request, "encyclopedia/createnewpage.html", {
                "new_page_form": form,
                "search_form": SearchForm()
            })

    return render(request, "encyclopedia/createnewpage.html", {
        "new_page_form": NewPageForm(),
        "search_form": SearchForm()
    })


def edit_page(request, title):
    if request.method == "GET":  # when the request is come from the entry page
        edit_page_url = reverse("encyclopedia:edit_page",
                                kwargs={"title": title})

        entry = util.get_entry(title)

        if not entry:
            return render(request, "encyclopedia/editpage.html", {
                "search_form": SearchForm(),
                "not_found": True
            })

        return render(request, "encyclopedia/editpage.html", {
            "edit_page_form": EditPageForm(initial={"content": entry}),
            "search_form": SearchForm(),
            "url": edit_page_url
        })
    else:  # when the request is to save the entry
        form = EditPageForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data['content']

            # save the new entry
            util.save_entry(title, content)

            entry_page_url = reverse(
                "encyclopedia:entry_page", kwargs={"title": title})

            return HttpResponseRedirect(entry_page_url)

        else:
            return render(request, "encyclopedia/editpage.html", {
                "edit_page_form": EditPageForm(initial={"content": entry}),
                "search_form": SearchForm(),
                "url": edit_page_url
            })


def random_page(request):
    entries = util.list_entries()
    random_number = random.randint(0, len(entries) - 1)

    random_entry = entries[random_number]

    url = reverse("encyclopedia:entry_page", kwargs={"title": random_entry})

    return HttpResponseRedirect(url)
