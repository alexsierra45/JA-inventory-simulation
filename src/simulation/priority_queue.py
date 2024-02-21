import queue

class EventQueue:
    def __init__(self):
        self.queue = queue.PriorityQueue()

    def push(self, event):
        self.queue.put(event)

    def pop(self):
        return self.queue.get()

    def empty(self):
        return self.queue.empty()