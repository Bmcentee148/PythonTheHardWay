# This will contain functions that implement common sorting algorithms

class tNum(object) :

    def __init__(self, num) :
        self.num = num

    def __eq__(self, other) :
        return self.num == other.num

    def __lt__(self, other) :
        return self.num < other.num

    def count_aloud(self) :
        for i in range(1, self.num + 1) :
            print num,
        print '\n'

def insertion_sort(elems) :
    for last_index in range(1, len(elems)) :
        for compared_index in range(last_index) :
            if elems[last_index] < elems[compared_index] :
                swap(elems, last_index, compared_index)
                break

def swap(elems,i,j) :
    """Swap the position of two elements in a list.

    Args:
        elems - the list in need of swapping
        i - the index of the first element to swap
        j - the index of the second element to swap
    """
    elems[i], elems[j] = elems[j], elems[i]

