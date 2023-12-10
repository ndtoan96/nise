from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from entities import ProductInfo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"hello": "world"}

@app.post("/productInfo")
def productInfo(body: ProductInfo):
    print(body)
