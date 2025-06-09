This is a short examample implementation of the bazel build management. The application prints a welcoming message alongside a time and date.

To build the application, use `bazel build :main`. The result can be found in BUI/bazel-bin/main.

To build and run the application, use `bazel run :main`.

To compile for a platform different from your host system, use the argument `--platforms=:windows`, `--platforms=:linux` or `--platforms=:macos`. This expects a x86_64 cpu and is mainly a PoC.

To run a complete clean, use `bazel clean --expunge`.

**Github Actions is set up for a test-run on a push**
