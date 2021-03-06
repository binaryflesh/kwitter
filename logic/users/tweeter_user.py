from users import user_management


class TweeterUser:
    def __init__(self, user_id=None, handle=None):
        self.user_id = user_id
        self.handle = handle

    def __conform__(self, protocol):
        pass

    def build_from_row(kwdb, row):
        if kwdb.db_type == 'sqlite3':
            return row
        else:
            raise Exception

    def build_from_row_sqlite3(row):
        id = TweeterUser._get_id_from_row_sqlite3(row)
        handle = TweeterUser._get_handle_from_row_sqlite3(row)
        return TweeterUser(id, handle)

    def build_from_rows_sqlite3(rows):
        return [TweeterUser.build_from_row_sqlite3(row) for row in rows]

    def _get_id_from_row_sqlite3(row):
        return row[0]

    def _get_handle_from_row_sqlite3(row):
        return row[1]

    def __str__(self):
        return str(self.handle) + ' (' + str(self.user_id) + ')'

    def __dbadd__(self, kwdb):
        user_management.add_user_auto(kwdb, self)