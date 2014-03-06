class Clc():
    def __init__(self):
        self.history = []
        self.vars = {}

    def push(self, equation):
        self.history.append(equation)
        stack = self.parse(equation)
        result = self.execute(stack)
        return result

    def parse(self, equation):
        terms = equation.split('+')
        if len(terms) == 1:
            return {"return": float(terms[0])}
        result = {"add": [self.parse(t) for t in terms]}
        return result

    def execute(self, stack):
        results = []
        print stack
        for k, v in stack.iteritems():
            if k == "return":
                results.append(v)
            elif k == "add":
                results.append(sum([self.execute(t) for t in v]))
        return results
