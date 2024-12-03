from typing import Optional
from sqlmodel import SQLModel, Field

class Problem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    lc_num: int
    problem_name: str
    problem_solution: str