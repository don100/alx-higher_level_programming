#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
    if (!list)
        return (0);
    const listint_t *current;
    const listint_t *head;
    head = list;
    current = list->next;
    while (current != NULL)
    {
        if(head == current)
            return (1);
        current = current->next;
    }
        return (0);
}
