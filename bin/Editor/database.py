import json
import MySQLdb
import operator
from db_base import DbBase

class DBAccess(DbBase):
    cur = None
    db = None

    def __init__(self):
        self.db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.database)
        self.cur = self.db.cursor();

