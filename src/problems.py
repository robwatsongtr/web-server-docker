from typing import List, TypedDict

class Problem(TypedDict):
    id: int
    lc_num: int
    problem_name: str
    problem_solution: str

PROBLEMS: List[Problem] = [
    {
        'id': 1,
        'lc_num': 27,
        'problem_name': "Remove Element",
        'problem_solution': ("""initi left pointer to 0. start for loop with right pointer at 0: if right is the value, skip it and loop to next element ( 'continue' loop), if it's different than value, copy right to left. return left. """).strip()
    },
    {
        'id': 2,
        'lc_num': 55,
        'problem_name': "Jump Game",
        'problem_solution': ("""init furthest to 0. for i in range len nums, first check if current i is greater than furthest, you're stuck so return false. Calculate furthest as the max of current furthest or the value of current index plus the index itself. If furthest is greater than or equal to THE LAST INDEX  return true """)
    },
    {
        'id': 3,
        'lc_num': 49,
        'problem_name': "Group Anagrams",
        'problem_solution': ("""init a hashmap. For word in strs: sort word with "".join(sorted(s)), if sorted word not in hashmap, put it there with an empty array as value. Otherwise every time look up sorted str and append its raw unsorted version from strs array. Outside loop return a list of the hashmap.values""")
    }
]