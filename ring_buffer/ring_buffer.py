from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.track = 0

    def append(self, item):
        if self.storage.length < self.capacity:  # If buffer isn't full, add to head
            self.storage.add_to_tail(item)
            self.track += 1
        else:  # If it's full remove in order
            cur = self.storage.head
            for _ in range(self.track % self.capacity):
                cur = cur.next
            cur.value = item
            self.track += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        item = self.storage.head
        if self.storage.length < 1:
            return list_buffer_contents
        else:
            while item.next:
                list_buffer_contents.append(item.value)
                item = item.next
            list_buffer_contents.append(item.value)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
