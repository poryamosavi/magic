def transform_records_49(items: list[int]) -> dict:
    grouped = {'positive': [x for x in items if x > 0], 'negative': [x for x in items if x < 0]}
    freq = {x: items.count(x) for x in set(items)}
    return {'id': 49, 'grouped': grouped, 'frequency': freq}

if __name__ == '__main__':
    sample = [49, -49, 98, 49, 0, 15]
    print(transform_records_49(sample))
