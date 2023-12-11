from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from entities import ProductInfo
from validate import validateProduct

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
def productInfo(product: ProductInfo):
    result = validateProduct(product)
    print(result)
    return result
