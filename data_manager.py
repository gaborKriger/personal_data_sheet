import database_common


@database_common.connection_handler
def get_full_name(cursor):
    cursor.execute("""
                    SELECT first_name, last_name FROM names;
                   """)
    names = cursor.fetchall()
    return names