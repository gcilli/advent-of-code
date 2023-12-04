import os

def read_input(day=None, delimiter='\n'):
    assert day is not None, "'day' args cannot be None"
    with open(f"days/day{day:02d}/input.txt") as f:
        return f.read().split(delimiter)
    
def read_input_test(day=None, delimiter='\n'):
    assert day is not None, "'day' args cannot be None"
    with open(f"days/day{day:02d}/input_test.txt") as f:
        return f.read().split(delimiter)
    
def get_digits_as_string():
    return "0123456789"

def keep_only_digits(string):
    return ''.join([c for c in string if c in get_digits_as_string()])

def pad(grid, width, char):
    pad = [char * len(grid[0])]
    for _ in range(width):
        grid = pad + grid + pad

    for i in range(len(grid)):
        grid[i] = char*width + grid[i] + char*width
    
    return grid
