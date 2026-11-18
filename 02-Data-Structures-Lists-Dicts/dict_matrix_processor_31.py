def transform_records_31(items: list[int]) -> dict:
    grouped = {'positive': [x for x in items if x > 0], 'negative': [x for x in items if x < 0]}
    freq = {x: items.count(x) for x in set(items)}
    return {'id': 31, 'grouped': grouped, 'frequency': freq}

if __name__ == '__main__':
    sample = [31, -31, 62, 31, 0, 15]
    print(transform_records_31(sample))
