from django.shortcuts import render



import openpyxl
def excel_to_list(request):
    wb = openpyxl.load_workbook("./crawling/data/animals.xlsx")
    ws = wb.active
    for r in ws.rows:
        print(r[1].value)
    return 
