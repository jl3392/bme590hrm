from get_ecg import Ecg
import glob

data = Ecg(csv_file=None, update_time=5,
           brady_threshold=60, tachy_threshold=100, mins=2)

if __name__ == "__main__":
    # Importing csv data
    # Create the list of file
    list_of_files = glob.glob('test_data/*.csv')
    for file_name in list_of_files:
        FI = open(file_name, 'r')
        data = Ecg(csv_file=file_name, update_time=5,
                   brady_threshold=60, tachy_threshold=100, mins=2)
        data.prep_data()
        data.get_max_peak()
        data.get_inst_hr()
        data.get_avghr()
        data.get_output()
