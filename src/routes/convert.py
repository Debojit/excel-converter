from fastapi import APIRouter, UploadFile, status

from typing import Dict

from ..services.converters import convert_json
from ..models.file_content import FileContent

router = APIRouter(tags=['File Conversion'])
@router.post('/convert', name='Convert File and Return Data', status_code=status.HTTP_200_OK)
def convert(file: UploadFile) -> FileContent:
  data = convert_json(file)
  return data