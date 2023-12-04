import os
import time


class Timer:
    """Timer class for measuring execution time in milliseconds."""

    def __init__(self):
        """Start the timer."""
        self.start_time = time.perf_counter()

    def reset(self):
        """Reset the timer to the current time."""
        self.start_time = time.perf_counter()

    def elapsed_ms(self):
        """Return elapsed time in milliseconds."""
        return (time.perf_counter() - self.start_time) * 1000.0


def read_input(filename):
    with open(filename) as f:
        return f.read()


def pad(grid, width, char):
    pad = [char * len(grid[0])]
    for _ in range(width):
        grid = pad + grid + pad

    for i in range(len(grid)):
        grid[i] = char * width + grid[i] + char * width

    return grid
