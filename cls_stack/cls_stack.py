class Stack:

    def __init__(self, sample: str):
        self.stack_list = list(sample)

    def isEmpty(self):
        return self.stack_list == []

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        return self.stack_list[len(self.stack_list) - 1]

    def size(self):
        return len(self.stack_list)

    def isBalanced(self, sample_stack: list):
        half_stack = len(sample_stack) / 2

        for idx in range(0, half_stack):
            if sample_stack[idx] != sample_stack[len(sample_stack) - idx]:
                return 'Unbalanced'
        return 'Balanced'

    def isBalanced(self):

        if len(self.stack_list) % 2 != 0:
            return 'Unbalanced'

        half_stack = int(len(self.stack_list)) / 2
        print(f'half_stack = {half_stack}')

        for idx in range(0, int(half_stack)):
            if self.stack_list[idx] != self.stack_list[len(self.stack_list)-1 - idx]:
                print(f'{self.stack_list[idx]} != {self.stack_list[len(self.stack_list)-1 - idx]}')
                return 'Unbalanced'
        return 'Balanced'
