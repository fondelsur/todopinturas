# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse

from _compact import JsonResponse

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db import models

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
                    ['article_id', 'article_description', 'article_PVP', 'article_line1', 'article_line2', 'article_line3', 'article_line4']]
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
            excel = request.FILES['file']
            dict_values = excel.get_records()
            for value in dict_values:
                code = value.get('INTERNO', None)
                description = value.get('DESCRIPCION ARTICULO', None)
                pvp = value.get('PVP', None)
                dtol2 = value.get('Dto. L2', 0.0)
                if dtol2 == "":
                    dtol2 = 0.0
                netl2 = value.get('Neto', 0.0)
                if netl2 == "":
                    netl2 = 0.0
                dtol4 = value.get('Dto. L4', 0.0)
                if dtol4 == '':
                    dtol4 = 0.0
                netl4 = value.get('Neto', 0.0)
                if netl4 == '':
                    netl4 = 0.0
                offer1 = str(value.get('Oferta 30+3', 0))
                if offer1 == '':
                    offer1 = '0'
                offer2 = value.get('Oferta 29+4', 0.0)
                if offer2 == '':
                    offer2 = 0.0
                offer3 = str(value.get('Oferta 28+5', 0))
                if offer3 == '':
                    offer3 = '0'

                try:
                    item = Item.objects.get(article_id=code)
                    item.article_description = description
                    item.article_PVP = pvp
                    item.discount_l2 = dtol2
                    item.net_l2 = netl2
                    item.discount_l4 = dtol4
                    item.net_l4 = netl4
                    item.offer_303 = offer1
                    item.offer_294 = offer2
                    item.offer_285 = offer3
                    item.save()
                except Item.DoesNotExist:
                    item = Item.objects.create(article_id=code,
                                               article_description=description,
                                               article_PVP=pvp,
                                               discount_l2=dtol2,
                                               net_l2=netl2,
                                               discount_l4=dtol4,
                                               net_l4=netl4,
                                               offer_303=offer1,
                                               offer_294=offer2,
                                               offer_285=offer3
                                               )
            return HttpResponse("Se ha subido correctamente el archivo")
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
