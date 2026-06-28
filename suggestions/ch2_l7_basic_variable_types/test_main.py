import main as student_code

# (variable_name, expected_value, expected_type)
run_cases = [
    ("player_health", 100, int),
]

submit_cases = run_cases + [
    ("player_has_magic", True, bool),
]


def test(var_name, expected_value, expected_type):
    print("---------------------------------")
    print(f"Checking: {var_name}")
    actual_value = getattr(student_code, var_name, None)
    actual_type = type(actual_value)
    print(f"Expected: {expected_value} (type: {expected_type.__name__})")
    print(f"Actual:   {actual_value} (type: {actual_type.__name__})")
    # We grade the real value AND the real type, so printing the
    # right text or leaving a value as a string can't pass.
    if actual_type is expected_type and actual_value == expected_value:
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
