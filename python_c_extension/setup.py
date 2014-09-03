from distutils.core import setup, Extension

setup(
    ext_modules=[Extension("con_math", ["con_math_py.c", "../lib/con_math.c"],
    include_dirs=['../lib'])],
)
