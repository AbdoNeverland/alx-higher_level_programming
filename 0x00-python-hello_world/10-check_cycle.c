#include "lists.h"
/**
 * check_cycle - checks if the list have a cycle
 * @list: the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	do {
		list = list->next;
	} while( list != NULL && list != head);
	if (list == head)
		return (1);
	else
		return (0);
}
