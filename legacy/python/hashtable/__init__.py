'''
Basic hash table to practice working through hash table logic...
'''


class HashTable():

    def __init__(self):
        CURRENT_SIZE = 10
        self.table_size = CURRENT_SIZE
#         self.table = [0] * self.table_size
        # TODO: make this more dynamic .. check for collisions instead of filling every slot with a linked list (maybe?)
        self.table = [SingleLinkedList() for x in range(CURRENT_SIZE)]

    def insert(self, input_str):
        # using chaining will require a linked list on all items..
        # will also need to resize if the table is full...
        # TODO: implement table resizing
        self.table[self.__simple_str_hash(input_str)].append(input_str)

    def remove(self, input_str):
        self.table[self.__simple_str_hash(input_str)].remove(input_str)

    def exists(self, input_str):
        return self.table[self.__simple_str_hash(input_str)].exists(input_str)

    def __resize_table(self):
        # TODO: implement table resizing
        pass

    def __simple_str_hash(self, str_to_hash):
        sum_ = 0
        if not str_to_hash:
            raise ValueError('invalid input string')

        for char in str_to_hash:
            sum_ += ord(char)

        # to determine placement within the table
        return sum_ % self.table_size

    def __str__(self):
        return '{}'.format(self.table)


class SingleLinkedList():

    def __init__(self):
        ''' Create as empty linked list. '''
        self.head = None
        self.tail = None

    def show(self):
        curr_node = self.head
        output = ''
        while curr_node:
            output += '{}, '.format(curr_node.data)
            curr_node = curr_node.next

        print('[{}]'.format(output))

    def append(self, data):
        # create the base node which holds the data
        node = self.Node(data, None)
        if self.head is None:
            # set the head and tail to this node if there was no previous
            # item in this LinkedList
            self.head = self.tail = node
        else:
            # if there was an item, add the item to the end of the LinkedList
            self.tail.next = node
        self.tail = node

    def remove(self, data):
        # prime the function with the head item...
        curr_node = self.head
        prev_node = None

        while curr_node:
            # check for a match, then remove it from the list
            if curr_node.data == data:
                # remove the previous node's next to the current node's next
                if prev_node:
                    prev_node.next = curr_node.next
                else:
                    self.head = curr_node.next
            prev_node = curr_node
            curr_node = curr_node.next

    def exists(self, data):
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                # we found it!
                return True
            curr_node = curr_node.next
        return False

    def __str__(self):
        return 'Head: {}, Tail: {}'.format(self.head, self.tail)

    class Node():

        def __init__(self, data, next_node):
            self.data = data
            self.next = next_node

        def __str__(self):
            return 'Data: {}, Next:{}'.format(self.data, self.next)

if __name__ == '__main__':
    s = SingleLinkedList()
    s.append(15)
    s.show()
    s.append(5)
    s.show()
    s.append(2)
    s.show()
    s.append(29)
    s.show()

    assert(s.exists(5) is True)
    assert(s.exists(239847) is False)

    s.remove(2)
    s.show()
    s.remove(5)
    assert(s.exists(5) is False)
    s.show()
    s.remove(15)
    s.show()

    my_hash_table = HashTable()
    my_hash_table.insert('Steve')  # should be 3
    my_hash_table.insert('Spark')  # should be 9
    my_hash_table.insert('Notes')
    assert(my_hash_table.exists('Steve') is True)  # should be true
    assert(my_hash_table.exists('steve') is False)  # should be false
    my_hash_table.remove('Steve')
    assert(my_hash_table.exists('Steve') is False)  # should be false now

#     print(my_hash_table)
