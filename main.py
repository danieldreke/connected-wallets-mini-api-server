# source: https://dev.to/arctype/deploy-a-python-api-on-vercel-using-postgres-4871
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

ORIGINS = "http[s]*://(localhost|127.0.0.1)(:[0-9]{1,5})?"

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origin_regex=ORIGINS, allow_methods=['GET', 'POST'])

users = dict()

@app.get("/")
def read_root():
    return {"message": "Server is up and running!"}

@app.post("/user")
async def add_or_update_user(userpubkey: str):
    if userpubkey not in users:
        users[userpubkey] = 1
    else:
        users[userpubkey] += 1
    counter = users[userpubkey]
    print(counter, userpubkey)
    return users