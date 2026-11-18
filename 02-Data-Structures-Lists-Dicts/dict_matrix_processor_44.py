def transform_records_44(items: list[int]) -> dict:
    grouped = {'positive': [x for x in items if x > 0], 'negative': [x for x in items if x < 0]}
    freq = {x: items.count(x) for x in set(items)}
    return {'id': 44, 'grouped': grouped, 'frequency': freq}

if __name__ == '__main__':
    sample = [44, -44, 88, 44, 0, 15]
    print(transform_records_44(sample))
