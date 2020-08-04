import global_logic_flags
def extract_attributes_from_timestamp(input_timestamp):
    """
    This function returns two values. The input to the function is timestamp
    :return:
    value 1 = hour
    value 2 = min
    """
    output_hour = input_timestamp.hour
    output_min = input_timestamp.min
    return output_hour,output_min

def extract_attributes_from_timedelta(input_seconds):
    """
    This function returns two values. The input tot he function is the seconds attribute of timedelta object
    :return:
    value 1 = hour
    value 2 = min
    """
    output_hour = input_seconds // 3600
    output_min = input_seconds // 60 - (output_hour * 60)
    return output_hour,output_min

def extract_time_attributes(extraction_method,input_value):
    """

    :param extraction_method:   1 for extraction from timestamp
                                2 for extraction from timedelta
    :param input_value:         timestamp for method 1
                                seconds for timedelta
    :return:
    value 1 = hour
    value 2 = min
    """
    try:
        if extraction_method == 1:
            if global_logic_flags.system_debug == 1:
                print("Extracting time attributes using timestamp method")
            extract_attributes_from_timestamp(input_value)
        elif extraction_method == 2:
            if global_logic_flags.system_debug == 1:
                print("Extracting time attributes using timedelta method")
            extract_attributes_from_timedelta(input_value)
        else:
            print(f"wrong method selected ==> {extraction_method}")
    except:
        print("Something went wrong with the extraction process.")

