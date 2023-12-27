from fastapi import UploadFile
from openpyxl import load_workbook

from io import BytesIO
from functools import reduce
from typing import List, Dict

def convert_json(excel_file: UploadFile) -> Dict:
  excel_data = {
    'FileName': excel_file.filename,
    'Size': excel_file.size,
    'RowCount': 0,
    'Data': []
  }
  file_content = BytesIO(excel_file.file.read())
  workbook = load_workbook(file_content, read_only=True)
  
  total_rows = 0
  for sheet in workbook.worksheets:
    sheet_data = {
      'SheetName': sheet.title,
      'RowCount': sheet.max_row - 1,
      'Rows': []
    }
    total_rows += sheet.max_row - 1
    header_row = [cell.value.replace('_', '') for cell in sheet[1]]
    for row in sheet.iter_rows(min_row=2, values_only=True):
      row_data = [str(cell).strip() for cell in row]
      sheet_data['Rows'].append(dict(zip(header_row, row_data)))
    excel_data['Data'].append(sheet_data)
    
  excel_data['RowCount'] = total_rows
  return excel_data