from fastapi import FastAPI, APIRouter
from problems import PROBLEMS, Problem
from typing import Optional, Dict, List 

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
    return { "msg": "Server is Running!" }

@api_router.get("/lcproblems/", status_code=200)
def fetch_all_problems() -> Dict[str, List[Problem]]:
    """
    Fetch all Leetcode probelms
    """
    result = [ prob for prob in PROBLEMS]

    return { "results": result }

# FastAPI will use path parameter given the variable in path matching with function param
@api_router.get("/lcproblems/{problem_id}", status_code=200)
def fetch_problem(*, problem_id: int) -> Dict[str, List[Problem]]:
    """
    Fetch single Leetcode problem by ID
    """
    result = [ problem for problem in PROBLEMS if problem['id'] == problem_id ]

    return { "results": result } if result else { "results": [] }

# based on the func parameters and the lack of a variable in the path FastAPI will use query string
@api_router.get("/search/", status_code=200)
def search_problems( 
    keyword: Optional[str] = None, max_results: Optional[int] = 10 ) -> Dict[str, List[Problem]]:
    """
    Search for Leetcode problems based on name keyword
    """
    if not keyword: 
        return { "results": PROBLEMS[:max_results] }
    # filters based on condition of keyword matching in problem_name
    results = filter(lambda problem: keyword.lower() in problem['problem_name'].lower(), PROBLEMS)

    return { "results": list(results)[:max_results] }




# register the api router with the FastAPI object running the show 
app.include_router(api_router) 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, log_level="debug", reload=True)

