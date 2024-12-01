from fastapi import FastAPI, APIRouter

app = FastAPI(
    title="Leetcode Problem Tracker API", openapi_url="/openapi.json"
)

# Used to group API endpoints 
api_router = APIRouter()

# this is a decorator that registers the root function to define a GET endpoint 
@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET 
    """
    return { "msg": "Server is Running!"}

# register the api router with the FastAPI object running the show 
app.include_router(api_router) 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")

