class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def linked_list_from_string(s):
    if s.strip() == "None":
        return None

    values = s.split(" -> ")[:-1]

    if not values:
        return None

    head = Node(int(values[0]), None)
    current = head

    for value in values[1:]:
        new_node = Node(int(value), None)
        current.next = new_node
        current = new_node
    return head 