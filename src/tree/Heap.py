class Heap(object):
    size = 0
    end = 0
    bin_tree = None
    comparer = None

    def __init__(self, size, comparer):
        self.comparer = comparer
        self.size = size
        self.bin_tree = [None] * (size + 1)

    def current_size(self):
        return self.end

    def add(self, val):
        if self.end < self.size:
            self.end = self.end + 1
            self.bin_tree[self.end] = val
            self.perculate_up()
        else:
            print("Error: heap is full")

    def remove(self):
        if self.end > 0:
            self.bin_tree[1] = self.bin_tree[self.end]
            self.bin_tree[self.end] = None
            self.end = self.end - 1
            self.perculate_down()
        else:
            print("Error: heap is empty")

    def perculate_up(self):
        i = j = self.end
        while j != 1:
            if i%2 == 0:
                i = i//2
            else:
                i = (i-1)//2
            if self.comparer(self.bin_tree[j], self.bin_tree[i]):
                self.swap(i,j)
            j = i

    def perculate_down(self):
        curr = left = right = 1
        while True:
            #Get children of current index
            leftChild = left*2
            rightChild = (right*2)+1

            #If either child is NULL mark the index so that path isn't taken
            if left != None and leftChild <= self.end:
                left = leftChild
            else:
                left = None

            if right != None and rightChild <= self.end:
                right = rightChild
            else:
                right = None

            #Determine which child should be swapped if any, based on comparer.
            #Case: Both children aren't NULL (check to see which is larger)
            if left != None and right != None:
                if self.comparer(self.bin_tree[left], self.bin_tree[right]):
                    if self.comparer(self.bin_tree[left], self.bin_tree[curr]):
                        self.swap(curr, left)
                        curr = left
                    else:
                        break;

                elif self.comparer(self.bin_tree[right], self.bin_tree[curr]):
                        self.swap(curr, right)
                        curr = right
                else:
                    break;

            #Case: Left child isn't NULL
            elif left != None:
                    if self.comparer(self.bin_tree[left], self.bin_tree[curr]):
                        self.swap(curr, left)
                    else:
                        break;

            #Case: Right child isn't NULL
            elif right != None:
                    if self.comparer(self.bin_tree[right], self.bin_tree[curr]):
                        self.swap(curr, right)
                    else:
                        break;
            else:
                break;

            #Set all indecies to next currents new location
            left = right = curr

    def peek(self):
        print(self.bin_tree[1])

    def print_bin_tree(self, index, level):
        if (index * 2) <= self.end:
            self.print_bin_tree(index*2, level+1)

        spacing = ""
        for x in range(level*10):
            spacing = spacing + " "

        print("%s%d"%(spacing, self.bin_tree[index]))

        if (index*2)+1 <= self.end:
            self.print_bin_tree((index*2)+1, level+1)

    def swap(self, val1, val2):
        temp = self.bin_tree[val1]
        self.bin_tree[val1] = self.bin_tree[val2]
        self.bin_tree[val2] = temp


