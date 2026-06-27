from main import get_critical_hits

run_cases = [
    ([12, 75, 40, 100, 9], [150, 200]),
    ([50, 49, 51], [100, 102]),
]

submit_cases = run_cases + [
    ([], []),
    ([10, 20, 30, 49], []),
    ([60, 60, 60], [120, 120, 120]),
    ([100, 5, 88, 50, 2], [200, 176, 100]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = get_critical_hits(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
