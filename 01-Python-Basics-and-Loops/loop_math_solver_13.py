def compute_series_13(limit: int = 130) -> dict:
    evens = [x for x in range(1, limit + 1) if x % 2 == 0]
    squares = [x ** 2 for x in range(1, min(limit, 20) + 1)]
    return {'module_id': 13, 'even_sum': sum(evens), 'max_square': max(squares, default=0)}

if __name__ == '__main__':
    print(compute_series_13())
