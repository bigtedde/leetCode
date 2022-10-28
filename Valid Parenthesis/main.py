# Ted Lawson
from typing import List


def main():
    s = "()[]{}"
    print(isValid(s))

    return


def isValid(s: str) -> bool:

    stack = []

    for char in s:
        if char == "{" or char == "(" or char == "[":
            stack.append(char)

        if char == "}":
            if not stack:
                return False
            if stack.pop() == "{":
                continue
            else:
                return False

        if char == ")":
            if not stack:
                return False
            if stack.pop() == "(":
                continue
            else:
                return False

        if char == "]":
            if not stack:
                return False
            if stack.pop() == "[":
                continue
            else:
                return False

    if not stack:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
