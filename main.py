import os
from rich.console import Console


con = Console()
DEBUG = False
def_config_file_name = "/home/neuro/dev/def_config/.config"
def_config_output_file = "/home/neuro/dev/def_config/enabled_in_config"
new_config_file_name = "/home/neuro/dev/new_config/.config"

def file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


def remove_file(filename: str):
    try:
        os.remove(filename)
    except FileNotFoundError:
        con.print("File Not Found:", filename)


def clear_from_commented(in_file: str, out_file: str):
    with open(in_file) as f:
        content = f.readlines()
    with open(out_file, "a") as o:
        for item in content:
            if item[0] != "#":
                o.writelines(item)
                if DEBUG:
                    con.print(item)


def main():
    def_cfg_list = file_to_list(def_config_file_name)
    new_cfg_list = file_to_list(new_config_file_name)
    s = set(def_cfg_list)
    tmp = [x for x in new_cfg_list if x not in s]
    for i in tmp:
        if i[0] != "#":
            con.print(i)

# differencer
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
