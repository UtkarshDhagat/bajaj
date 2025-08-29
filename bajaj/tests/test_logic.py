from bfhl.logic import process_payload

def test_example_a():
    data = ["a", "1", "334", "4", "R", "$"]
    out = process_payload(data)
    assert out.odd_numbers == ["1"]
    assert out.even_numbers == ["334", "4"]
    assert out.alphabets == ["A", "R"]
    assert out.special_characters == ["$"]
    assert out.sum_numbers == 339
    assert out.concat_string == "Ra"

def test_example_c():
    data = ["A", "ABcD", "DOE"]
    out = process_payload(data)
    assert out.odd_numbers == []
    assert out.even_numbers == []
    assert out.alphabets == ["A", "ABCD", "DOE"]
    assert out.special_characters == []
    assert out.sum_numbers == 0
    assert out.concat_string == "EoDdCbAa"
