                                                                                                                         # Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
   
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        print(f"{name} added to the front of the waitlist.")

    def add_end(self, name):
        new_node = Node(name)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"{name}added to the end of the waitlist.")

    
    def remove(self, name):
        if self.head is None:
            print("The waitlist is empty")
            return
        
        if self.head.name == name:
            self.head = self.head.next
            print(f"Removed {name} from the waitlist.")
            return
        
        current = self.head
        while current.next:
            if current.next.name == name:
                current.next = current.next.next
                print(f"Removed {name} from the waitlist.")
                return
            current = current.next

        print(f"{name} not found")

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
        else:
            current = self.head
            while current:
                print(f"- {current.name}")
                current = current.next 

def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()
            
            
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program

waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''
  
 # My code uses a linked list to store and manage a small restaurant style waitlist. The two main parts that I used to make my code work properly are Nodes and LinkedLists. I used Nodes to store names of customers as well as a reference to the next node in the list. I then used a LinkedList to manage the chain of nodes by using the head (first node in the list) as a reference point. The linked list works by connecting nodes together in sequence. If a new customer is added to the front of the LinkedList a new Node is created as the new head of the LinkedList. If a customer is added to the end, the program follows the list and adds the new node to the end. Removing a customer works by adjusting the references so that the unwanted Node is skipped, effectively cutting it out of the chain.
 # A real engineer might need a custom list like this in cases where dynamic memory management and efficient insertion/removal are required. For example, linked lists can be useful for task scheduling systems, real-time simulations, memory allocation tools, or queue management systems where the number of items is constantly changing. Unlike arrays, linked lists do not require resizing, which makes them a flexible choice in environments where performance and memory efficiency are important. 

 