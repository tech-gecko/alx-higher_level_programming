#include "lists.h"

/**
 * check_cycle - ...
 * @list: list
 *
 * Return: 0, no head otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (-1);
/* floyed cycle detection */
	slow = list;
	while (slow->next != NULL)
	{
		fast = slow->next;
		if (slow == fast)
			return (1);
		slow = slow->next;
	}

	return (0);
}
