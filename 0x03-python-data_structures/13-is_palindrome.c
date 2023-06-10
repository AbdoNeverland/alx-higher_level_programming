#include "lists.h"

/**
 * is_palindrome - checks if it's a palindrome
 *@head: the lis
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int is, nb = 0, i, *v;
	listint_t *h = *head;

	for (nb = 0; h &&  h->next != NULL; h = h->next)
		nb++;
	if (nb == 0)
		return (1);
	v = malloc(nb * sizeof(int));
	if (!v)
		return (0);
	for (h = *head, i = 0; h && h->next != NULL; h = h->next, i++)
		v[i] = h->n;
	v[i] = h->n;
	is = 1;
	for (i = 0; i <= nb / 2; i++)
	{
		if (v[i] != v[nb  - i])
		{
			is = 0;
			break;
		}
	}
	free(v);
	return (is);
}
