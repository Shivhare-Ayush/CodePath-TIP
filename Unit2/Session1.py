'''
-- Dictionaries
Common Use:
- Store key-value pairs
- Fast lookups by key
- Frequency count
- Grouping items by a common attribute



UPI method:
U - Understand
    I - Input
    O - Output
    R - Requirements
    E - Edge cases
P - Plan
I - Implement
'''

def total_treasure(treasure_map):
    ''' Understand: Given a dictionary representing a treasure map, we need to calculate the total value of the treasures.
    Input: Dictionary "treasure_map"
    Output: Integer total value of treasures
    Requirements: Sum the values of all treasures in the map'''
    total = 0
    for value in treasure_map.values():
        total += value
    return total

# --
treasure_map = {'gold': 100, 'silver': 50, 'diamonds': 200}
print("Total Treasure Value:", total_treasure(treasure_map)) # 350

def can_trust_message(message):
    ''' Understand: Given a message string, we need to determine if the message can be trusted based on its 'verified' status.
    Input: String "message"
    Output: Boolean indicating if the message is trusted
    Requirements: Return True if 'verified' is True, otherwise False'''
    checker = set(message)
    return 'verified' in checker and checker['verified'] is True

# --
message1 = {'text': 'Hello', 'verified': True}
message2 = {'text': 'Hello', 'verified': False}
print("Message 1 Trusted:", can_trust_message(message1)) # True
print("Message 2 Trusted:", can_trust_message(message2)) # False

# So far its been set spamming and dict spamming, now lets do a mix of both

# Booby trap
'''
    Understand: Given a string, find if removing 1 word makes all remaining words =.
    Input: String "message" 
    Output: Boolean indicating if the condition is met
    edge cases: max occurrences = 1, return True

'''
def booby_trap(message):
    word_freq = {}
    for word in message.split():
        word_freq[word] = word_freq.get(word, 0) + 1

    freq_values = list(word_freq.values())
    return freq_values.count(freq_values[0]) == len(freq_values) - 1

# if you make a dict like this hashmap = defaultdict (int) it makes an empty dict with default int values as 0