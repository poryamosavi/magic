def transform_records_42(items: list[int]) -> dict:
    grouped = {'positive': [x for x in items if x > 0], 'negative': [x for x in items if x < 0]}
    freq = {x: items.count(x) for x in set(items)}
    return {'id': 42, 'grouped': grouped, 'frequency': freq}

if __name__ == '__main__':
    sample = [42, -42, 84, 42, 0, 15]
    print(transform_records_42(sample))
