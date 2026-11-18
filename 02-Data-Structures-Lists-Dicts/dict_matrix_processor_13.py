def transform_records_13(items: list[int]) -> dict:
    grouped = {'positive': [x for x in items if x > 0], 'negative': [x for x in items if x < 0]}
    freq = {x: items.count(x) for x in set(items)}
    return {'id': 13, 'grouped': grouped, 'frequency': freq}

if __name__ == '__main__':
    sample = [13, -13, 26, 13, 0, 15]
    print(transform_records_13(sample))
