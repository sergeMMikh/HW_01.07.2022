class Stack:
    balanced_dic = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    def __init__(self):
        self.stack_list = []

    def clean(self):
        self.stack_list.clear()

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

    def is_balanced(self, sample: str):

        sample_list = list(sample)

        if not self.isEmpty():
            self.clean()

        if len(self.stack_list) % 2 != 0:
            return 'unbalanced'

        for item in sample_list:
            if item in self.balanced_dic.keys():
                self.push(item)
            else:
                if self.isEmpty():
                    return 'unbalanced'
                if item != self.balanced_dic.get(self.peek()):
                    return 'unbalanced'
                else:
                    self.pop()

        return 'balanced'
