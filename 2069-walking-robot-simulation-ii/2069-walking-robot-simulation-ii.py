class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = 0
        self.moved = False
        # The total number of unique positions on the boundary
        # Note: (W-1) + (H-1) + (W-1) + (H-1)
        self.perimeter = 2 * (width + height - 2)

    def step(self, num: int) -> None:
        self.moved = True
        # Modular arithmetic handles large 'num' efficiently
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> list[int]:
        curr = self.pos
        # 1. Bottom edge: (0,0) to (W-1, 0)
        if curr <= self.w - 1:
            return [curr, 0]
        
        # 2. Right edge: (W-1, 1) to (W-1, H-1)
        curr -= (self.w - 1)
        if curr <= self.h - 1:
            return [self.w - 1, curr]
        
        # 3. Top edge: (W-2, H-1) to (0, H-1)
        curr -= (self.h - 1)
        if curr <= self.w - 1:
            return [self.w - 1 - curr, self.h - 1]
        
        # 4. Left edge: (0, H-2) to (0, 1)
        curr -= (self.w - 1)
        return [0, self.h - 1 - curr]

    def getDir(self) -> str:
        # Special case for origin
        if self.pos == 0:
            return "South" if self.moved else "East"
        
        # Thresholds for direction changes
        east_limit = self.w - 1
        north_limit = (self.w - 1) + (self.h - 1)
        west_limit = 2 * (self.w - 1) + (self.h - 1)
        
        if 1 <= self.pos <= east_limit:
            return "East"
        elif east_limit < self.pos <= north_limit:
            return "North"
        elif north_limit < self.pos <= west_limit:
            return "West"
        else:
            return "South"
