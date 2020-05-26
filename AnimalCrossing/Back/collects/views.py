from django.shortcuts import render
import openpyxl
from .models import Fish

def excel_to_list(request):
    wb = openpyxl.load_workbook("./crawling/data/fish.xlsx")
    ws = wb.active
    이름 = []
    기간 = []
    시간 = []
    장소 = []
    크기 = []
    가격 = []     
    for r in ws.rows:
        이름. append(r[1].value)
        기간. append(r[3].value)
        시간. append(r[5].value)
        장소. append(r[6].value)
        크기. append(r[7].value)
        가격. append(r[8].value)
    for i in range(80):
        fish = Fish()
        fish.fish_name = 이름[i]
        fish.fish_month = 기간[i]
        fish.fish_time = 시간[i]
        fish.fish_size = 크기[i]
        fish.fish_location = 장소[i]
        fish.fish_price = 가격[i]
        fish.save()
    return 
