import sqlite3
import LoadGUI
class Database(object):
    def __init__(self,savename,level,lives,date,score):
        self.name=savename
        self.lives=lives
        self.level=level
        self.date=date
        self.score=score
        self.connection=sqlite3.connect("pacman.db")
        self.new1=[()]
    def databasesetter(self):
        count =0

        
        
        selector=self.connection.execute("SELECT SAVENAME,LEVEL, LIVES, DATESAVE, SCORE from PACMANGAMES")
        for row in selector:
            count += 1
        if count<3:
            self.connection.execute("INSERT OR IGNORE INTO PACMANGAMES(SAVENAME,LEVEL,LIVES,DATESAVE,SCORE)\
                                        VALUES(?,?,?,?,?)",(self.name,self.level,self.lives,self.date,self.score));
            self.connection.commit()
        else:
            print("no no")
        
        
        selector2=self.connection.execute("SELECT SAVENAME,LEVEL, LIVES, DATESAVE, SCORE from PACMANGAMES")
        new=selector2.fetchall()
        # for row in selector2:
        #     print("Save name=",row[1])
            # print("Level=",row[1])
            # print("Lives=",row[2])
            # print("Date of save=",row[3])
            # print("Score=",row[4])
            # print(Database.limit)
        print("\n")
        self.connection.close()
