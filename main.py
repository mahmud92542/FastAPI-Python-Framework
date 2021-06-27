from fastapi import FastAPI

app = FastAPI()

@app.get('/') #path operation decorator #operation #path
#path operation function
def index():
    return {'data': {
        'name': 'blog list!'
    }
}
    

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