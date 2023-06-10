#include "lists.h"
/**
 * print_python_list_info -prints infos
 *@p: list
 */
void print_python_list_info(PyObject *p)
{
	printf("[*] Size of the Python List = %d\n", Py_SIZE(p));
	printf("[*] Allocated = %d\n", PyObject_Size(p));
	for()
	{
	printf("Element %d: %s\n");
	}
}
