import importlib
from pathlib import Path
import os

last_modified = max([file for file in Path.cwd().glob("*.py") if file.stem != "runner"],
                    key=lambda x: os.path.getctime(x.resolve()))

if __name__ == '__main__':
    solution_obj = importlib.import_module(last_modified.stem).Solution()
    functions = [getattr(solution_obj, i) for i in dir(solution_obj) if "__" not in i and callable(getattr(solution_obj, i))]
    if functions:
        print(f"Running {last_modified.stem}\n")
        print(next(iter(functions))(
            [["5", "3", ".", ".", "7", ".", ".", ".", "."]
                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        ))
