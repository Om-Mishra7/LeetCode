def reverseList(head):
        
        previous_value = None

        current_head = head

        while current_head:
            next_value = current_head.next
            current_head = previous_value