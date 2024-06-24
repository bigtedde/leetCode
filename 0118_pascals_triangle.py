from typing import List
import pytest

def main():
    answer = generate_triangle(0)
    print(answer)

def generate_triangle(numRows: int) -> List[List[int]]:
    prev_row, cur_row, answer = [1], [], [[1]]
    for row in range(1, numRows):
        for index in range(len(prev_row) + 1):
            if index == 0 or index == len(prev_row):
                cur_row.append(1)
            else:
                cur_row.append(prev_row[index] + prev_row[index - 1])
        answer.append(cur_row)
        prev_row, cur_row = cur_row, []
    return answer if numRows else []

@pytest.fixture
def triangle():
    return generate_triangle(10)

def test_start_and_end(triangle):
    for row in triangle:
        assert row[0] == 1
        assert row[-1] == 1

def test_length(triangle):
    triangle = generate_triangle(10)
    for row in range(1, len(triangle)):
        assert len(triangle[row]) == len(triangle[row-1]) + 1

def test_no_rows():
    assert generate_triangle(0) == []

def test_single_row():
    assert generate_triangle(1) == [[1]]

def test_two_rows():
    assert generate_triangle(2) == [[1], [1, 1]]

if __name__ == "__main__":
    main()
