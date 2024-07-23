MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def color_pair_to_string(major, minor):
    return f'{major} {minor}'

def get_color_from_pair_number(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise Exception('Major index out of range')
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major, minor):
    if major not in MAJOR_COLORS:
        raise Exception('Major index out of range')
    if minor not in MINOR_COLORS:
        raise Exception('Minor index out of range')
    return MAJOR_COLORS.index(major) * len(MINOR_COLORS) + MINOR_COLORS.index(minor) + 1
    
