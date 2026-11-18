def transform_records_11(items: list[int]) -> dict:
    grouped = {'positive': [x for x in items if x > 0], 'negative': [x for x in items if x < 0]}
    freq = {x: items.count(x) for x in set(items)}
    return {'id': 11, 'grouped': grouped, 'frequency': freq}

if __name__ == '__main__':
    sample = [11, -11, 22, 11, 0, 15]
    print(transform_records_11(sample))
