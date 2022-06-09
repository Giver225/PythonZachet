class node():
    def __init__(self, walk=None, order=None, turn=None):
        self.walk = walk
        self.order = order
        self.turn = turn


class main():
    def __init__(self):
        self.a = node(walk=(0, 'b'))
        self.b = node(order=(1, 'c'), walk=(2, 'b'), turn=(3, 'e'))
        self.c = node(walk=(4, 'd'))
        self.d = node(turn=(5, 'e'))
        self.e = node(walk=(6, 'f'))
        self.f = node(walk=(7, 'g'), order=(8, 'd'))
        self.g = node(order=(9, 'g'))
        self.current = self.a

    def walk(self):
        if self.current.walk is None:
            raise KeyError
        ans = self.current.walk[0]
        exec(f'self.current = self.{self.current.walk[1]}')
        return ans

    def order(self):
        if self.current.order is None:
            raise KeyError
        ans = self.current.order[0]
        exec(f'self.current = self.{self.current.order[1]}')
        return ans

    def turn(self):
        if self.current.turn is None:
            raise KeyError
        ans = self.current.turn[0]
        exec(f'self.current = self.{self.current.turn[1]}')
        return ans


o = main()
example = ['walk', 'order', 'walk', 'walk', 'turn', 'turn', 'turn', 'walk', 'turn', 'turn', 'turn', 'order', 'walk']
for i in example:
    exec(f'print(o.{i}())')
