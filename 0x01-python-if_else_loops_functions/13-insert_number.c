#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *current;
    listint_t *prev;
    current = *head;
    prev = NULL;

    new = malloc(sizeof(listint_t));
    new->n = number;
    new->next = NULL;
    
    if (current == NULL)
        return (NULL);

    if (*head == NULL)
    {
        new->next = NULL;
        *head = new;
    }

    else
    {
        while (current != NULL)
        {
            if (current->n >= number)
            {
                if (prev == NULL)
                    *head = new;
                else
                    prev->next = new;
                new->next = current;
                break;
            }
            prev = current;
            current = current->next;
        }
        if (new->next == NULL)
        {
            prev->next = new;
            new->next = current;
        }
    }
    return (new);
}
