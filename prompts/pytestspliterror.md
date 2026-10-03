running into attached error while running pytest
pytest tests/test_split.py
=========================================================== test session starts ============================================================
platform darwin -- Python 3.12.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/ga/cs690/Assignment-2/cs690-a2-ask-the-code
configfile: pytest.ini
plugins: anyio-4.15.1
collected 8 items                                                                                                                          

tests/test_split.py FFFFFFFF                                                                                                         [100%]

================================================================= FAILURES =================================================================
___________________________________________________ test_names_for_functions_and_methods ___________________________________________________

tmp_path = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_names_for_functions_and_m0')

    def test_names_for_functions_and_methods(tmp_path):
        path = write(tmp_path, "sample.py", SAMPLE)
>       assert [c.name for c in split_file(path, tmp_path)] == ["top", "Box.open", "Box.label"]
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_split.py:38: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_names_for_functions_and_m0/sample.py')
root = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_names_for_functions_and_m0')

    def split_file(path: Path, root: Path) -> list[Chunk]:
        """Return one Chunk for every function and method in the Python file at `path`.
    
        Rules. The tests check every one.
    
        1. Make a chunk for each `def` or `async def` that sits directly in the module,
           and for each `def` or `async def` that sits directly in a class that sits
           directly in the module. Nothing else becomes a chunk: not code outside
           functions, not a class with no methods, not a function nested inside another
           function, not a class nested inside a class, and not a function defined inside
           an `if`, `try`, `for`, `while` or `with` block at module level.
        2. name is the function name, or "ClassName.method_name" for a method.
        3. start_line is the line of the `def`, or the line of the first decorator if the
           function has decorators. end_line is the last line of the function.
           Both count from 1.
        4. text is exactly the source lines start_line to end_line, joined with "\\n".
           Split the file's text on "\\n" (not with str.splitlines) so your line numbers
           agree with the ones ast reports.
        5. file is the path of `path` relative to `root`, written with forward slashes,
           e.g. "sessions.py" or "sub/module.py".
        6. Return the chunks in the order they appear in the file.
    
        Hint: ast.parse(source) gives you a tree. tree.body lists the top-level
        statements. A function node has .name, .lineno, .end_lineno and .decorator_list,
        and each decorator node has its own .lineno. A class node has .name and .body.
        Read the file with encoding="utf-8".
        """
>       raise NotImplementedError("Step 2: write split_file in askcode/split.py")
E       NotImplementedError: Step 2: write split_file in askcode/split.py

askcode/split.py:43: NotImplementedError
_____________________________________________________ test_line_numbers_and_exact_text _____________________________________________________

tmp_path = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_line_numbers_and_exact_te0')

    def test_line_numbers_and_exact_text(tmp_path):
        path = write(tmp_path, "sample.py", SAMPLE)
>       top, box_open, _ = split_file(path, tmp_path)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_split.py:43: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_line_numbers_and_exact_te0/sample.py')
root = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_line_numbers_and_exact_te0')

    def split_file(path: Path, root: Path) -> list[Chunk]:
        """Return one Chunk for every function and method in the Python file at `path`.
    
        Rules. The tests check every one.
    
        1. Make a chunk for each `def` or `async def` that sits directly in the module,
           and for each `def` or `async def` that sits directly in a class that sits
           directly in the module. Nothing else becomes a chunk: not code outside
           functions, not a class with no methods, not a function nested inside another
           function, not a class nested inside a class, and not a function defined inside
           an `if`, `try`, `for`, `while` or `with` block at module level.
        2. name is the function name, or "ClassName.method_name" for a method.
        3. start_line is the line of the `def`, or the line of the first decorator if the
           function has decorators. end_line is the last line of the function.
           Both count from 1.
        4. text is exactly the source lines start_line to end_line, joined with "\\n".
           Split the file's text on "\\n" (not with str.splitlines) so your line numbers
           agree with the ones ast reports.
        5. file is the path of `path` relative to `root`, written with forward slashes,
           e.g. "sessions.py" or "sub/module.py".
        6. Return the chunks in the order they appear in the file.
    
        Hint: ast.parse(source) gives you a tree. tree.body lists the top-level
        statements. A function node has .name, .lineno, .end_lineno and .decorator_list,
        and each decorator node has its own .lineno. A class node has .name and .body.
        Read the file with encoding="utf-8".
        """
>       raise NotImplementedError("Step 2: write split_file in askcode/split.py")
E       NotImplementedError: Step 2: write split_file in askcode/split.py

askcode/split.py:43: NotImplementedError
___________________________________________________ test_decorator_line_starts_the_chunk ___________________________________________________

tmp_path = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_decorator_line_starts_the0')

    def test_decorator_line_starts_the_chunk(tmp_path):
        path = write(tmp_path, "sample.py", SAMPLE)
