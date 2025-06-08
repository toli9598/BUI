load("@rules_python//python:py_binary.bzl", "py_binary")
load("@rules_python//python:py_library.bzl", "py_library")

py_binary(
    name = "hello_world",
    srcs = select({
        ":windows": ["hello_windows.py"],
        ":macos": ["hello_mac.py"],
        "//conditions:default": ["hello_linux.py"]
    }),
    main = select({
        ":windows": "hello_windows.py",
        ":macos": "hello_mac.py",
        "//conditions:default": "hello_linux.py"
    }),
    deps = [":main"]
)

py_library(
    name = "main",
    srcs = ["hello_world.py"],
    deps = [
        "//lib:libs"
    ]
)

constraint_setting(name = "os")
constraint_value(name = "windows_system", constraint_setting = ":os")
constraint_value(name = "linux_system", constraint_setting = ":os")
constraint_value(name = "macos_system", constraint_setting = ":os")

#platform(
#    name = "windows"
#    constraint_values = [
#        "@platforms//os:windows"
#    ]
#)
