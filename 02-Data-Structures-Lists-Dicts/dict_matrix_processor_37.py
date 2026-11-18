def transform_records_37(items: list[int]) -> dict:
    grouped = {'positive': [x for x in items if x > 0], 'negative': [x for x in items if x < 0]}
    freq = {x: items.count(x) for x in set(items)}
    return {'id': 37, 'grouped': grouped, 'frequency': freq}

if __name__ == '__main__':
    sample = [37, -37, 74, 37, 0, 15]
    print(transform_records_37(sample))
