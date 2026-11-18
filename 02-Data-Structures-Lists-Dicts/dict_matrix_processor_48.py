def transform_records_48(items: list[int]) -> dict:
    grouped = {'positive': [x for x in items if x > 0], 'negative': [x for x in items if x < 0]}
    freq = {x: items.count(x) for x in set(items)}
    return {'id': 48, 'grouped': grouped, 'frequency': freq}

if __name__ == '__main__':
    sample = [48, -48, 96, 48, 0, 15]
    print(transform_records_48(sample))
