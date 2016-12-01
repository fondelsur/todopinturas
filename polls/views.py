from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse

from _compact import JsonResponse

from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

import django_excel as excel

from polls.models import Question, Choice, Item

from .forms import UploadFileForm


data = [
    [1, 2, 3],
    [4, 5, 6]
]
# Create your views here.+


class IndexWithSearch(ListView):
    """
    Main view to get search and results in
    the index.
    """
    model = Item
    template_name = "todopinturas.html"
    context_object_name = "consulta"

    def get_queryset(self):
        search_string = self.request.GET.get('id', None)
        if search_string:
            qs = self.model.objects.filter(article_id__contains=search_string)
            if qs.exists():
                return qs
        search_string = self.request.GET.get('description', None)
        if search_string:
            qs = self.model.objects.filter(article_description__contains=search_string)
            if qs.exists():
                return qs
        return []


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",
                                       file_name="download")
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Todo Pinturas S.L.',
            'header': ('Introduzca el archivo excel a subir en  ' +
                       'la base de datos:')
        })


def download(request, file_type):
    sheet = excel.pe.Sheet(data)
    return excel.make_response(sheet, file_type)


def download_as_attachment(request, file_type, file_name):
    return excel.make_response_from_array(
        data, file_type, file_name=file_name)


def export_data(request, atype):
    if atype == "sheet":
        return excel.make_response_from_a_table(
            Item, 'xls', file_name="sheet")
    elif atype == "book":
        return excel.make_response_from_tables(
            [Question, Choice], 'xls', file_name="book")
    elif atype == "custom":
        question = Question.objects.get(slug='ide')
        query_sets = Choice.objects.filter(question=question)
        column_names = ['choice_text', 'id', 'votes']
        return excel.make_response_from_query_sets(
            query_sets,
            column_names,
            'xls',
            file_name="custom"
        )
    else:
        return HttpResponseBadRequest(
            "Bad request. please put one of these " +
            "in your url suffix: sheet, book or custom")


def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)

        def choice_func(row):
            q = Question.objects.filter(slug=row[0])[0]
            row[0] = q
            return row
        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models=[Item],
                initializers=[None, choice_func],
                mapdicts=[
                    ['article_id', 'article_description','article_PVP', 'article_line1', 'article_line2', 'article_line3', 'article_line4']]
            )
            return HttpResponse("OK", status=200)
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        })


@login_required
def import_sheet(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                # name_columns_by_row=2,
                model=Item,
                mapdict=(['article_id', 'article_description', 'article_PVP', 'article_line1', 'article_line2', 'article_line3', 'article_line4']))
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {'form': form})


def exchange(request, file_type):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        filehandle = request.FILES['file']
        return excel.make_response(filehandle.get_sheet(), file_type)
    else:
        return HttpResponseBadRequest()


def parse(request, data_struct_type):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        filehandle = request.FILES['file']
        if data_struct_type == "array":
            return JsonResponse({"result": filehandle.get_array()})
        elif data_struct_type == "dict":
            return JsonResponse(filehandle.get_dict())
        elif data_struct_type == "records":
            return JsonResponse({"result": filehandle.get_records()})
        elif data_struct_type == "book":
            return JsonResponse(filehandle.get_book().to_dict())
        elif data_struct_type == "book_dict":
            return JsonResponse(filehandle.get_book_dict())
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()
