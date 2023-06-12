#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t *current;

    while (*head != NULL)
    {
        current = *head;
        *head = current->next;
        printf("%d - " , current->n);
    }
	return (1);
}
