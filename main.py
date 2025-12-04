from fastapi import FastAPI
from dotenv import load_dotenv
from Routes import root

load_dotenv()

app = FastAPI()

app.include_router(root.router,prefix="",tags=["root"])


