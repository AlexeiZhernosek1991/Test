import sqlite3 as sl

con = sl.connect('clinic.db')


# sql_insert = "INSERT OR IGNORE INTO SMTH (name, age, information, tel) values(?, ?, ?, ?)"
# # INSERT OR IGNORE - модификатор для уникальных значений
# with con:
#     con.execute(sql_insert, ["человек", 20, "qweewq", "+7123321123321"])
#     # executemany - для двумерного
#     con.execute(sql_insert, ["человек2", 24, "qweewq", "+7123321123322"])


# with con:
#     data = con.execute("SELECT * FROM SMTH WHERE age <= 20")
#     print(data)
#     print(data.fetchall())
#     # fetchone

def Select_tabl(tabl):
    with con:
        data = con.execute(f"SELECT * FROM {tabl}")
        data = data.fetchall()
        print(data)
        return data


def name_colum_tabl(tabl):
    with con:
        name_colum = con.execute(f"PRAGMA table_info ({tabl})")
        name_colum = name_colum.fetchall()
        name_colum_list = []
        for colum in name_colum:
            name_colum_list.append(colum[1])
        print(name_colum_list)
        return name_colum_list


def Add_doctor(doc_info: list):
    try:
        sql_insert = f"INSERT OR IGNORE INTO FIO (first_name, second_name, sure_name, birthday, tel, post) values(?, ?, ?, ?, ?, ?)"
        with con:
            con.execute(sql_insert, doc_info)
        return True
    except:
        return False


def update_new(tabl, info_new: dict):
    try:
        sqlite_update_query = f"Update {tabl} set"
        columnValues = tuple(info_new.values())[1:]
        for d in info_new:
            sqlite_update_query = f'{sqlite_update_query} {d}=?,'
        sqlite_update_query = sqlite_update_query[:-1]
        sqlite_update_query = f'{sqlite_update_query} WHERE id =?'
        con.execute(sqlite_update_query, columnValues)
        return True
    except:
        return False


def info_dict():
    fio = Select_tabl('FIO')
    clients = Select_tabl('Clients')
    services = Select_tabl('Services')
    fio_dict = {}
    clients_dict = {}
    services_dict = {}
    for f in fio:
        fio_dict.setdefault(f[0], f'{str(f[1])} {f[2]} {f[3]}')
    print(fio_dict)
    for c in clients:
        clients_dict.setdefault(str(c[0]), f'{c[1]} {c[2]}')
    print(clients_dict)
    for fi in services:
        services_dict.setdefault(str(fi[0]), f'{fi[1]}')
    print(services_dict)
    return fio_dict, clients_dict, services_dict


def entry_service(id_tuple):
    try:
        sql_insert = f"INSERT INTO Finish_services (name_doctor, service, client) values(?, ?, ?)"
        with con:
            con.execute(sql_insert, id_tuple)
        return True
    except:
        return False


def all_service_doctor(doctor_id):
    with con:
        data = con.execute(
            f"SELECT service FROM Services JOIN Staff ON Services.post = Staff.id JOIN FIO ON Staff.id = FIO.post Where FIO.id = {doctor_id}")
        a = data.fetchall()
        print(a)
        return a


def delete_row_table(tabl, id_list):
    if len(id_list) < 2:
        id_list.append(id_list[0])
    with con:
        a = f'DELETE FROM {tabl} WHERE id IN {tuple(id_list)}'
        con.execute(a)



