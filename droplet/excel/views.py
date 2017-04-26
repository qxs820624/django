#encoding: utf-8

from django.shortcuts import render_to_response,render
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from _compact import JsonResponse
from django import forms
import django_excel as excel
#from excel.models import Question, Choice
from excel.models import * 
from clusterdbm.views import get_user_group

import xlrd, xlwt

# 设置GBK编码
xlrd.Book.encoding = "gbk"

data = [
    [1, 2, 3],
    [4, 5, 6]
]


class UploadFileForm(forms.Form):
    file = forms.FileField()

@login_required
# Create your views here.
def getExcel(request, employeeid):
    # 打开excel 
    workbook = xlrd.open_workbook(r'overtime.xls',formatting_info=True)
    print("codepage", workbook.codepage)
    print("colour_map", workbook.colour_map)
    print("countries", workbook.countries)
    print("user_name", workbook.user_name)
    print(len(workbook.xf_list))
    print(dir(workbook.xf_list))
    #print("xf_list") ## , workbook.xf_list
    #for xf in workbook.xf_list :
        #print(str(xf.dump()))
    print("format_list")  ## , workbook.format_list
    for f in workbook.format_list:
        print("format_key", f.format_key, "type", f.type, "format_str", f.format_str)
    #查看文件中包含sheet的名称：file.sheet_names()
    #得到第一个工作表，或者通过索引顺序 或 工作表名称
    #sheet = file.sheets()[0]
    #sheet = file.sheet_by_index(0)
    #sheet = file.sheet_by_name(u'Sheet1')
    
    for i in  range(workbook.nsheets) :
        sheet = workbook.sheet_by_index(i)
        print("number", sheet.number)
        print("colinfo_map.length", len(sheet.colinfo_map), "colinfo_map")
        print("width", "xf_index", "bit1_flag", "collapsed", "hidden", "outline_level")
        for index in sheet.colinfo_map:
            print(str((sheet.colinfo_map[index].width, sheet.colinfo_map[index].xf_index, sheet.colinfo_map[index].bit1_flag, sheet.colinfo_map[index].collapsed, sheet.colinfo_map[index].hidden, sheet.colinfo_map[index].outline_level)))
        #print("name", sheet.name)
        #print("col_label_ranges", sheet.col_label_ranges)
        #print("row_label_ranges", sheet.row_label_ranges)
        #print("visibility", sheet.visibility)
        #print("merged_cells", sheet.merged_cells)
        #print("rowinfo_map:") ## , sheet.rowinfo_map
        #print("height", "has_default_height", "outline_level", "outline_group_starts_ends", "hidden", "height_mismatch", "has_default_xf_index", "xf_index", "additional_space_above", "additional_space_below")
        #for index in sheet.rowinfo_map:
            #print(str(sheet.rowinfo_map[index].__getstate__()))
        #获取行数和列数
        #nrows = sheet.nrows
        #ncols = sheet.ncols
        rows, cols = sheet.nrows, sheet.ncols
        print("Number of rows: %s Number of cols: %s" % (rows, cols))
        for row in range(rows):
            for col in range(cols):
                thecell = sheet.cell(row, col)  # could get 'dump', 'value', 'xf_index'
                #print("row, col is:", row+1, col+1, "value:", thecell.value, "ctype:", thecell.ctype, "xf_index", thecell.xf_index)
                #http://www.th7.cn/Program/Python/2011/11/20/47240.shtml
                #ctype xlrd.XL_CELL_TEXT(Text 文本),xlrd.XL_CELL_NUMBER(Number 数字),xlrd.XL_CELL_DATE(Date 日期),xlrd.XL_CELL_BOOLEAN(Boolean 布尔值), xlrd.XL_CELL_ERROR(Error 错误)xlrd.XL_CELL_EMPTY(空值),XL_CELL_BLANK(空字符串)
                #提供的xldate_as_tuple方法把日期单元格中的float数转化为适合实例化各种日期或时间对象的元组。
                # date_value =xldate_as_tuple(sheet.cell(3,2).value,workbook.datemode)
                # print(datetime(*date_value),date(*date_value[:3]))
                # error_text_from_code方法用来把错误代码转换为错误信息：print(error_text_from_code[sheet.cell(5,2).value])
                #print("cell_type:", sheet.cell_type(row, col),"cell_value:", sheet.cell_value(row, col))
                #以下获取颜色
                xfx = sheet.cell_xf_index(row, col)
                xf = workbook.xf_list[xfx]
                bgx = xf.background.pattern_colour_index
                #print("bgx:", bgx)
        #获取整行和整列的值（数组）
        #sheet.row_values(i)
        #sheet.col_values(i)
        #单元格（索引获取）
        #cell_A1 = sheet.cell(0,0).value
        #cell_C4 = sheet.cell(2,3).value
        #分别使用行列索引
        #cell_A1 = sheet.row(0)[0].value
        #cell_A2 = sheet.col(1)[0].value
        #这里使用了csrf_token所以必须使用render，带上request, 否则会报错
        """
        Forbidden (403)
        CSRF verification failed. Request aborted
        """
        return render(request, "cdyd.html")
        #return render_to_response("cdyd.html")
    
def upload(request):
    group = get_user_group(request)
    user = request.user    
    return render(
        request,
        'cdyd.html',
        {'group':group, 'user': user, 'sheets': None})
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
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        })


def download(request, file_type):
    sheet = excel.pe.Sheet(data)
    return excel.make_response(sheet, file_type)


def download_as_attachment(request, file_type, file_name):
    return excel.make_response_from_array(
        data, file_type, file_name=file_name)


#def export_data(request, atype):
    #if atype == "sheet":
        #return excel.make_response_from_a_table(
            #Question, 'xls', file_name="sheet")
    #elif atype == "book":
        #return excel.make_response_from_tables(
            #[Question, Choice], 'xls', file_name="book")
    #elif atype == "custom":
        #question = Question.objects.get(slug='ide')
        #query_sets = Choice.objects.filter(question=question)
        #column_names = ['choice_text', 'id', 'votes']
        #return excel.make_response_from_query_sets(
            #query_sets,
            #column_names,
            #'xls',
            #file_name="custom"
        #)
    #else:
        #return HttpResponseBadRequest(
            #"Bad request. please put one of these " +
            #"in your url suffix: sheet, book or custom")


#def import_data(request):
    #if request.method == "POST":
        #form = UploadFileForm(request.POST,
                              #request.FILES)

        #def choice_func(row):
            #q = Question.objects.filter(slug=row[0])[0]
            #row[0] = q
            #return row
        #if form.is_valid():
            #request.FILES['file'].save_book_to_database(
                #models=[Question, Choice],
                #initializers=[None, choice_func],
                #mapdicts=[
                    #['question_text', 'pub_date', 'slug'],
                    #['question', 'choice_text', 'votes']]
            #)
            #return HttpResponse("OK", status=200)
        #else:
            #return HttpResponseBadRequest()
    #else:
        #form = UploadFileForm()
    #return render(
        #request,
        #'upload_form.html',
        #{
            #'form': form,
            #'title': 'Import excel data into database example',
            #'header': 'Please upload sample-data.xls:'
        #})


def import_sheet(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                name_columns_by_row=2,
                #model=Question,
                model= Sheet,
                mapdict=['question_text', 'pub_date', 'slug'])
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
