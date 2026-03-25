class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0) # Dummy head
        self.tail = Node(0, 0) # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_at_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_tail(self):
        if self.size == 0: return None
        node = self.tail.prev
        self.remove_node(node)
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_map = {} # key -> Node
        self.freq_map = {} # freq -> DoublyLinkedList

    def _update_freq(self, node):
        # Remove from old frequency list
        old_freq = node.freq
        self.freq_map[old_freq].remove_node(node)
        
        # If the old list is empty and was the min_freq, increment min_freq
        if self.freq_map[old_freq].size == 0 and old_freq == self.min_freq:
            self.min_freq += 1
            
        # Update node frequency and move to new list
        node.freq += 1
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DoublyLinkedList()
        self.freq_map[node.freq].add_at_head(node)

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        node = self.key_map[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        
        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self._update_freq(node)
        else:
            if self.size == self.capacity:
                # Evict the LRU node from the min_freq list
                removed_node = self.freq_map[self.min_freq].remove_tail()
                del self.key_map[removed_node.key]
                self.size -= 1
            
            # Add new node
            new_node = Node(key, value)
            self.key_map[key] = new_node
            self.min_freq = 1
            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            self.freq_map[1].add_at_head(new_node)
            self.size += 1