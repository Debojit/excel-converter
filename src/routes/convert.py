from fastapi import APIRouter, UploadFile, status

router = APIRouter(tags=['File Conversion'])
@router.post('/convert', name='Convert File and Return Data', status_code=status.HTTP_200_OK)
def convert(file: UploadFile):
  return file