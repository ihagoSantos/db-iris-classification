import pandas as pd
from utils import constants as consts

class Dataset:
    """
    Manipulate Iris Data
    """
    def __init__(self):
        self.url = consts.IRIS_DATA_URL
        self.attrs = ["sepal_length","sepal_width", "petal_length", "petal_width", "class"]

    def load_from_url(self) -> pd.DataFrame:
        """
        Import data from iris.data and return a pandas dataframe.
        """
        df = pd.read_csv(self.url, names = self.attrs)
        df.columns = self.attrs
        return df