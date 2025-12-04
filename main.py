from fastapi import FastAPI
from dotenv import load_dotenv
from Routes import root,chat

load_dotenv()

app = FastAPI()

app.include_router(root.router,prefix="",tags=["root"])
app.include_router(chat.router,prefix="",tags=["chat"])

