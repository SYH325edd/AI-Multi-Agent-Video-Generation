class BaseAgent:
    def __init__(self, name):
        self.name = name

    def run(self, state):
        raise NotImplementedError("必须实现run方法")