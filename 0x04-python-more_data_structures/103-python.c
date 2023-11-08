void print_python_list(PyObject *p)
{
    Py_ssize_t i, len;
    PyObject *item;
    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    len = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", len, ((PyListObject *)p)->allocated);

    for (i = 0; i < len; i++)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}


void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes;
    Py_ssize_t size, i;
    char *string;
    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;
    size = PyBytes_Size(p);

    string = PyBytes_AsString(p);
    printf("  size: %ld\n  trying string: %s\n", size, string);

    if (size > 10)
        size = 10;

    printf("  first %ld bytes: ", size);

    for (i = 0; i < size; i++)
    {
        printf("%02x", (unsigned char)string[i]);
        if (i == size - 1)
            printf("\n");
        else
            printf(" ");
    }
}
