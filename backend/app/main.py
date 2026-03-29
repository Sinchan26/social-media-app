from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.auth import auth
from app.api.v1.user import user

app=FastAPI()

app.include_router(auth.router)
app.include_router(user.router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "API is running"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run("app.main:app",reload=True)
