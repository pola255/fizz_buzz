from fizz_buzz.fizz_buzz import fizz_buzz


def test_fizzBuzz():
    assert fizz_buzz(1) == 1
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(15) == "FizzBuzz"
    assert fizz_buzz(20) == "Buzz"
