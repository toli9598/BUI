load("@rules_python//python:py_binary.bzl", "py_binary")
load("@rules_python//python:py_library.bzl", "py_library")

py_binary(
    name = "hello_world",
    srcs = select({
        "@platforms//os:windows": ["hello_windows.py"],
        "@platforms//os:macos": ["hello_mac.py"],
        "//conditions:default": ["hello_linux.py"]
    }),
    main = select({
        "@platforms//os:windows": "hello_windows.py",
        "@platforms//os:macos": "hello_mac.py",
        "//conditions:default": "hello_linux.py"
    }),
    deps = [":main"],
    visibility = ["//:__pkg__"]
)

py_library(
    name = "main",
    srcs = ["hello_world.py"],
    deps = [
        "//lib:libs"
    ]
)
