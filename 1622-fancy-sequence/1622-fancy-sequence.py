class Fancy:
    def __init__(self):
        self.mod = 10**9 + 7
        self.seq = []
        self.a = 1  # Cumulative multiplier
        self.b = 0  # Cumulative increment

    def append(self, val: int) -> None:
        # We store val 'normalized' against current a and b
        # val = (stored_val * a + b) -> stored_val = (val - b) * inv(a)
        inv_a = pow(self.a, self.mod - 2, self.mod)
        self.seq.append(((val - self.b) * inv_a) % self.mod)

    def addAll(self, inc: int) -> None:
        # (x * a + b) + inc -> x * a + (b + inc)
        self.b = (self.b + inc) % self.mod

    def multAll(self, m: int) -> None:
        # (x * a + b) * m -> x * (a * m) + (b * m)
        self.a = (self.a * m) % self.mod
        self.b = (self.b * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        # Apply the current transformation to the stored normalized value
        return (self.seq[idx] * self.a + self.b) % self.mod