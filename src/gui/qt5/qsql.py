from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication
app = QApplication([])

db = QSqlDatabase("QPSQL")
print("Available drivers", db.drivers())

if not db.open():
    print("Unable to connect.")
    print('Last error', db.lastError().text())
else:
    print("Connection to the database successful")