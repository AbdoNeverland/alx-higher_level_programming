#include "lists.h"

/**
 * insert_node - insert node
 *@head: the list
 *@number: int to add
 * Return: node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	unsigned int i = 0;
	listint_t *t, *prv = NULL, *h;

	h = *head;
	if (!h)
	{
		/*add to begining*/
		t = malloc(sizeof(listint_t));
		if (!t)
			return (NULL);
		t->n = number;
		t->next = NULL;
		*head = t;
		return (t);

	}
	do {
		if (!prv && h && number <= h->n)
		{
			/*add to begining*/
			t = malloc(sizeof(listint_t));
			if (!t)
				return (NULL);
			t->n = number;
			t->next = h;
			if (i == 0)
				*head = t;
			return (t);

		}
		if (prv && h && number >= prv->n && number <= h->n)
		{
			t = malloc(sizeof(listint_t));
			if (!t)
				return (NULL);
			t->n = number;
			t->next = h;
			if (prv)
				prv->next = t;
			if (i == 0)
				*head = t;
			return (t);
		}
		if (!h)
			break;
		prv = h;
		h = h->next;
		i++;
	} while (1);
	return (NULL);
}