>       label = split_file(path, tmp_path)[2]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_split.py:52: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_decorator_line_starts_the0/sample.py')
root = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_decorator_line_starts_the0')

    def split_file(path: Path, root: Path) -> list[Chunk]:
        """Return one Chunk for every function and method in the Python file at `path`.
    
        Rules. The tests check every one.
    
        1. Make a chunk for each `def` or `async def` that sits directly in the module,
           and for each `def` or `async def` that sits directly in a class that sits
           directly in the module. Nothing else becomes a chunk: not code outside
           functions, not a class with no methods, not a function nested inside another
           function, not a class nested inside a class, and not a function defined inside
           an `if`, `try`, `for`, `while` or `with` block at module level.
        2. name is the function name, or "ClassName.method_name" for a method.
        3. start_line is the line of the `def`, or the line of the first decorator if the
           function has decorators. end_line is the last line of the function.
           Both count from 1.
        4. text is exactly the source lines start_line to end_line, joined with "\\n".
           Split the file's text on "\\n" (not with str.splitlines) so your line numbers
           agree with the ones ast reports.
        5. file is the path of `path` relative to `root`, written with forward slashes,
           e.g. "sessions.py" or "sub/module.py".
        6. Return the chunks in the order they appear in the file.
    
        Hint: ast.parse(source) gives you a tree. tree.body lists the top-level
        statements. A function node has .name, .lineno, .end_lineno and .decorator_list,
        and each decorator node has its own .lineno. A class node has .name and .body.
        Read the file with encoding="utf-8".
        """
>       raise NotImplementedError("Step 2: write split_file in askcode/split.py")
E       NotImplementedError: Step 2: write split_file in askcode/split.py

askcode/split.py:43: NotImplementedError
________________________________________________ test_file_is_relative_with_forward_slashes ________________________________________________

tmp_path = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_file_is_relative_with_for0')

    def test_file_is_relative_with_forward_slashes(tmp_path):
        path = write(tmp_path, "pkg/inner/mod.py", "def f():\n    pass\n")
>       assert split_file(path, tmp_path)[0].file == "pkg/inner/mod.py"
               ^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_split.py:59: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_file_is_relative_with_for0/pkg/inner/mod.py')
root = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_file_is_relative_with_for0')

    def split_file(path: Path, root: Path) -> list[Chunk]:
        """Return one Chunk for every function and method in the Python file at `path`.
    
        Rules. The tests check every one.
    
        1. Make a chunk for each `def` or `async def` that sits directly in the module,
           and for each `def` or `async def` that sits directly in a class that sits
           directly in the module. Nothing else becomes a chunk: not code outside
           functions, not a class with no methods, not a function nested inside another
           function, not a class nested inside a class, and not a function defined inside
           an `if`, `try`, `for`, `while` or `with` block at module level.
        2. name is the function name, or "ClassName.method_name" for a method.
        3. start_line is the line of the `def`, or the line of the first decorator if the
           function has decorators. end_line is the last line of the function.
           Both count from 1.
        4. text is exactly the source lines start_line to end_line, joined with "\\n".
           Split the file's text on "\\n" (not with str.splitlines) so your line numbers
           agree with the ones ast reports.
        5. file is the path of `path` relative to `root`, written with forward slashes,
           e.g. "sessions.py" or "sub/module.py".
        6. Return the chunks in the order they appear in the file.
    
        Hint: ast.parse(source) gives you a tree. tree.body lists the top-level
        statements. A function node has .name, .lineno, .end_lineno and .decorator_list,
        and each decorator node has its own .lineno. A class node has .name and .body.
        Read the file with encoding="utf-8".
        """
>       raise NotImplementedError("Step 2: write split_file in askcode/split.py")
E       NotImplementedError: Step 2: write split_file in askcode/split.py

askcode/split.py:43: NotImplementedError
________________________________________________ test_code_outside_functions_is_not_a_chunk ________________________________________________

tmp_path = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_code_outside_functions_is0')

    def test_code_outside_functions_is_not_a_chunk(tmp_path):
        path = write(tmp_path, "consts.py", "A = 1\nB = 2\n\nclass Empty:\n    pass\n")
>       assert split_file(path, tmp_path) == []
               ^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_split.py:64: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_code_outside_functions_is0/consts.py')
