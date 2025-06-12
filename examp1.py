import ast

class ComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.decision_points = 0

    def visit_If(self, node):
        self.decision_points += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.decision_points += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.decision_points += 1
        self.generic_visit(node)

    def visit_Try(self, node):
        self.decision_points += len(node.handlers)
        if node.finalbody:
            self.decision_points += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        self.decision_points += len(node.values) - 1
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.generic_visit(node)

    def calculate_complexity(self):
        return self.decision_points + 1

def get_function_complexity(source_code):
    tree = ast.parse(source_code)
    analyzer = ComplexityAnalyzer()
    analyzer.visit(tree)
    return analyzer.calculate_complexity()

sample_code = """
def example_function(x):
    if x > 0:
        print("Positive")
    elif x == 0:
        print("Zero")
    else:
        print("Negative")

    for i in range(x):
        if i % 2 == 0:
            print(i)

    while x > 0:
        x -= 1

    try:
        result = 10 / x
    except ZeroDivisionError:
        print("Division by zero!")
    finally:
        print("Done")

    if x > 5 and x < 10:
        print("In range")
"""

complexity = get_function_complexity(sample_code)
print("Cyclomatic Complexity:", complexity)
