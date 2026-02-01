load("@rules_python//python:defs.bzl", "py_library")
load("@rules_cc//cc:defs.bzl", "cc_library")

cc_library(
    name = "cpputils",
    hdrs = ["cpputils.h"],
    visibility = ["//:__subpackages__"],
)

py_library(
    name = "pyutils",
    srcs = ["pyutils.py"],
    visibility = ["//:__subpackages__"],
)
