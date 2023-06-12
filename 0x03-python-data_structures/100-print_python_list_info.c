#include "lists.h"
#include <Python.h>
#include <listobject.h>
#include <object.h>
/**
 * print_python_list_info -prints infos
 *@p: list
 */
void print_python_list_info(PyObject *p)
{
	long int n = PyList_Size(p);
	int i;
	PyListObject *p_list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", n);
	printf("[*] Allocated = %ld\n", p_list->allocated);
	for (i = 0; i < n; i++)
	{
		struct _typeobject *to = Py_TYPE(p_list->ob_item[i]);
		printf("Element %d: %s\n", i, to->tp_name);
	}
}
