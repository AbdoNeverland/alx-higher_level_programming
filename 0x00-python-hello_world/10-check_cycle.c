#include "lists.h"
/**
 * check_cycle - checks if the list have a cycle
 * @list: the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;

	if (!list)
		return (0);
	do {
		list = list->next;
		if (list == head)
			return (1);
	} while (list != NULL && list != head);
	return (0);
}
