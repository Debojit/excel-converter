from fastapi import FastAPI

from .routes import convert

api_version:str = '1.0'
api_root:str = f'/convert-excel/{api_version}'
app_description = '''
API to convert Excel file to JSON. Consuming applications upload am Excel file and receive a JSON payload of the contents.
**Supported Operations:**
* **Convert File**
'''

app = FastAPI(title='Excel Converter',
              description=app_description,
              summary='Excel file conversion API',
              version=api_version,
              contact={
                'name': 'Debojit Sinha',
                'email': 'tahecef461@gyxmz.com'
              },
              license_info={
                'name': 'Apache 2.0',
                'identifier': 'Apache-2.0',
              },
              prefix=api_root)

app.include_router(convert.router, prefix=api_root)
