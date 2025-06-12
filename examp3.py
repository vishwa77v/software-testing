def add(a, b):
    return a + b

def generate_test_cases():
    return [
        {"input": (1, 2), "expected": 3},
        {"input": (0, 0), "expected": 0},
        {"input": (-1, 1), "expected": 0},
        {"input": (100, 200), "expected": 300},
        {"input": (3.5, 2.5), "expected": 6.0},
        {"input": (1, -2), "expected": -1},
        {"input": ("a", "b"), "expected": "ab"},  
    ]

def run_tests(func, test_cases):
    print("Running Automated Tests...\n")
    for i, case in enumerate(test_cases, start=1):
        args = case["input"]
        expected = case["expected"]
        try:
            result = func(*args)
            if result == expected:
                status = "✅ PASS"
            else:
                status = "❌ FAIL"
        except Exception as e:
            result = str(e)
            status = "❌ ERROR"

        print(f"Test Case {i}:")
        print(f"  Input: {args}")
        print(f"  Expected Output: {expected}")
        print(f"  Actual Output:   {result}")
        print(f"  Status: {status}\n")

if __name__ == "__main__":
    test_cases = generate_test_cases()
    run_tests(add, test_cases)
