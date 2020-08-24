class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx < sx or ty < sy: return False

        if tx == sx: return True if (ty-sy) % sx == 0 else False

        if ty == sy: return True if (tx-sx) % sy == 0 else False

        return self.reachingPoints(sx, sy, tx-ty, ty) or\
               self.reachingPoints(sx, sy, tx, ty - tx)
