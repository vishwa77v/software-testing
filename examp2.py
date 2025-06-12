import ast
import re

def check_module_docstring(tree):
    return bool(ast.get_docstring(tree))

def check_function_docstrings(tree):
    return [(node.name, bool(ast.get_docstring(node)))
            for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

def check_function_names(tree):
    pattern = re.compile(r'^[a-z_][a-z0-9_]*$')
    return [node.name for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef) and not pattern.match(node.name)]

def check_indentation(lines):
    bad_lines = []
    for i, line in enumerate(lines):
        if not line.strip() or line.strip().startswith("#"):
            continue
        if '\t' in line or (len(line.expandtabs(4)) - len(line.lstrip())) % 4 != 0:
            bad_lines.append((i + 1, line.strip()))
    return bad_lines

def sqa_check(file_path):
    try:
        with open(file_path, "r") as f:
            code = f.read()
    except FileNotFoundError:
        print("❌ File not found.")
        return

    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        print(f"❌ Syntax error in code: {e}")
        return

    lines = code.splitlines()
    print("\n🔍 SQA Checklist:\n")

    # Docstrings
    print("📘 Documentation:")
    print(f" - Module docstring: {'✅' if check_module_docstring(tree) else '❌ Missing'}")
    for name, has_doc in check_function_docstrings(tree):
        print(f" - Function '{name}': {'✅' if has_doc else '❌ Missing docstring'}")

    # Naming
    print("\n🔤 Function Naming:")
    bad_names = check_function_names(tree)
    if bad_names:
        for name in bad_names:
            print(f" - ❌ '{name}' is not in snake_case")
    else:
        print(" - ✅ All function names are snake_case")

    # Indentation
    print("\n📏 Indentation:")
    bad_indent = check_indentation(lines)
    if bad_indent:
        for line_num, line in bad_indent:
            print(f" - ❌ Line {line_num}: {line}")
    else:
        print(" - ✅ Indentation looks good")

    print("\n✅ SQA Check Completed.\n")

if __name__ == "__main__":
    path = input("Enter path to Python file: ").strip()
    sqa_check(path)
