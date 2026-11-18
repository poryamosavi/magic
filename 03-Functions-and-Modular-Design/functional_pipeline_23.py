from functools import reduce

def pipeline_stage_23(data: list[float], scale: float = 2.15) -> float:
    normalized = list(map(lambda v: round(v * scale, 4), data))
    filtered = list(filter(lambda v: v > 11.5, normalized))
    return round(reduce(lambda a, b: a + b, filtered, 0.0), 4)

if __name__ == '__main__':
    print('Pipeline Output:', pipeline_stage_23([2.5, 10.0, 25.4, 40.2]))
