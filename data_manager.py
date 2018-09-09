import database_common


@database_common.connection_handler
def get_full_name(cursor):
    cursor.execute("""
                    SELECT first_name, last_name FROM names;
                   """)
    names = cursor.fetchall()
    return names

@database_common.connection_handler
def add_new_personal(cursor, first_name, last_name):
    print(first_name)
    print(last_name)
    cursor.execute("""
                    INSERT INTO names (first_name, last_name)
                    VALUES (%(first_name)s, %(last_name)s);
                   """,
                    {'first_name': first_name, 'last_name': last_name})
