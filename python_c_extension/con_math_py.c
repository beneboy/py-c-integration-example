#include <Python.h>
#include <con_math.h>

static PyObject *con_math_py_is_prime_naive(PyObject *self, PyObject *args) {
    unsigned int numberToCheck;

    if (!PyArg_ParseTuple(args, "I", &numberToCheck))
        return NULL;

    bool result = isPrimeNaive(numberToCheck);

    return Py_BuildValue("i", result);
}


static PyMethodDef ConMathMethods[] = {
    {"is_prime_naive",  con_math_py_is_prime_naive, METH_VARARGS,
     "Test if a number is prime."},
    {NULL, NULL, 0, NULL}
};


PyMODINIT_FUNC initcon_math(void) {
    (void) Py_InitModule("con_math", ConMathMethods);
}
