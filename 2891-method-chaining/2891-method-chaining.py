import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals = animals[animals['weight'] > 100].sort_values('weight', ascending=False)
    animals.drop(columns= ['weight','age','species'],inplace=True)
    return animals