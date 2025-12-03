def main() -> None:
    # Read 10 integers into a list
    numbers = list(map(int, input("Enter 10 integers: ").split()))
    if len(numbers) != 10:
        print("Error: you must enter exactly 10 integers.")
        return

    # Example 1: squares using list comprehension
    squares = [x * x for x in numbers]
    print("Numbers:", numbers)
    print("Squares:", squares)

    # Example 2: only even numbers using filter
    evens = [x for x in numbers if x % 2 == 0]
    print("Even numbers:", evens)

    # Example 3: min, max, sum
    print("Min:", min(numbers))
    print("Max:", max(numbers))
    print("Sum:", sum(numbers))


if __name__ == "__main__":
    main()
