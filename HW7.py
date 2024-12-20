class Polynomial:
    def __init__(self, coefficients):
        self._coefficients = coefficients

    def degree(self):
        return len(self._coefficients) - 1

    def __repr__(self):
        terms = []
        for i, coef in enumerate(self._coefficients):
            if coef == 0:
                continue
            term = f"{coef}"
            if i == 1:
                term += "x"
            elif i > 1:
                term += f"x^{i}"
            terms.append(term)
        return " + ".join(terms[::-1]) or "0"

    def __call__(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(self._coefficients))

    def __add__(self, other):
        max_degree = max(self.degree, other.degree)
        new_coefficients = [0] * (max_degree + 1)
        for i in range(max_degree + 1):
            coef1 = self._coefficients[i] if i <= self.degree else 0
            coef2 = other._coefficients[i] if i <= other.degree else 0
            new_coefficients[i] = coef1 + coef2
        return Polynomial(new_coefficients)

    def __sub__(self, other):
        max_degree = max(self.degree, other.degree)
        new_coefficients = [0] * (max_degree + 1)
        for i in range(max_degree + 1):
            coef1 = self._coefficients[i] if i <= self.degree else 0
            coef2 = other._coefficients[i] if i <= other.degree else 0
            new_coefficients[i] = coef1 - coef2
        return Polynomial(new_coefficients)

    def __mul__(self, other):
        result_degree = self.degree + other.degree
        result_coefficients = [0] * (result_degree + 1)
        for i, coef1 in enumerate(self._coefficients):
            for j, coef2 in enumerate(other._coefficients):
                result_coefficients[i + j] += coef1 * coef2
        return Polynomial(result_coefficients)

    def derivative(self):
        if self.degree == 0:
            return Polynomial([0])
        new_coefficients = [i * coef for i, coef in enumerate(self._coefficients)][1:]
        return Polynomial(new_coefficients)

    def evaluate(self, x):
        return self.__call__(x)


class QuadraticPolynomial(Polynomial):
    def __init__(self, coefficients):
        if len(coefficients) != 3:
            raise ValueError("У квадратичного полинома 3 коэффициента")
        super().__init__(coefficients)

    def discriminant(self):
        a, b, c = self._coefficients[2], self._coefficients[1], self._coefficients[0]
        return b**2 - 4 * a * c

    def find_roots(self):
        a, b, c = self._coefficients[2], self._coefficients[1], self._coefficients[0]
        d = self.discriminant()
        if d < 0:
            return "Корней нет"
        elif d == 0:
            root = -b / (2 * a)
            return (root,)
        else:
            root1 = (-b + d**0.5) / (2 * a)
            root2 = (-b - d**0.5) / (2 * a)
            return root1, root2