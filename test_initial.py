from fizzbuzz import process

def test_dummy():
    pass

def test_number_one():
    assert(process(1) == 1)

def test_number_simple_number():
    assert(process(2) == 2)

def test_multiple():
    assert(process(3) == "fizz")
    assert(process(6) == "fizz")
    assert(process(9) == "fizz")
    assert(process(90) == "fizz")

def test_multiple_of_five_buzz():
    assert(process(5) == "buzz")
    assert(process(10) == "buzz")

def test_fizzbuzz():
    assert(process(15) == "fizzbuzz")
    assert(process(30) == "fizzbuzz")
    assert(process(45) == "fizzbuzz")
    assert(process(90) == "fizzbuzz")