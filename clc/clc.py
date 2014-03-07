import numpy as np


class Clc():
    def __init__(self):
        self.history = []
        self.vars = {}

    def push(self, equation):
        print equation
        self.history.append(equation)
        stack = self.parse(equation)
        result = self.execute(stack)
        return result

    def parse(self, equation):
        print 'parsing', equation
        terms = equation.split('(', 1)
        if len(terms) > 1:
            # assume the parenthesis never closes
            idx = len(terms[1])

            # check if it actually does
            paren_count = 1
            for i, c in enumerate(terms[1]):
                if c == "(":
                    paren_count += 1
                if c == ")":
                    paren_count -= 1
                if paren_count == 0:
                    idx = i
                    break

            inner_stack = self.parse(terms[1][:idx])
            print "inner_stack:", inner_stack
            result = self.execute(inner_stack)
            print "inner result", result
            return self.parse(terms[0] + str(result) + terms[1][idx + 1:])

        terms = equation.split('+', 1)
        if len(terms) > 1:
            return {"add": [self.parse(t) for t in terms]}
        terms = equation.split('-', 1)
        if len(terms) > 1:
            # must check for negative number
            if len(terms[0]) == 0:
                terms[0] = "0"
            return {"subtract": [self.parse(t) for t in terms]}
        terms = equation.split('*', 1)
        if len(terms) > 1:
            return {"dot": [self.parse(t) for t in terms]}
        terms = equation.split('/', 1)
        if len(terms) > 1:
            return {"divide": [self.parse(t) for t in terms]}
        print terms
        return {"return": float(terms[0])}

    def execute(self, stack):
        result = None
        for k, v in stack.iteritems():
            if k == "return":
                result = v
            elif k == "add":
                terms = [self.execute(t) for t in v]
                result = np.add(*terms)
            elif k == "subtract":
                terms = [self.execute(t) for t in v]
                result = np.subtract(*terms)
            elif k == "dot":
                terms = [self.execute(t) for t in v]
                result = np.dot(*terms)
            elif k == "divide":
                terms = [self.execute(t) for t in v]
                result = np.divide(*terms)
        return result
