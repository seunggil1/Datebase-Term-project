from django.db import connection

class Query:
    cursor = connection.cursor()

    @staticmethod
    def queryType1():
        try:
            cursor = Query.cursor
            sqlQuery = """
                Select country, avg(score)
                From students
                group by country
                order by country;"""
            cursor.execute(sqlQuery)
            row = cursor.fetchall()
            connection.commit()

        except Exception as e:
            return tuple('','','','')
        return row
        
    @staticmethod
    def queryType2():
        try:
            cursor = Query.cursor
            sqlQuery = """
                Select Countries.city, avg(Students.score)
                from Students join Countries 
                on Students.country = Countries.countryName
                group by city
                order by Countries.city;"""
            cursor.execute(sqlQuery)
            row = cursor.fetchall()
            connection.commit()

        except Exception as e:
            return tuple('','','','')
        return row
        
    @staticmethod
    def queryType3():
        try:
            cursor = Query.cursor
            sqlQuery = """
                Select Professors.name, Students.name
                From Students, Professors,(
                        Select stu.country, maxScore, maxAge
                        From (
                            select country, max(score) as maxScore
                            from students
                            group by country
                        ) as stu join
                        (
                            select country, max(age) as maxAge
                            from professors
                            group by country
                        ) as pro on stu.country = pro.country
                    ) as maxInfo
                Where Students.country = Professors.country
                    and Students.country = maxInfo.country
                    and Students.score = maxInfo.maxScore
                    and Professors.age = maxInfo.maxAge;"""
            cursor.execute(sqlQuery)
            row = cursor.fetchall()
            connection.commit()

        except Exception as e:
            return tuple('','','','')
        return row


    @staticmethod
    def queryType4():
        try:
            cursor = Query.cursor
            sqlQuery = """
                Select Pro.name, Stu.name
                FROM (
                        Select facultyID, name, age, ProfessorsWithCity.city
                        From (Select *
                                From Professors join Countries
                                on Professors.country = Countries.countryName
                            ) as ProfessorsWithCity,
                            (
                                Select max(age) as maxAge, city
                                From Professors join Countries
                                on Professors.country = Countries.countryName
                                group by city
                            ) as cityMaxAge
                        Where ProfessorsWithCity.age = cityMaxAge.maxAge
                            and ProfessorsWithCity.city = cityMaxAge.city
                    ) as Pro 
                    join
                    (
                        Select studentID, name, score, studentsWithCity.city
                        From (Select *
                                From Students join Countries
                                on Students.country = Countries.countryName
                            ) as studentsWithCity,
                            (
                                Select max(score) as maxScore, city
                                From Students join Countries
                                on Students.country = Countries.countryName
                                group by city
                            ) as cityMaxScore
                        Where studentsWithCity.score = cityMaxScore.maxScore
                            and studentsWithCity.city = cityMaxScore.city
                    ) as Stu
                    on Pro.city = Stu.city;"""
            cursor.execute(sqlQuery)
            row = cursor.fetchall()
            connection.commit()

        except Exception as e:
            return tuple('','','','')
        return row

    @staticmethod
    def queryType5():
        try:
            cursor = Query.cursor
            sqlQuery = """
                Select name, city
                From Students join Countries
                on Students.country = Countries.countryName
                WHERE city in (
                    Select *
                    From(
                        Select ci.city
                        From (
                            Select city, sum(population) as cityPopulation
                            FROM Countries
                            Group by city) as ci
                        join (
                            select city, count(patientID) as cityPatient
                            from covid
                            group by city
                            ) as co
                            on ci.city = co.city
                        order by (cityPatient / cityPopulation) desc
                        LIMIT 3
                    ) as tmp
                )
                order by city;"""
            cursor.execute(sqlQuery)
            row = cursor.fetchall()
            connection.commit()

        except Exception as e:
            return tuple('','','','')
        return row
