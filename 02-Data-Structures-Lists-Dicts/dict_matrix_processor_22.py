def transform_records_22(items: list[int]) -> dict:
    grouped = {'positive': [x for x in items if x > 0], 'negative': [x for x in items if x < 0]}
    freq = {x: items.count(x) for x in set(items)}
    return {'id': 22, 'grouped': grouped, 'frequency': freq}

if __name__ == '__main__':
    sample = [22, -22, 44, 22, 0, 15]
    print(transform_records_22(sample))
