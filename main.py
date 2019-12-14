import csv
import sys
import glob


def write_csv(data):
    fieldnames = ["ID", "Happy", "Fear"]
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)

    writer.writeheader()
    for key, value in data.items():
        writer.writerow(
            {
                "ID": key,
                "Happy": value.get("happy", "N/A"),
                "Fear": value.get("fear", "N/A"),
            }
        )


def find_files():
    all_files = glob.glob("SB*")
    data = {all_file: {} for all_file in sorted(all_files)}

    fears = glob.glob("SB*/T4/model/tgng/fear_lev1_mod1.feat")
    happys = glob.glob("SB*/T4/model/tgng/happy_lev1_mod1.feat")

    for fear in fears:
        key = fear.split("/")[0]
        with open(fear) as f:
            fear_value = f.read()
        data[key]["fear"] = float(fear_value)

    for happy in happys:
        key = happy.split("/")[0]
        with open(happy) as f:
            happy_value = f.read()
        data[key]["happy"] = float(happy_value)

    return data


data = find_files()
write_csv(data)
