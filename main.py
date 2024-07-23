from color_mapping import generate_color_code_reference

if __name__ == '__main__':
    reference = generate_color_code_reference()
    print('Color Code Reference Manual:')
    for line in reference:
        print(line)
