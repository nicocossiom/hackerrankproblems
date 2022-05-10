# Enter your code here. Read input from STDIN. Print output to STDOUT
class queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, elem):
        self.queue.append(elem)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]


if __name__ == "__main__":
    queries = int(input())
    q = queue()
    for _ in range(queries):
        op = input().split(" ")
        op_arg = None
        op_code = int(op[0])
        if len(op) == 2:
            op_arg = int(op[1])
        if op_code == 1:
            q.enqueue(op_arg)
        if op_code == 2:
            q.dequeue()
        if op_code == 3:
            print(q.peek())
