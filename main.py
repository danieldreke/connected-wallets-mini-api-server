# source: https://dev.to/arctype/deploy-a-python-api-on-vercel-using-postgres-4871
from fastapi import FastAPI
app = FastAPI()

users = dict()

@app.get("/")
def read_root():
    return {"message": "Server is up and running!"}

@app.post("/user")
async def add_or_update_user(userpubkey: str):
    if userpubkey not in users:
        users[userpubkey] = 0
    else:
        users[userpubkey] += 1
    counter = users[userpubkey]
    print(counter, userpubkey)
    return users