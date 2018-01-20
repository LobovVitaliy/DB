from django.db import connection


def get_data(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def fetchall(func):
    def wrapper(*args):
        c = connection.cursor()
        query = func(*args)
        c.execute(query)
        data = get_data(c)
        c.close()
        return data
    return wrapper


def get_id(func):
    def wrapper(*args):
        c = connection.cursor()
        query = func(*args)
        c.execute(query)
        id = c.lastrowid
        c.close()
        return id
    return wrapper


def execute(func):
    def wrapper(*args):
        c = connection.cursor()
        query = func(*args)
        c.execute(query)
        c.close()
    return wrapper


def executemany(func):
    def wrapper(*args):
        c = connection.cursor()
        query, dict_list = func(*args)
        c.executemany(query, dict_list)
        c.close()
    return wrapper


@fetchall
def all(table):
    return 'SELECT * FROM %s' % table


@fetchall
def get(table, id):
    return 'SELECT * FROM %s WHERE id=%s' % (table, id)


def get_query_join_flights():
    return """
        SELECT
            flight.id,
            a1.id as id_from,
            a1.name as `from`,
            a2.id as id_to,
            a2.name as `to`,
            plane.id as plane,
            date,
            status
        FROM flight
            JOIN airport as a1 ON id_from_airport = a1.id
            JOIN airport as a2 ON id_to_airport = a2.id
            JOIN plane ON id_plane = plane.id
    """


@fetchall
def get_join_flights():
    return get_query_join_flights()


@fetchall
def fulltext(phrase, excluded):
    match = """
        (
            MATCH (a1.name) AGAINST ('"%s"' IN BOOLEAN MODE)
            OR
            MATCH (a2.name) AGAINST ('"%s"' IN BOOLEAN MODE)
        )
    """ % (phrase, phrase)

    not_match = """
        (
            NOT MATCH (a1.name) AGAINST ('+%s' IN BOOLEAN MODE)
            AND
            NOT MATCH (a2.name) AGAINST ('+%s' IN BOOLEAN MODE)
        )
    """ % (excluded, excluded)

    where = 'WHERE '

    if phrase and excluded:
        where += '%s AND %s' % (match, not_match)
    elif phrase:
        where += match
    elif excluded:
        where += not_match
    else:
        where = ''

    return '%s %s' % (get_query_join_flights(), where)


@fetchall
def do(query):
    return query


@get_id
def create(table, dict):
    columns = ', '.join(dict.keys())
    values = ', '.join(dict.values())
    return 'INSERT INTO %s (%s) VALUES (%s)' % (table, columns, values)


@executemany
def create_list(table, dict_list):
    keys = dict_list[0].keys()
    columns = ', '.join(keys)
    values = ', '.join(('%%(%s)s' % k) for k in keys)
    query = 'INSERT INTO %s (%s) VALUES (%s)' % (table, columns, values)
    return query, dict_list


@execute
def update(table, id, dict):
    columns = ', '.join(('%s=%s' % (k, v)) for k, v in dict.items())
    return 'UPDATE %s SET %s WHERE id=%s' % (table, columns, id)


@execute
def delete(table, id):
    return 'DELETE FROM %s WHERE id=%s' % (table, id)


@execute
def truncate(table):
    return 'TRUNCATE TABLE %s' % table
