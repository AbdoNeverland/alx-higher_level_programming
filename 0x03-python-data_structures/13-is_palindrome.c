#include "lists.h"

/**
 * is_palindrome - checks if it's a palindrome
 *@head: the lis
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int nb = 0, i, *v, vv[1024];
	listint_t *h = *head;

	for (nb = 0; h &&  h->next != NULL; h = h->next)
		nb++;
	if (nb == 0)
		return (1);
	v = malloc(nb * sizeof(int));
	if (!v)
		return (0);
	for (h = *head, i = 0; h && h->next != NULL; h = h->next, i++)
		v[i] = vv[i]= h->n;
	v[i] = h->n;
	for (i = 0; i <= nb / 2; i++)
	{
		if (vv[i] != vv[nb  - i])
		{
			free(v);
			return (0);
		}
	}
	free(v);
	return (1);
}
