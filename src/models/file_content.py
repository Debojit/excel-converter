from typing import List, Dict

from pydantic import BaseModel, Field

class FileData(BaseModel):
  sheet_name:str = Field(alias='SheetName')
  row_count:int = Field(alias='RowCount', default=0)
  rows:List[Dict] = Field(alias='Rows', default=[]) # Replace Dict with a model to make it sheet/excel-specific.

class FileContent(BaseModel):
  file_name:str = Field(alias='FieldName')
  file_size:int = Field(alias='Size', default=0)
  row_count:int = Field(alias='RowCount', default=0)
  file_data:FileData = Field(alias='Data', default=[])