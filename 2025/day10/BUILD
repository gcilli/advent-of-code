load("@rules_python//python:defs.bzl", "py_binary")
load("@rules_cc//cc:defs.bzl", "cc_binary")

cc_binary(
    name="cppmain",
    srcs=["cppmain.cpp"],
    copts=[
        "-std=c++23",
        "-O3",
        "-march=native",
        "-DNDEBUG",
    ],
    data=[
        "inputs/input.txt",
        "inputs/input_test.txt",
    ],
    deps=["//utilities:cpputils"],
)

py_binary(
    name="pymain",
    srcs=["pymain.py"],
    data=[
        "inputs/input.txt",
        "inputs/input_test.txt",
    ],
    deps=[
        "//utilities:pyutils",
        "@pip//sympy",
        "@pip//numpy",
        "@pip//scipy",
    ],
)
