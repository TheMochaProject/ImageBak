# config.py by Ramesh Balaji
# Part of ImageBak, Image Backup System for all Operating Systems, controlled in software, not by preboot
#
#
def initial_procedure():
    with open("config.cfg") as configfile:
        configuration_array = configfile.readlines()


with open("config.cfg") as configfile:
    configuration_array = configfile.readlines()


def get_value(key):
    for configline in configuration_array:
        config_keyval = configline.split(" ")
        if config_keyval[0] == key:
            return config_keyval[1]



def set_value(key, val):
    line = 0
    for configline in configuration_array:
        config_keyval = configline.split(" ")
        if config_keyval[0] == key:
            config_str = key + " " + val + "\n"
            configuration_array[line] = config_str
        line += 1
    with open('config.cfg', 'w') as config:
        config.writelines(configuration_array)

print(get_value("mounted_backuploc"))