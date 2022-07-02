from cls_stack.cls_stack import Stack

sample_dict = {
    'first_str': '(((([{}]))))',
    'second_str': '[([])((([[[]]])))]{()}',
    'third_str': '{{[()]}}',
    'fourth_str': '}{}',
    'fifth_str': '{{[(])]}}',
    'sixth_str': '[[{())}]'
}

if __name__ == '__main__':
    stack = Stack()
    for key, value in sample_dict.items():
        print(f'The {key}: {value} is {stack.is_balanced(value)}')
