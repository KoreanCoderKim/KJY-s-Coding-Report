class super:
    functions = []
    def run(self, idx, *args, **kwargs):
        return self.functions[idx](*args, **kwargs)
    def this(self, func):
        self.functions.append(func)