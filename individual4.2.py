from functools import reduce
from operator import mul


def main() -> None:
    nums = list(map(float, input("Enter real numbers separated by space: ").split()))
    if not nums:
        print("Error: empty list")
        return

    # sum of negative elements (LC)
    neg_sum = sum(x for x in nums if x < 0)

    min_val = min(nums)
    max_val = max(nums)
    min_idx = nums.index(min_val)
    max_idx = nums.index(max_val)

    start = min(min_idx, max_idx) + 1
    end = max(min_idx, max_idx)

    middle = nums[start:end]

    prod = 1.0
    if middle:
        prod = reduce(mul, middle, 1.0)

    print("Sum of negative elements:", neg_sum)
    print("Product of elements between min and max:", prod)


if __name__ == "__main__":
    main()
