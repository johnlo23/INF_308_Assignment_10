# John Logiudice
# INF 308 - Fall 2022
# Assignment 10 - Algorithms
# Work with names in a list


class Names:

    def __init__(self, name_list=None):
        # If no list provided, start with empty list
        if name_list is None:
            self.name_list = []
        else:
            self.name_list = name_list

    # return the length of the current name list
    def list_len(self):
        return len(self.name_list)

    # Print the current list of names with index numbers
    def display_list(self):
        print("Name List")
        print("- "*8)
        for i in range(0, self.list_len()):
            print(f"{i}. {self.name_list[i]}")

    # Add (insert) a name to the specified index number
    def add_name(self, value, index=None):
        # Default to end of list if no index is given
        if index is None:
            index = self.list_len()

        # If the given index out of bounds return None
        if index > self.list_len():
            return None

        # Add a new empty item to the end of list
        self.name_list.append("")

        # Copy each item after the insert point to the next spot in the list
        for i in range(self.list_len() - 1, index, -1):
            self.name_list[i] = self.name_list[i-1]

        # Add the new item to the specified spot in the list
        self.name_list[index] = value

        return value

    # Delete the first occurrence of a name in the list
    def delete_name(self, value):
        index = self.search_name(value)
        if index is None:
            return None
        else:
            for i in range(index, self.list_len() - 1):
                self.name_list[i] = self.name_list[i+1]

        del (self.name_list[-1])
        return value

    # Sort two words lexicographically, return tuple in sorted order
    def sort_word(self, word1, word2):
        # Convert variables to strings
        word1 = str(word1)
        word2 = str(word2)

        # Get lengths of both words
        len1 = len(word1)
        len2 = len(word2)

        # Get the length of the shortest word for the iteration
        min_len = min(len1, len2)

        # Iterate over each letter
        for i in range(0, min_len):
            if word1[i].lower() < word2[i].lower():
                # Word 1 sorts first
                return word1, word2

            elif word2[i].lower() < word1[i].lower():
                # Word 2 sorts first
                return word2, word1

        # If we get to this test, the first i characters of each word are identical
        if len2 < len1:
            # Word 2 is shorter
            return word2, word1
        else:
            # Word 1 is shorter or lengths are even, so keep initial order
            return word1, word2

    # Sort the list by name
    def sort_list(self):
        # Iterate of each word in order
        for i in range(0, self.list_len()):
            # Iterate over each other word in order, skip words in the same position
            # min() avoids index out of range errors
            for j in range(min(i+1, self.list_len()), self.list_len()):
                # Sort word1 and word2
                a, b = self.sort_word(self.name_list[i], self.name_list[j])
                # If the sorted order is different than the original order
                if (self.name_list[i], self.name_list[j]) != (a, b):
                    # Swap the two words
                    self.name_list[i] = a
                    self.name_list[j] = b

    # Search for the index number of a name in the list
    def search_name(self, value):
        for i in range(0, self.list_len()):
            if self.name_list[i].lower() == value.lower():
                return i

        return None


# Class to create a menu with menu numbers
class PickMenu:

    # Initialize the menu with required Title and menu Items
    def __init__(self, menu_details):
        self.menu_name = menu_details['title']
        self.menu_items = menu_details['items']

    # Print each menu item with menu numbers
    def show_menu(self):
        print(self.menu_name)
        print("- "*8)
        for i in range(0, len(self.menu_items)):
            print(f"{str(i + 1)}. {self.menu_items[i]}")

    # Get and validate menu choice from user
    def get_menu_response(self):
        # loop until user gives valid menu response
        while True:
            # Ask user for menu number
            response = input("Enter the number of your menu choice: ").strip()
            # Check if response string is an integer
            if response.isdigit():
                # Check if response is a valid menu integer
                if (int(response) - 1) in range(0, len(self.menu_items)):
                    return int(response)

            # User did not enter valid integer response
            print(f"Please enter a menu choice between 1 and {len(self.menu_items)}.")
            print()







def main():
    # Initialize list of names with some starter names
    names = Names(['Kwame', 'Alex', 'Roberta', 'Bharathi', 'Spyro', 'Martika', 'Roberta',
                 'Sebastian', 'Robert', 'Greta', 'Oliver'])

    # Main Menu details
    main_menu_tuple = ('Add a Name', 'Delete a Name', 'Sort List by Name', 'Search for a Name', 'Quit')
    main_menu_name = 'Main Menu'
    main_menu_details = {'title': main_menu_name, 'items': main_menu_tuple}

    # Create the Main Menu object
    main_menu = PickMenu(main_menu_details)

    # Display list of names
    print()
    names.display_list()

    # Display main menu
    print()
    main_menu.show_menu()

    names.sort_list()

    names.display_list()


if __name__ == '__main__':
    main()