from PyQt5.QtSql import QSqlQueryModel, QSqlDatabase

conn = QSqlDatabase.addDatabase("QPSQL")
conn.setDatabaseName("edf-re-uk")
conn.setHostName("defslp-pgs01")
conn.setUserName(r"EU\jcampbell")
conn.setPassword("IrvineWelsh2")
conn.setPort(5432)


def my_model() -> None:
    model = QSqlQueryModel()
    model.setQuery("SELECT id, name FROM constraint_layers")

    for i in range(model.rowCount()):
        _id = model.record(i).value("id")
        name = model.record(i).value("name")
        print(_id, name)


if __name__ == "__main__":
    print(conn.open())
    print(conn.lastError().driverText())
    print(conn.lastError().databaseText())
    print(conn.isValid())
