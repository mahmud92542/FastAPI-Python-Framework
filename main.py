from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/') #path operation decorator #operation #path
#path operation function
def index(limit,publish:bool, sort:Optional[str] = None): #query parameter
    if publish:
        return {'data': {'name': f'{limit} publish blog list!'}}
    else:
        return {'data': {'name': f'{limit} blog list!'}}
    

@app.get('/blog/{id}') #path operation decorator #operation #path
#path operation function
def about(id):
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{
        '2','3'
    }}
    
@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}