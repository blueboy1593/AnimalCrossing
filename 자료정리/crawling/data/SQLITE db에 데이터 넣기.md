## 물고기

```python
from django.shortcuts import render
import openpyxl
from .models import Fish, Insect, Animal, Painting, Fossil

def excel_to_list(request):
    wb = openpyxl.load_workbook("./crawling/data/fossil.xlsx")
    ws = wb.active
    이름 = []
    가격 = []
    for r in ws.rows:
        이름. append(r[1].value)
        가격. append(r[2].value)
    for i in range(73):
        fossil = Fossil()
        fossil.name = 이름[i]
        fossil.price = 가격[i]
        fossil.save()
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
        fish.name = 이름[i]
        fish.month = 기간[i]
        fish.time = 시간[i]
        fish.size = 크기[i]
        fish.location = 장소[i]
        fish.price = 가격[i]
        fish.save()

    wb = openpyxl.load_workbook("./crawling/data/insect.xlsx")
    ws = wb.active
    이름 = []
    기간 = []
    시간 = []
    장소 = []
    가격 = []     
    for r in ws.rows:
        이름. append(r[1].value)
        기간. append(r[3].value)
        시간. append(r[4].value)
        장소. append(r[5].value)
        가격. append(r[6].value)
    for i in range(80):
        insect = Insect()
        insect.name = 이름[i]
        insect.month = 기간[i]
        insect.time = 시간[i]
        insect.location = 장소[i]
        insect.price = 가격[i]
        insect.save()

    wb = openpyxl.load_workbook("./crawling/data/animals.xlsx")
    ws = wb.active
    이름 = []
    영어이름 = []
    성별 = []
    생일 = []
    성격 = []
    종류 = []     
    for r in ws.rows:
        이름. append(r[1].value)
        영어이름. append(r[2].value)
        성별. append(r[3].value)
        생일. append(r[4].value)
        성격. append(r[5].value)
        종류. append(r[6].value)
    for i in range(391):
        animal = Animal()
        animal.name = 이름[i]
        animal.engname = 영어이름[i]
        animal.gender = 성별[i]
        animal.birthday = 생일[i]
        animal.personality = 성격[i]
        animal.sort = 종류[i]
        animal.save()
    wb = openpyxl.load_workbook("./crawling/data/painting.xlsx")
    ws = wb.active
    이름 = []
    영어이름 = []
    실제미술품 = []
    가품특징 = []
    for r in ws.rows:
        이름. append(r[1].value)
        영어이름. append(r[2].value)
        실제미술품. append(r[3].value)
        가품특징. append(r[4].value)
    for i in range(43):
        painting = Painting()
        painting.name = 이름[i]
        painting.engname = 영어이름[i]
        painting.real = 실제미술품[i]
        painting.memo = 가품특징[i]
        painting.save()
    return 
```

