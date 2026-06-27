from main import get_quest_log

run_cases = [
    (
        ["Slay the dragon", "Find the lost amulet", "Rescue the merchant"],
        ["1. Slay the dragon", "2. Find the lost amulet", "3. Rescue the merchant"],
    ),
    (["Gather firewood"], ["1. Gather firewood"]),
]

submit_cases = run_cases + [
    ([], []),
    (
        ["Polish the armor", "Sharpen the sword", "Brew a potion", "Train the squire"],
        [
            "1. Polish the armor",
            "2. Sharpen the sword",
            "3. Brew a potion",
            "4. Train the squire",
        ],
    ),
    (
        ["Scout the cave", "Light the torch"],
        ["1. Scout the cave", "2. Light the torch"],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = get_quest_log(input1)
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
