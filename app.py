"""
    Napisz program, w którym sumujesz parzyste elementy kolekcji liczb,
    a otrzymany wynik prezentujesz w formacie JSON.
"""
import json

def sum_even_numbers(numbers: list[int]) -> int:
    return sum([number for number in numbers if number % 2 == 0])

def main() -> None:
    numbers = [1, 2, 3, 4]
    json_str = json.dumps({'sum': sum_even_numbers(numbers)}, indent=4)
    print(json_str)

if __name__ == '__main__':
    main()
