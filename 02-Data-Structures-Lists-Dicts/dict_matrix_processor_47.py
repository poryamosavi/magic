def transform_records_47(items: list[int]) -> dict:
    grouped = {'positive': [x for x in items if x > 0], 'negative': [x for x in items if x < 0]}
    freq = {x: items.count(x) for x in set(items)}
    return {'id': 47, 'grouped': grouped, 'frequency': freq}

if __name__ == '__main__':
    sample = [47, -47, 94, 47, 0, 15]
    print(transform_records_47(sample))
