##checker_2

def adv_print(*args, **kwargs):

    arguments_info = dict(**kwargs)

    if 'sep' not in arguments_info:
        arguments_info['sep'] = ' '
    else:
        arguments_info['sep'] = arguments_info['sep']

    if 'end' not in arguments_info:
        arguments_info['end'] = '\n'
    else:
        arguments_info['end'] = arguments_info['end']
##    arguments_info['end'] = '\n'

    if 'start' not in arguments_info:
        arguments_info['start'] = '\n'
    else:
        arguments_info['start'] = arguments_info['start']
##    arguments_info['start'] = '\n'

    if 'max_line' not in arguments_info:
        arguments_info['max_line'] = 79
    else:
        arguments_info['max_line'] = arguments_info['max_line']

    arguments_info['max_line_sep'] = '\n'

##    def max_line(item):
##
##        if len(item) > arguments_info['max_line']:
##            item[:[arguments_info['max_line']]] + '\n'

    def item_generator(item):
        start = 0
        end = len(args)
        while start < end:
            arguments_to_print = args[start]
            yield arguments_to_print
            start += 1

##    arguments_to_print = args
##    if len(args) > 1:
##        arguments_to_print = []
##        for item in args:
##            arguments_to_print = item + item
       
    for item in args:
        if type(item) == str:
            arguments_to_print = f'{arguments_info["sep"]}'.join(args)
        else:
            arguments_to_print = item

    arguments_to_print = args[0]
    
    print(arguments_to_print[:[arguments_info['max_line']]])

    def max_line(item):

        if len(item) > arguments_info['max_line']:
            item[:[arguments_info['max_line']]] + '\n'

##    print(type(arguments_to_print))
##    print(type(args))
##    arguments_to_print_2 = []
##
##    for item in arguments_to_print:
##        new_item = f'\n{item}'
##        arguments_to_print_2.append(new_item)
##
##    print(arguments_to_print_2)
##    arguments_to_print.clear()
##    arguments_to_print.extend(arguments_to_print_2)
##    print([*args])
##
##    for item in arguments_to_print:
##        print(item)

##    print(arguments_to_print[0].index('dog'))
##    print(arguments_to_print[0])
##    print(arguments_to_print_2)

##    for item in arguments_to_print[0]:
##        new_item = arguments_info['start'] + item
##        item.replace(item, new_item)

##    for item in arguments_to_print:
##        for i in item:
##            new_item = arguments_info['start'] + i
##            item.remove(item.index(i))
##            item.insert(item.index(i), new_item)
##
##    print(arguments_to_print)
            
##        print(new_item)
##        arguments_to_print[0].insert(arguments_to_print[0].index(item), new_item)
##        arguments_to_print_2.pop(arguments_to_print_2.index(item))
##        arguments_to_print[0].insert(arguments_to_print[0].index(item), new_item)
##        print(item)
        
##    print(type(arguments_to_print[0]))

##    for item in 
##    sep = arguments_info['sep'] = ' '
##    end = arguments_info['end'] = '\n'

##    print(arguments_info)
    return print(('%s%s')%(arguments_info['start'], max_line(arguments_to_print)), sep=arguments_info['sep'], end=arguments_info['end'])
##    return print(('%s%s')%(arguments_info['start'], [item for item in item_generator(args)]), sep=arguments_info['sep'], end=arguments_info['end'])
##    return print(('%s%s')%(arguments_info['start'], args), sep=arguments_info['sep'], end=arguments_info['end'])

##adv_print({'cat': 11, 'dog': 12}, '1', sep =', ', end='\n\n')
##adv_print({'cat': 11, 'dog': 12}, sep =', ', end='\n\n')
adv_print('Кот ест блинчики. Кот ест блинчики. Кот ест блинчики. Кот ест блинчики. Кот ест блинчики. Кот ест блинчики. Кот ест блинчики.', sep =', ', end='\n\n')

##print('cat', 'dog', sep=', ')
