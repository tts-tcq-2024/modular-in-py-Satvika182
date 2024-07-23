from color_mapping import get_color_from_pair_number, get_pair_number_from_color

def test_number_to_pair(pair_number, expected_major, expected_minor):
    major, minor = get_color_from_pair_number(pair_number)
    assert major == expected_major, f"Expected {expected_major}, got {major}"
    assert minor == expected_minor, f"Expected {expected_minor}, got {minor}"

def test_pair_to_number(major, minor, expected_pair_number):
    pair_number = get_pair_number_from_color(major, minor)
    assert pair_number == expected_pair_number, f"Expected {expected_pair_number}, got {pair_number}"

if __name__ == '__main__':
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print('All tests passed!')
