import pandas as pd

titanic = pd.read_csv('data/titanic.csv')

# =============================================================================
# Creating a column with null age filled with the mean of ages
#
# mediaAge = int(titanic["Age"].mean())
# 
# titanic["AgeFillNaMean"] = titanic["Age"].fillna(mediaAge)
# print(titanic["AgeFillNaMean"].head(10))
# =============================================================================

# =============================================================================
# # Grouping mean of ages for people by sex with GROUP BY
#
# peopleBySex = titanic.groupby("Sex")["Age"].mean()
# print(peopleBySex.head())
# =============================================================================

# =============================================================================
# personByCabin = titanic.groupby("Cabin")["PassengerId"].count()
# print(personByCabin.head())
# =============================================================================

averageMan = round(titanic.Age[titanic["Sex"] == "male"].mean())
averageWoman = round(titanic.Age[titanic["Sex"] == "female"].mean())


def fillAge(line):
    age = line["Age"]
    sex = line["Sex"]
    
    if pd.isnull(age):
        if sex == "male":
            return averageMan
        elif sex == "female":
            return averageWoman
    else:
        return age
titanic["AgeRange"] = titanic.apply(fillAge, axis=1)