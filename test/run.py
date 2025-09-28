


def test_isNumPosStrValue():
    test_cases = {
        "123": True,     # 正常正数字符串
        "0": False,      # 排除零
        "001": True,     # 前导零也算数字
        "abc": False,    # 非数字字符串
        None: False,     # None
        123: False,      # 整型而不是字符串
    }

    try:
        from lib.core.common import isNumPosStrValue
    except:
        print("Test 1 failed: Could not find isNumPosStrValue in lib.core.common")
        return
    for inp, expected in test_cases.items():
        result = isNumPosStrValue(inp)
        try:
            assert result == expected
        except AssertionError as e:
            print(f"Test 1 failed: Input: {repr(inp):6} → Output: {result} (Expected: {expected})")
            return

    print("Test 1 passed.")

def test_import():
    try:
        import plugins.generic.enumeration as enumeration
        enumeration.isNumPosStrValue(1)
    except Exception as e:
        if str(e) == "module 'plugins.generic.enumeration' has no attribute 'isNumPosStrValue'":
            print("Test 2 failed: You did not import isNumPosStrValue in plugins/generic/enumeration.py")
            return

    print("Test 2 passed.")

def test_refactor():
    with open("plugins/generic/enumeration.py", "r") as f:
        locs = f.readlines()

    cleaned_locs = [s.replace(" ", "").replace("\t", "").replace("\n", "") for s in locs]

    old_loc_cnt = 0
    new_loc_cnt = 0
    for s in cleaned_locs:
        if s == "ifnotcount.isdigit()ornotlen(count)orcount ==\"0\":":
            old_loc_cnt += 1
        if s == "ifnotisNumPosStrValue(count):":
            new_loc_cnt += 1

    try:
        assert old_loc_cnt == 0 and new_loc_cnt == 12
    except:
        print("Test 3 failed: You missed some places to refactor")
        return

    print("Test 3 passed.")


if __name__ == "__main__":
    # Test 1:
    test_isNumPosStrValue()

    # Test 2:
    test_import()

    # Test 3:
    test_refactor()