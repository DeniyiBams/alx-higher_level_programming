#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node in a sorted list
 * @head: pointer to list to be add
 * @number: number to add
 * Return: the list with the new number
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *runner;
	runner = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (runner->next != NULL)
	{
		if ((runner->next)->n >= number)
		{
			new->next = runner->next;
			runner->next = new;
			return (new);
		}
		runner = runner->next;
	}

	runner->next = new;
	new->next = NULL;
	return (new);
}
