import sqlite3

class Database:

    def __init__(self) -> None:
        self.conn = sqlite3.connect(':memory:')
        self.cur = conn.cursor()

    def createTableIfNew(self) -> None:
        try:
            self.cur.execute("SELECT * FROM songTable")
            self.cur.fetchone()
        except:
            self.cur.execute('''CREATE TABLE songTable (
                                                        name VARCHAR(255),
                                                        data BLOB)''')

    def getData(self, name)-> list:
        self.cur.execute("SELECT data FROM songTable WHERE name =:name",{'name':name})
        return self.cur.fetchone()

    def updateData(self,name, data) -> None:
        '''This method can UPDATE or INSERT data into the db'''
        if self.getData(name):
            self.cur.execute("UPDATE songTable SET data =:data WHERE name =:name",{'name':name, 'data':data})
        else:
            self.cur.execute("INSERT INTO songTable VALUES (:name, :data)",{'name':name, 'data':data})
        self.conn.commit()

    def close(self) ->None:
        self.conn.close()

da  = '''[[{'#00ff80': (0.0, 255.99609375, 128.5)}]]'''
da1 = '''[[{'#FFFFFF': (0.0, 255.99609375, 128.5)}]]'''

db = Database()

db.updateData('test', da)
db.updateData('test1',da)
print(db.getData('test1'))
db.updateData('test1',da1)
print(db.getData('test1'))
db.close()