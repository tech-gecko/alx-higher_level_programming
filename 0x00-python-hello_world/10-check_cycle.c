#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks for cycles in singly linked lists.
 * @list: Singly linked list to be checked.
 *
 * Return: 0 if no cycles found,
 *         1 if cycles were found.
 */
int check_cycle(listint_t *list)
{
	listint_t *i;
	while (list != NULL)
	{
		i = list->next;
		if (list == i)
		{
			return (1);
		}
		list = list->next;
	}
	return (0);
}
