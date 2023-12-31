from turtle import title
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# import data
from data.offer import offers
from data.company import companies
from data.user import users


app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)

# CORSミドルウェアを有効にする
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://kosen-intercollegiate-ynori123s-projects.vercel.app", "http://kosen-intercollegiate-ynori123s-projects.vercel.app", "https://kosen-intercollegiate.vercel.app", "http://localhost:3000"],  # 許可するオリジンを指定
    allow_credentials=True,
    allow_methods=["*"],  # 許可するHTTPメソッドを指定（"*"はすべてのメソッドを許可）
    allow_headers=["*"],  # 許可するヘッダーを指定（"*"はすべてのヘッダーを許可）
)
app.mount("/img", StaticFiles(directory="img"), name="img")


@app.get("/offers")
async def get_offers():
    return {
    "code" : 0,
    "data" : {
        "page" : 1,
        "totalPage" : 1,
        "offers" : offers
        }
    }

@app.get("/offer/{offer_id}")
async def get_offer(offer_id: str):
    offer = {}
    for item in offers:
        if item["id"] == offer_id:
            return {
            "code" : 0,
            "data" : {
                "offer" : item
                }
            }
    return {}
    
@app.get("/companies")
async def get_companies():
    return {
    "code" : 0,
    "data" : {
        "page" : 1,
        "totalPage" : 1,
        "companies" : companies
        }
    }

@app.get("/company/{company_id}")
async def get_company(company_id: str):
    for item in companies:
        if item.get("id") == company_id:
            return {
                "code" : 0,
                "data" : {
                    "company" : item
                }
            }
    return {
        "code" : 1,
        "data" : {}
    }
    
class LoginShema(BaseModel):
    email: str
    password: str

@app.post("/login")
async def login(data: LoginShema):
    for user in users:
        if user.get("email") == data.email and user.get("password") == data.password:
            return {
                "code" : 0,
                "token" : user.get("token")
                
            }
    return {
        "code" : 1,
        "token" : ""
    }
