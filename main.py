# source: https://dev.to/arctype/deploy-a-python-api-on-vercel-using-postgres-4871
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is up and running!"}