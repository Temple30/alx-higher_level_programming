#include <stdio.h>
#include <python.h>
/**
 * print_python_list - Prints information about a Python list
 * @p: PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid PyListObject\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);

	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid PyBytesObject\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	char *bytes_str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", bytes_str ? bytes_str : "(no printable)");

	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < size && i < 10; ++i)
	{
		printf("%02hhx", bytes_str[i]);

		if (i < 9)
			printf(" ");
	}
	printf("\n");
}
