def transform_records_41(items: list[int]) -> dict:
    grouped = {'positive': [x for x in items if x > 0], 'negative': [x for x in items if x < 0]}
    freq = {x: items.count(x) for x in set(items)}
    return {'id': 41, 'grouped': grouped, 'frequency': freq}

if __name__ == '__main__':
    sample = [41, -41, 82, 41, 0, 15]
    print(transform_records_41(sample))
