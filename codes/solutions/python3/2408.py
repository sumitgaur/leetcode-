from collections import defaultdict


class SQL:
    def __init__(self, names, columns):
        self.names = names
        self.columns = columns
        self.tables = defaultdict(dict)
        self.next_ids = [0] * len(names)

        # table 1[
        #   [a1,b1,c1],
        #   [a2,b2,c2]
        #  ],
        # table2[
        #   [a1,b1,c1],
        #   [a2,b2,c2]
        #  ]

    def insert(self, table_ind, row):
        if len(row) == self.columns[table_ind]:
            self.next_ids[table_ind] += 1
            self.tables[table_ind][self.next_ids[table_ind]] = row
            return True
        return False

    def remove(self, table_ind, rmv_id):
        self.tables[table_ind].pop(rmv_id)

    def select(self, table_ind, row_id, col_id):
        return self.tables[table_ind][row_id][col_id]

    def export(self, table_ind):
        print(self.tables[table_ind])


sql = SQL(["users"], [3])
sql.insert(0, ["Alice", "25", "NYC"])
sql.insert(0, ["Bob", "30", "LA"])
sql.remove(0, 1)
sql.insert(0, ["Charlie", "35", "SF"])
sql.export(0, )
