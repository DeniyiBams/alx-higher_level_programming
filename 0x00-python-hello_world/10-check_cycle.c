#include "lists.h"

/**
 * check_cycle - check if there is a cycle
 * @list: pointer to list to be analyzed
 * Return: 1 is cycle 0 not
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise;
	listint_t *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = hare = list;

	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}

	return (0);
}
