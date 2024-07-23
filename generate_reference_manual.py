from color_mapping import MAJOR_COLORS, MINOR_COLORS, get_pair_number_from_color, color_pair_to_string

def generate_color_code_reference():
    reference =[]
    return [f'{pair}: {color_pair_to_string(*get_color_from_pair_number(pair))}' 
            for pair in range(1, 26)]


if __name__ == '__main__':
    reference = generate_color_code_reference()
    
