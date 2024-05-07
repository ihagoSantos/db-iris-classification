from visualization import Visualization
from dataset import Dataset

def main():
    dataset = Dataset()
    df = dataset.load_from_url()
    visualization = Visualization(df)

    visualization.sumary()


main()