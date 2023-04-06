import sqlite3 as sl

con = sl.connect('clinic.db')


# with con:
#     con.execute("""
#         CREATE TABLE IF NOT EXISTS Finish_services (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             client INT,
#             service INT,
#             name_doctor INT,
#             time_start DATETIME,
#             time_end DATETIME
#         );
#     """)

# with con:
#     con.execute("""
#         CREATE TABLE IF NOT EXISTS Clients (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             sore_name TEXT,
#             birthday DATE,
#             tel INT,
#             json_file TEXT,
#             UNIQUE(tel)
#         );
#     """)


# with con:
#     con.execute("""
#         CREATE TABLE IF NOT EXISTS Services (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             service TEXT,
#             price INT,
#             time_duration TEXT,
#             post INT
#         );
#     """)
#

# with con:
#     con.execute("""
#         CREATE TABLE IF NOT EXISTS FIO (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             first_name TEXT,
#             second_name TEXT,
#             sure_name TEXT,
#             birthday INTEGER,
#             tel TEXT,
#             post INT,
#             UNIQUE(tel)
#         );
#     """)
# with con:
#     con.execute("""
#         CREATE TABLE IF NOT EXISTS Staff (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             post TEXT,
#             cash INT,
#             office INT
#         );
#     """)