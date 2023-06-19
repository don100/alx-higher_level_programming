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

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    //new->next = NULL;

    if (*head == NULL){
        new->next = NULL;
        *head = new;
    }
        
    else
    {
        while (current->next != NULL)
        {
            if(current->n >= number)
            {
                new->next = current;
                prev->next = new;
            }       
            prev = current;
            current = current->next;

        }
    }

    return (new);
}
