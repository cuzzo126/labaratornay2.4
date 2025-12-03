def main() -> None:
    a = list(map(int, input("Enter 10 integers: ").split()))
    if len(a) != 10:
        print("Error: you must enter exactly 10 integers.")
        return

    max_val = max(a)
    max_idx = a.index(max_val)

    # build new list with swapped elements using list comprehension
    b = [
        max_val if i == 0
        else a[0] if i == max_idx
        else x
        for i, x in enumerate(a)
    ]

    print("Transformed array (LC):", b)


if __name__ == "__main__":
    main()
