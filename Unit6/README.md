# Unit 6

This folder contains Python practice files for Unit 6 of CodePath's TIP 102 Course.

## Files
- Add your Python practice files (.py) here
- Include any notes or additional resources as needed

## Usage
Each .py file should be named descriptively based on the problem or concept being practiced.


Linked lists 2 
Techniques for linked lists 

Temp head method: 
- Create a temporary head node to simplify edge cases
- If we need to delete the head node itself, we can just adjust the next pointer of the temporary head
- At the end, return temp_head.next as the new head of the modified list

Slow and fast pointers:
- Use two pointers moving at different speeds to find the middle of the list or detect cycles
- The slow pointer moves one step at a time, while the fast pointer moves two steps at a time
- When the fast pointer reaches the end, the slow pointer will be at the middle of the list
** Given an even list length, return the second middle node (round up)

