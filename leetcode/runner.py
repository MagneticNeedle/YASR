import importlib
from pathlib import Path
import os

last_modified = max([file for file in Path.cwd().glob("*.py") if file.stem != "runner"],
                    key=lambda x: os.path.getctime(x.resolve()))

if __name__ == '__main__':
    solution_obj = importlib.import_module(last_modified.stem).Solution()
    functions = [i for i in dir(solution_obj) if "__" not in i and callable(getattr(solution_obj, i))]
    if functions:
        print(getattr(solution_obj, next(iter(functions)))(
            [[".","+"]]
            , [0,0]
        ))
