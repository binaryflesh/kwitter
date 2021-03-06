'''
This is intended for debug or for tools.

Normally, this probably shouldn't be called...
'''

from tweets import tweet
from users import tweeter_user
from tags import tag as tag_module

from database.unsupported_db_type_exception import UnsupportedDBTypeException


def get_all_users(kwdb):
    if kwdb.db_type == 'sqlite3':
        return get_all_users_sqlite3(kwdb)
    else:
        raise UnsupportedDBTypeException

def get_all_users_sqlite3(kwdb):
    cursor = kwdb.cursor()
    rows = cursor.execute('select * from USERS').fetchall()
    return [tweeter_user.TweeterUser.build_from_row_sqlite3(row) for row in rows]

def get_all_tweets(kwdb):
    if kwdb.db_type == 'sqlite3':
        return get_all_tweets_sqlite3(kwdb)
    else:
        raise UnsupportedDBTypeException(kwdb.db_type)

def get_all_tags(kwdb):
    if kwdb.db_type == 'sqlite3':
        return get_all_tags_sqlite3(kwdb)
    else:
        raise UnsupportedDBTypeException(kwdb.db_type)

def get_all_tags_sqlite3(kwdb):
    cursor = kwdb.cursor()
    rows = cursor.execute('select TAG_ID, FIELD, COUNT from TAGS').fetchall()
    return [tag_module.Tag(tag_id=row[0], field=row[1], count=row[2]) for row in rows]

def get_all_tweets_sqlite3(kwdb):
    cursor = kwdb.cursor()
    rows = cursor.execute('select * from TWEETS').fetchall()
    return [tweet.Tweet.build_from_row(row) for row in rows]