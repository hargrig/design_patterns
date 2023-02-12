# In Strategy pattern, a class behavior or its algorithm can be changed at run time.
# This type of design pattern comes under behavior pattern.
# In Strategy pattern, we create objects which represent various strategies and a
# context object whose behavior varies as per its strategy object.
# The strategy object changes the executing algorithm of the context object.


from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def do_operation(self, num1: int, num2: int):
        raise NotImplemented

class OperationAdd(Strategy):
    def do_operation(self, num1: int, num2: int):
        return num1 + num2

class OperationMul(Strategy):
    def do_operation(self, num1: int, num2: int):
        return num1 * num2

class OperationSub(Strategy):
    def do_operation(self, num1: int, num2: int):
        return num1 - num2


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        print("Changing the strategy of our context")
        self._strategy = strategy

    def exec_strategy(self, num1: int, num2: int) -> int:
        return self._strategy.do_operation(
            num1, num2
        )


class DemoStrategyPattern:
    def main(self):
        context = Context(OperationAdd())
        print(f"10 + 5 = {context.exec_strategy(10, 5)}")

        context.strategy = OperationSub()		
        print(f"10 - 5 = {context.exec_strategy(10, 5)}")

        context.strategy = OperationMul()		
        print(f"10 * 5 = {context.exec_strategy(10, 5)}")


if __name__ == "__main__":
    demo = DemoStrategyPattern()
    demo.main()
