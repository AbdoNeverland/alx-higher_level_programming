#include "lists.h"
/**
 * reverse_linked_from_index - reverse list by index
 * @head: list
 * @index: index
 */
listint_t *reverse_linked_from_index(listint_t **head, int index)
{
	int i;
	listint_t *h = *head, *prv, *t_next, *t_h, *br = NULL;
	for (h = *head, i = 0;; i++)
	{
		t_next = h->next;
		t_h = h;
		if (i == index)
		{
			h->next = NULL;
			br = prv;
		}
		else if (i > index)
		{
			h->next = prv;
		}
		prv = t_h;

		h = t_next;
		if (t_next == NULL)
			break;
	}
	br->next = t_h;
	return (t_h);
}
/**
 * is_palindrome - checks if it's a palindrome
 *@head: the lis
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int demi, nb = 0, result = 1, i;
	listint_t *h = *head, *r;

	for (nb = 0; h && h->next != NULL; h = h->next)
		nb++;
	if (nb == 0)
		return (1);
	demi = nb / 2;
	nb = nb % 2 == 0 ? nb : nb - 1;
	h = *head;
	r = reverse_linked_from_index(head, demi);
	for (i = 0; i < demi; i++)
	{
		if (h->n != r->n)
		{
			result = 0;
			break;
		}
		h = h->next;
		r = r->next;
	}
	reverse_linked_from_index(head, demi);
	return (result);
}
/**
 * is_palindrome0 - checks if it's a palindrome
 *@head: the lis
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome0(listint_t **head)
{
	int nb = 0, i, *v;
	listint_t *h = *head;

	for (nb = 0; h && h->next != NULL; h = h->next)
		nb++;
	if (nb == 0)
		return (1);
	v = malloc(nb * sizeof(int));
	if (!v)
		return (0);
	for (h = *head, i = 0; h && h->next != NULL; h = h->next, i++)
		v[i] = h->n;
	v[i] = h->n;
	for (i = 0; i <= nb / 2; i++)
	{
		if (v[i] != v[nb - i])
		{
			free(v);
			return (0);
		}
	}
	free(v);
	return (1);
}
