#!/usr/bin/python3
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int len = 0, i = 0;
    int arr[len / 2];
    
    // Get length of linked list
    while (current)
    {
        len++;
        current = current->next;
    }
    
    // Store first half of linked list in array
    current = *head;
    while (i < len / 2)
    {
        arr[i] = current->n;
        current = current->next;
        i++;
    }
    
    // Handle odd length cases
    if (len % 2 != 0)
        current = current->next;
    
    // Compare second half of linked list with array
    i--;
    while (current)
    {
        if (current->n != arr[i])
            return 0;
        current = current->next;
        i--;
    }
    return 1;
}
