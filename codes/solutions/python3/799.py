class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        glasses = [[poured if i == 0 and j == 0 else 0 for i in range(j + 1)] for j in range(query_row + 1)]
        for i in range(1, len(glasses)):
            for j in range(len(glasses[i])):
                if j - 1 >= 0 and glasses[i - 1][j - 1] > 1: glasses[i][j] += (glasses[i - 1][j - 1] - 1) / 2
                if j <= i - 1 and glasses[i - 1][j] > 1: glasses[i][j] += (glasses[i - 1][j] - 1) / 2
        return glasses[query_row][query_glass] if glasses[query_row][query_glass] <= 1 else 1

    def champagneTower2(self, poured: int, query_row: int, query_glass: int) -> float:
        rows, y, i = [[1]] if poured >= 1 else [[poured]], poured - 1, 1
        while i <= query_row and y > 0:
            next_row = [1] * (i + 1)
            access_div = y / (2.0 * i)
            if access_div < 1:
                next_row[0] = next_row[-1] = access_div
            if 2.0 * access_div < 1:
                next_row[1:-1] = [2.0 * access_div] * (len(next_row) - 2)
            rows.append(next_row)
            y -= i + 1
            i += 1
        return rows[query_row][query_glass] if len(rows) > query_row else 0.0


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0.0] * 101 for _ in range(101)]
        glasses[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                if glasses[i][j] >= 1:
                    glasses[i + 1][j] += (glasses[i][j] - 1) / 2.0
                    glasses[i + 1][j + 1] += (glasses[i][j] - 1) / 2.0
                    glasses[i][j] = 1

        return glasses[query_row][query_glass]


print(Solution().champagneTower2(25, 6, 1))
print(Solution().champagneTower(25,6, 1))
