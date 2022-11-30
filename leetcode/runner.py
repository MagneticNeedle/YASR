import importlib
from pathlib import Path
import os
from typing import Callable
import sys
import json

last_modified = max([file for file in Path(__file__).parent.glob("*.py") if file.stem != "runner"],
                    key=lambda x: os.path.getctime(x.resolve()))

if __name__ == '__main__':
    solution_obj = importlib.import_module(last_modified.stem).Solution()
    functions = [getattr(solution_obj, i) for i in dir(solution_obj) if
                 "__" not in i and callable(getattr(solution_obj, i))]
    if functions:
        func: Callable = next(iter(functions))
        print(f"Running function : {func.__name__} from file {last_modified.stem}\n")
        print(func(*[json.loads(i) for i in sys.argv[1:]]))
