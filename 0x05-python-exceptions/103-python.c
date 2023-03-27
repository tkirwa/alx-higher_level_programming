#include <Python.h>
#include <float.h>

/**
 * print_python_list - prints information about Python lists
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t i, size;
    PyObject *obj;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        fflush(stdout);
        return;
    }
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, ((PyListObject *)p)->allocated);
    for (i = 0; i < size; i++)
    {
        obj = PyList_GET_ITEM(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
        else if (PyFloat_Check(obj))
            print_python_float(obj);
    }
    fflush(stdout);
}

/**
 * print_python_bytes - prints information about Python bytes objects
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *buffer;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        fflush(stdout);
        return;
    }
    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);
    buffer = PyBytes_AsString(p);
    printf("  trying string: %s\n", buffer);
    if (size > 10)
        size = 10;
    printf("  first %ld bytes:", size + 1);
    for (i = 0; i <= size; i++)
        printf(" %02x", buffer[i] & 0xff);
    printf("\n");
    fflush(stdout);
}

/**
 * print_python_float - prints information about Python float objects
 * @p: pointer to PyObject
 */
void print_python_float(PyObject *p)
{
    char *buffer;
    Py_ssize_t size;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        fflush(stdout);
        return;
    }
    buffer = PyOS_double_to_string(PyFloat_AsDouble(p), 'r', 0, Py_DTSF_ADD_DOT_0, &size, NULL);
    printf("  value: %s\n", buffer);
    fflush(stdout);
    PyMem_Free(buffer);
}
