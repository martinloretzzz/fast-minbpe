class MergeListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MergeList:
    def __init__(self, initial=[]):
        self.next = None
        self.expand(initial)

    def expand(self, idx):
        last = self
        while last.next:
            last = last.next

        for id in idx:
            new_node = MergeListNode(id)
            last.next = new_node
            last = new_node

    def merge(self, pair, idx):
        previous = self

        while previous.next and previous.next.next:
            current = previous.next
            next = current.next
            if current.data == pair[0] and next.data == pair[1]:
                new_node = MergeListNode(idx)
                previous.next = new_node
                new_node.next = next.next

                previous = new_node
            else:
                previous = current

    def get_stats(self, counts=None):
        counts = {} if counts is None else counts
        current = self.next
        while current and current.next:
            next = current.next
            pair = (current.data, next.data)
            if not pair in counts:
                counts[pair] = 0
            counts[pair] += 1
            current = next
        return counts

    def print_list(self):
        current = self.next
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
