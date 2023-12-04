# Advent of Code

Here there are my solutions to the AoC events. Each solution is coded in both C++ and Python (when I had time to write both).

How to run:

    # C++
    bazel run //2025/day01:cppmain

    # Python
    bazel run //2025/day01:pymain

Regarding runtime, whenever possible, I tried to not consider input parsing. So all the steps needed to read the input file from the filesystem and parse it are, in most cases, ignored by the runtime performance.