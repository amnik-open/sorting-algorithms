class BinaryHeap:
    heap = None

    def __init__(self, array=None):
        if array is not None:
            self.heap = array.copy()
            for i in reversed(range(len(array) // 2)):
                self._siftDown(i)
        else:
            self.heap = list()

    def insert(self, v):
        self.heap.append(v)
        self._siftUp(len(self.heap) - 1)

    def remove(self, i):
        self.heap[i] = float("-inf")
        self._siftUp(i)
        self.extractMIN()

    def extractMIN(self):
        answer = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftDown(0)
        return answer

    def _siftUp(self, i):
        while True:
            p = self._parent(i)
            if p is not None:
                if self.heap(i) < self.heap[p]:
                    self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                    i = p
                else:
                    break
            else:
                break

    def _siftDown(self, i):
        while True:
            if self._left_child(i) is None and self._right_child(i) is None:
                break
            min_index = i
            if self._left_child(i) is not None and self.heap[i] > self.heap[
                self._left_child(i)]:
                min_index =  self._left_child(i)
            if self._right_child(i) is not None and self.heap[min_index] > self.heap[
                self._right_child(i)]:
                min_index = self._right_child(i)
            if min_index == i:
                break
            self.heap[min_index], self.heap[i] = self.heap[i], self.heap[min_index]
            i = min_index

    def _left_child(self, i):
        if 0 <= 2 * i + 1 < len(self.heap):
            return 2 * i + 1
        return None

    def _right_child(self, i):
        if 0 <= 2 * i + 2 < len(self.heap):
            return 2 * i + 2
        return None

    def _parent(self, i):
        if 0 <= (i - 1) // 2 < len(self.heap):
            return (i - 1) // 2
        return None


def heap_sort(array):
    h = BinaryHeap(array)
    for i, _ in enumerate(array):
        array[i] = h.extractMIN()


array = list(map(int, input().split()))
heap_sort(array)
print(array)

