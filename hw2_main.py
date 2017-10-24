from get_ecg import Ecg
import glob


if __name__ == "__main__":
    """
    
    Main script that calls all methods of Ecg in order to 
    process data contained in an input csv file and output a .txt file
    containing all estimated heart rate parameters 
    
    """
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
