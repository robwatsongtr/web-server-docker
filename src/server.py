from fastapi import FastAPI, APIRouter
from typing import Annotated
from sqlmodel import Field, Session, SQLModel, create_engine, select
from contextlib import asynccontextmanager

app = FastAPI(
    title="Leetcode Problem Tracker API", openapi_url="/openapi.json"
)

# Used to group API endpoints 
api_router = APIRouter()

class Problem(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    lc_num: int
    problem_name: str
    problem_solution: str

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# A Session is what stores the objects in memory and keeps track of any changes
# needed in the data, then it uses the engine to communicate with the database.
def get_session():
    with Session(engine) as session:
        yield session

# setup the tables on startup 
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
