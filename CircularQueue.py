class CircularQueue():
    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0


    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    # -----------MODIFY BELOW--------------

    def __str__(self):
        """
	    This function displays the queue
	    :return: the printed queue
	    """
        if self.size == 0:
            return "Empty Stack"
        output = []
        for i in range(self.capacity):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))

    def is_empty(self):
        """
	    This function checks if the array is empty
	    :return: True if empty false otherwise
	    """
        if self.size == 0:
            return True
        else:
            return False

    def __len__(self):
        """
	    This function returns the amount of items in the queue
	    :return: the amount of items in the array
	    """
        return self.size

    def first_value(self):
        """
	    This function returns the front of the queue
	    :return: The front value of the array
	    """
        return self.data[self.head]
    def enqueue(self, val):
        """
	    This function adds the val to the back of the queue
	    :param: val The value to be added to the queue
	    :return: None
	    """
        if self.tail == self.capacity:
            self.tail = 0
        self.data[self.tail] = val
        self.tail += 1
        self.size += 1
        if self.size == self.capacity:
            self.grow()
    
    def dequeue(self):
        """
	    This function removes and returns the front value in the queue
	    :return: The value at the front of the queue
	    """
        if self.is_empty():
            return None
        else:
            head = self.data[self.head]
            self.data[self.head] = None
            if self.head == self.capacity:
                #index wraps around
                self.head = 0
            else:
                #index moves forward one
                self.head = self.head + 1
        self.size -= 1 
        if self.size <= (self.capacity//4):
            self.shrink()
        return head

    def grow(self):
        """
	    This function doubles the capacity of the array
	    """
        if self.tail > self.head:
            #when tail is larger than head
            ind_range = self.tail - self.head
        else:
            #when head is larger than tail
            ind_range = self.tail % self.head + (self.capacity - self.head)
        self.capacity = (self.capacity * 2)
        new_array = [None] * self.capacity
        for i in range(0, ind_range):
            new_array[i] = self.data[i]
        self.data = new_array
        self.head = 0
        
    def shrink(self):
        """
	    This function halves the capacity of the array as long as the capacity would
	    still be above 4
	    """
        if (self.capacity // 2) < 4:
            return 
        if self.tail > self.head:
            #when tail is larger than head
            ind_range = self.tail - self.head
        else:
            #when head is larger than tail
            ind_range = self.tail % self.head + (self.capacity - self.head)
        old_cap = self.capacity
        self.capacity = (self.capacity // 2)
        new_array = [None] * self.capacity
        j = self.head
        for i in range(0, ind_range):
            if j == old_cap:
                j = 0
            new_array[i] = self.data[j]
            j += 1
        self.data = new_array
        self.head = 0
        self.tail = self.size
        