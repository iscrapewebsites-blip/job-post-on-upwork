import json
from openpyxl import Workbook
from openpyxl.styles.fonts import Font

data_str = ''
with open('jobs.json', 'r', encoding='utf-8') as f:
     data_str = f.read()

data = json.loads(data_str)

header = list(data[0].keys())
grand_data = [list(record.values()) for record in data]
grand_data.insert(0, header)

wb = Workbook()
ws = wb.active

for row in grand_data:
     ws.append(row)

for cell in ws['1']:
     cell.font = Font(bold=True)

wb.save('upwork_jobs.xlsx')