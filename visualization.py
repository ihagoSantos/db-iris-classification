import pandas as pd
class Visualization:
    """
    Class for data visualization
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def get_separator(self, title = None) -> str:
        """
        Return separator
        """
        separator = "="*50
        if title:
            return f"\n{separator} {title} {separator}\n"
        
        return separator * 2

    def sumary(self) -> None:
        """
        Show sumary of dataframe
        """
        sumary_functions = {
            "DATA": self.dataframe.head,
            "SHAPE": (lambda : self.dataframe.shape),
            "DESCRIBE": self.dataframe.describe,
            "CLASS DISTRIBUTION": self.dataframe.groupby('class').size
        }

        for key, fn in sumary_functions.items():
            print(self.get_separator(key))
            print(fn())
