#include "lists.h"
/**
 * check_cycle - checks if the list have a cycle
 * @list: the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *one = list, *two = list;

	if (!list)
		return (0);
	while (two && (two->next))
	{
		one = one->next;
		two = two->next->next;
		if (two == one)
			return (1);
	}
	return (0);
}
