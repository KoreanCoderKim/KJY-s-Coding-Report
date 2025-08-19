class super:
    value = None
    def run(self, func):
        return func(self.value)
    def this(self, v):
        self.value = v

S = super()
S.this(5)
print(S.run(type))