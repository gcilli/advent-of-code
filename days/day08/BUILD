cc_binary(
    name = "cppmain",
    srcs = ["cppmain.cpp"],
    data = [
        "input.txt",
        "input_test.txt",
    ],
    deps = ["//utilities:cpputils"],
)

py_binary(
    name = "pymain",
    srcs = ["pymain.py"],
    data = [
        "input.txt",
        "input_test.txt",
    ],
    deps = ["//utilities:pyutils"],
)
