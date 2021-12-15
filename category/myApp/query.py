from django.db import connection


def studentIndex():
    try:
        # cursor = connection.cursor()
        # 
        cursor = connection.cursor()
        sqlQuery = "Select * from students;"
        cursor.execute(sqlQuery)
        row = cursor.fetchall()

        connection.commit()
        connection.close()

    except Exception as e:
        return tuple('','','','')
    return row

def quertType1():
    sqlQuery = """Select country, avg(score)
                From students
                group by country"""

def quertType2():
    sqlQuery = """Select country, avg(score)
                From students
                group by country"""

def quertType3():
    sqlQuery = """
        Select pro.name, stu.name
        From (
            select name, country, max(score)
            from students
            group by country
        ) as stu join
        (
            select name, country, max(age)
            from professors
            group by country
        ) as pro on stu.country = pro.country
    """