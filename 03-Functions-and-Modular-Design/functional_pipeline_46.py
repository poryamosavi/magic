from functools import reduce

def pipeline_stage_46(data: list[float], scale: float = 3.30) -> float:
    normalized = list(map(lambda v: round(v * scale, 4), data))
    filtered = list(filter(lambda v: v > 23.0, normalized))
    return round(reduce(lambda a, b: a + b, filtered, 0.0), 4)

if __name__ == '__main__':
    print('Pipeline Output:', pipeline_stage_46([2.5, 10.0, 25.4, 40.2]))
