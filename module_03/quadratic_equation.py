import math

EPSILON = 1e-08


def solve(a: float, b: float, c: float) -> tuple[float, float] | tuple[None, None]:
    """Вычисление корней квадратного уравнения.

        a•x^2 + b•x + c = 0

    Args:
        a, b, c: Коэффициенты квадратного уравнения.

    Raises:
        ValueError: Аргумент a = 0.
        TypeError: Хотя бы один аргумент не соответствует типу float.

    Returns:
        Корни квадратного уравнения x1 и x2.
    """
    if not all(isinstance(arg, float) for arg in (a, b, c)):
        raise TypeError("all arguments must be float")

    if abs(0. - a) <= EPSILON:
        raise ValueError("argument 'a' сan't be equal to 0")

    d = b ** 2 - 4 * a * c
    print(d)

    if d < -EPSILON:
        return (None, None)

    return (
        (- b + math.sqrt(d)) / 2 * a,
        (- b - math.sqrt(d)) / 2 * a,
    )
