from django.db import connection

class Query:
    cursor = connection.cursor()

    @staticmethod
    def studentIndex():
        try:
            cursor = Query.cursor
            sqlQuery = "Select * from students;"
            result = cursor.execute(sqlQuery)
            row = cursor.fetchall()

            connection.commit()

        except Exception as e:
            return tuple('','','','')
        return row

    @staticmethod
    def quertType1():
        try:
            cursor = Query.cursor
            sqlQuery = """
                Select country, avg(score)
                From students
                group by country;"""
            cursor.execute(sqlQuery)
            row = cursor.fetchall()
            connection.commit()

        except Exception as e:
            return tuple('','','','')
        return row
        
    @staticmethod
    def quertType2():
        # 미완성
        try:
            cursor = Query.cursor
            sqlQuery = """
                Select country, avg(score)
                From students
                group by country"""
            cursor.execute(sqlQuery)
            row = cursor.fetchall()
            connection.commit()

        except Exception as e:
            return tuple('','','','')
        return row
        
    @staticmethod
    def quertType3():
        try:
            cursor = Query.cursor
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
                ) as pro on stu.country = pro.country;"""
            cursor.execute(sqlQuery)
            row = cursor.fetchall()
            connection.commit()

        except Exception as e:
            return tuple('','','','')
        return row