root = PosixPath('/private/var/folders/5q/4d4y9thn6fvd1szq1_j6kfk00000gn/T/pytest-of-ga/pytest-1/test_code_outside_functions_is0')

    def split_file(path: Path, root: Path) -> list[Chunk]:
        """Return one Chunk for every function and method in the Python file at `path`.
    
        Rules. The tests check every one.
    
        1. Make a chunk for each `def` or `async def` that sits directly in the module,
           and for each `def` or `async def` that sits directly in a class that sits
           directly in the module. Nothing else becomes a chunk: not code outside
           functions, not a class with no methods, not a function nested inside another
           function, not a class nested inside a class, and not a function defined inside
           an `if`, `try`, `for`, `while` or `with` block at module level.
        2. name is the function name, or "ClassName.method_name" for a method.
        3. start_line is the line of the `def`, or the line of the first decorator if the
           function has decorators. end_line is the last line of the function.
           Both count from 1.
        4. text is exactly the source lines start_line to end_line, joined with "\\n".
           Split the file's text on "\\n" (not with str.splitlines) so your line numbers
           agree with the ones ast reports.
        5. file is the path of `path` relative to `root`, written with forward slashes,
           e.g. "sessions.py" or "sub/module.py".
        6. Return the chunks in the order they appear in the file.
    
        Hint: ast.parse(source) gives you a tree. tree.body lists the top-level
        statements. A function node has .name, .lineno, .end_lineno and .decorator_list,
        and each decorator node has its own .lineno. A class node has .name and .body.
        Read the file with encoding="utf-8".
        """
>       raise NotImplementedError("Step 2: write split_file in askcode/split.py")
E       NotImplementedError: Step 2: write split_file in askcode/split.py

askcode/split.py:43: NotImplementedError
________________________________________________________ test_corpus_has_230_chunks ________________________________________________________

    def test_corpus_has_230_chunks():
>       assert len(split_corpus(CORPUS_DIR)) == 230
                   ^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_split.py:68: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

root = PosixPath('/Users/ga/cs690/Assignment-2/cs690-a2-ask-the-code/corpus/requests')

    def split_corpus(root: Path = CORPUS_DIR) -> list[Chunk]:
        """Return the chunks of every .py file under `root`, including subfolders.
    
        Process the files in order of their relative path, written with forward slashes
        and sorted as plain strings. Keep each file's chunks in file order.
        For the requests codebase this returns 230 chunks.
        """
>       raise NotImplementedError("Step 2: write split_corpus in askcode/split.py")
E       NotImplementedError: Step 2: write split_corpus in askcode/split.py

askcode/split.py:53: NotImplementedError
_________________________________________________________ test_corpus_known_method _________________________________________________________

    def test_corpus_known_method():
>       chunks = split_corpus(CORPUS_DIR)
                 ^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_split.py:72: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

root = PosixPath('/Users/ga/cs690/Assignment-2/cs690-a2-ask-the-code/corpus/requests')

    def split_corpus(root: Path = CORPUS_DIR) -> list[Chunk]:
        """Return the chunks of every .py file under `root`, including subfolders.
    
        Process the files in order of their relative path, written with forward slashes
        and sorted as plain strings. Keep each file's chunks in file order.
        For the requests codebase this returns 230 chunks.
        """
>       raise NotImplementedError("Step 2: write split_corpus in askcode/split.py")
E       NotImplementedError: Step 2: write split_corpus in askcode/split.py

askcode/split.py:53: NotImplementedError
__________________________________________________ test_corpus_order_is_by_file_then_line __________________________________________________

    def test_corpus_order_is_by_file_then_line():
>       chunks = split_corpus(CORPUS_DIR)
                 ^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_split.py:81: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

root = PosixPath('/Users/ga/cs690/Assignment-2/cs690-a2-ask-the-code/corpus/requests')

    def split_corpus(root: Path = CORPUS_DIR) -> list[Chunk]:
        """Return the chunks of every .py file under `root`, including subfolders.
    
        Process the files in order of their relative path, written with forward slashes
        and sorted as plain strings. Keep each file's chunks in file order.
        For the requests codebase this returns 230 chunks.
        """
>       raise NotImplementedError("Step 2: write split_corpus in askcode/split.py")
E       NotImplementedError: Step 2: write split_corpus in askcode/split.py

askcode/split.py:53: NotImplementedError
========================================================= short test summary info ==========================================================
FAILED tests/test_split.py::test_names_for_functions_and_methods - NotImplementedError: Step 2: write split_file in askcode/split.py
FAILED tests/test_split.py::test_line_numbers_and_exact_text - NotImplementedError: Step 2: write split_file in askcode/split.py
FAILED tests/test_split.py::test_decorator_line_starts_the_chunk - NotImplementedError: Step 2: write split_file in askcode/split.py
FAILED tests/test_split.py::test_file_is_relative_with_forward_slashes - NotImplementedError: Step 2: write split_file in askcode/split.py
FAILED tests/test_split.py::test_code_outside_functions_is_not_a_chunk - NotImplementedError: Step 2: write split_file in askcode/split.py
FAILED tests/test_split.py::test_corpus_has_230_chunks - NotImplementedError: Step 2: write split_corpus in askcode/split.py
FAILED tests/test_split.py::test_corpus_known_method - NotImplementedError: Step 2: write split_corpus in askcode/split.py
FAILED tests/test_split.py::test_corpus_order_is_by_file_then_line - NotImplementedError: Step 2: write split_corpus in askcode/split.py
============================================================ 8 failed in 0.05s ============================================================