"""
Author: BENEDICT  KARIUKI
Date: September 14, 2024
Version: 1.0
Description: This script removes common letters from two names and determines the
relationship between two people using the FLAMES game logic.
"""
# function to remove common letters
def remove_common(player1: str, player2: str) -> str:
    name1_list = list(player1)
    name2_list = list(player2)
    for i in name1_list[:]:
        for j in name2_list[:]:
            if i == j:
                name1_list.remove(i)
                name2_list.remove(j)
    total_remaining = name1_list + name2_list
    return "".join(total_remaining)

if __name__ == '__main__':
    # ask for user input
    player1_name = input("Player 1 name: ").upper()
    player2_name = input("Player 2 name: ").upper()
    uniq_chars = remove_common(player1_name, player2_name)
    print(uniq_chars)
    flames = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]
    count = len(uniq_chars)
    index = 0
    while len(flames) > 1:
        # calculate the index to remove
        """
        Example. say the remaining characters are 6
        count = 6
        iteration 1: removes 'Siblings' = index 5
        iteration 2: removes 'Friends' = index 0
        iteration 3: removes 'Affectionate' = index 2
        iteration 4: removes 'Lovers' = index 1
        iteration 5: removes 'Enemies' = index 4
        iteration 6 - flames length is 1 and breaks out of the loop
        """
        index = (index + count - 1) % len(flames)
        # remove the element at this index
        flames.remove(flames[index])
    print(f'Relationship: {flames[0]}')



