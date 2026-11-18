def compute_series_31(limit: int = 310) -> dict:
    evens = [x for x in range(1, limit + 1) if x % 2 == 0]
    squares = [x ** 2 for x in range(1, min(limit, 20) + 1)]
    return {'module_id': 31, 'even_sum': sum(evens), 'max_square': max(squares, default=0)}

if __name__ == '__main__':
    print(compute_series_31())
