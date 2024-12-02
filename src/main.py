from fastapi import FastAPI, APIRouter
from problems import PROBLEMS
from typing import Optional

app = FastAPI(
    title="Leetcode Problem Tracker API", openapi_url="/openapi.json"
)

# Used to group API endpoints 
api_router = APIRouter()

# this is a decorator that registers the root function to define a GET endpoint.
@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET 
    """
    return { "msg": "Server is Running!"}

# the '*' in the parameter list means all parameters after it must be specified by name when called
@api_router.get("/lcproblems/{problem_id}", status_code=200)
def fetch_problem(problem_id: int) -> dict:
    """
    Fetch single Leetcode problem by ID
    """
    result = [ problem for problem in PROBLEMS if problem['id'] == problem_id ]
    if result:
        return result[0]
    
@api_router.get("/search/", status_code=200)
def search_problems( keyword: Optional[str] = None, max_results: Optional[int] = 10 ) -> dict:
    """
    Search for Leetcode problems based on name keyword
    """
    if not keyword: 
        return { "results": PROBLEMS[:max_results] }
    # filters based on condition of keyword matching in problem_name
    results = filter(lambda problem: keyword.lower() in problem['problem_name'].lower(), PROBLEMS)

    return { "results": list(results)[:max_results]}



# register the api router with the FastAPI object running the show 
app.include_router(api_router) 


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, log_level="debug", reload=True)

