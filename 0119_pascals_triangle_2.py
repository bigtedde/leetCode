from typing import List
import pytest

def getRow(rowIndex: int) -> List[int]:
    prev, curr = [1], [1]  # set defaults
    for row in range(1, rowIndex + 1):
        curr = []
        for col in range(len(prev) + 1):
            if col == 0 or col == len(prev):  # first and last in each row always 1
                curr.append(1)
            else:  # all other elements are combination of elements above them
                curr.append(prev[col] + prev[col - 1])
        prev = curr
    return curr

@pytest.fixture(scope="module")
def row_ten():
    """Runs 'getRow' with a value of ten, returning the 10th 0-indexed row."""
    return getRow(10)

@pytest.mark.skip(reason="Test not yet implemented")
def test_left_side_mirrors_right_side(row_ten):
    """Ensure the left side mirrors the right side, with an optional unique middle element"""
    print(row_ten)
    pass



if __name__ == "__main__":
    print(getRow(5))