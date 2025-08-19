class super:
    functions = []
    funced = []
    def run(self, idx, *args, **kwargs):
        for f in self.functions:
           try:
             f(*args,**kwargs)
              self.funced.append(str(f))
            except Exception as e:
              pass
        return self.funced
    def this(self, func):
        self.functions.append(func)