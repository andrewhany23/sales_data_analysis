import pandas as pd

all_data = pd.read_csv("./main/all_data.csv")

def generate_split_data (type):
    series = all_data[type]
    lst = list ()
    for element in series:
        if element not in lst:
            lst.append (element)
            data = all_data[all_data[type] == element]
            data.to_csv (f"./split data/{type}/{element}_data.csv")

def generate_collective_date (type):
    series = all_data[type]
    lst = list ()
    dct = {f"{type}": [], "counts": [], "average_sales": [], "total_sales": []}
    for element in series:
        if element not in lst:
            lst.append (element)
            data = all_data[all_data[type] == element]
            counts = len(data)
            average_sales = int (data.sales.mean ())
            total_sales = data.sales.sum ()

            dct [f"{type}"].append(element)
            dct ["counts"].append (counts)
            dct ["average_sales"].append(average_sales)
            dct ["total_sales"].append(total_sales)

    data_frame = pd.DataFrame(dct)
    data_frame.to_csv (f"./collective data/{type}/{type}_data.csv")

generate_split_data ("date")
generate_split_data ("location")
generate_split_data ("payment_method")

generate_collective_date ("location")
generate_collective_date ("date")
generate_collective_date ("payment_method")
