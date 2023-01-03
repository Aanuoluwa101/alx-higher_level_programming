#include "lists.h"


/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: head of a listint_t list
 *
 * Returns: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp;
	listint_t *prev;

	temp = list;
	prev = temp;

	while (temp != NULL)
	{
		if (temp->next == prev)
		{
			return (1);
		}
		else
		{
			prev = temp;
			temp = temp->next;
		}
	}
	return (0);
}
