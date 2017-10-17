from get_ecg import Ecg
from glob import glob

data = Ecg(csv_file=None, update_time=5,
           brady_threshold=60, tachy_threshold=100, mins=2)

if __name__ == "__main__":
    # Importing csv data
    # Create the list of file
    list_of_files = glob.glob('test_data/*.csv')
    for file_name in list_of_files:
        FI = open(file_name, 'r')
        output_name = file_name[:-4]
        data = Ecg(csv_file=None, update_time=5,
                   brady_threshold=60, tachy_threshold=100, mins=2)
