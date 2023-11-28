#include "lists.h"

/**
 * check_cycle - Checks for cycles in singly linked lists.
 * @list: Singly linked list to be checked.
 *
 * Return: 0 if no cycles found,
 *         1 if cycles were found.
 */
int check_cycle(listint_t *list)
{
	listint_t *backward, *forward;

	if (!list)
		return (NULL);
	/* Cycle detection */
	baxkward = forward = list;
	while (forward && forward->next && forward->next->next)
	{
		backward = backward->next;
		forward = forward->next->next;
		if (backward == forward)
			return (1);
	}

	return (0);
}
