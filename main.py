from cls_stack.cls_stack import Stack

if __name__ == '__main__':
    first_str = Stack('(((([{}]))))')
    print(first_str.isBalanced())
    second_str = Stack('[([])((([[[]]])))]{()}')
    print(second_str.isBalanced())
