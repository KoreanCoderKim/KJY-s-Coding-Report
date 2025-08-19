class super:
    functions = []
    def run(self, idx, v):
        return self.functions[idx](v)
    def this(self, func):
        self.functions.append(func)

S = super()
S.this(type)
S.this(print)
S.run(1, S.run(0, "str"))