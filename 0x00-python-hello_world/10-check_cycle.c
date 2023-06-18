#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	const listint_t *current;
    const listint_t *head;
    head = list;
    current = list->next;
    while (current != NULL)
    {
        printf("%i %i ***", current->n, head->n);
        if(head == current && current->next == NULL){
            return 1;
        }
        current = current->next;
    }
        return 0;
}
