import os
import json

homepath = os.getcwd()
reportpath = os.path.join(homepath, 'REPORTS')

def Sort_Tuple(tup):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    return(sorted(tup, reverse=True, key = lambda x: x[1]))

def gen_bootflash_report(): # Defines a function to create a report on bootflash
    folderpath = os.path.join(homepath, 'bootflash', 'HW')
    filepaths = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
    all_files = []
    version_list = []
    all_list = []
    all_list_sorted = []
    for path in filepaths:
        with open(path, 'r') as f:
            destino_dict = json.load(f)
            spacefree = destino_dict["ansible_facts"]["ansible_net_filesystems_info"]["bootflash:"]["spacefree_kb"]
            spacetotal = destino_dict["ansible_facts"]["ansible_net_filesystems_info"]["bootflash:"]["spacetotal_kb"]
            hostname = destino_dict["ansible_facts"]["ansible_net_hostname"]
            version = destino_dict["ansible_facts"]["ansible_net_version"]
            version_list.append(version)
            occup = round(((1 - spacefree/spacetotal)*100), 0)
            host_version_occup_tuple = (hostname, occup, version)
            all_list.append(host_version_occup_tuple)
            all_list_sorted = Sort_Tuple(all_list)
    report_path_name = os.path.join(reportpath, 'report_bootflash.txt')
    with open(report_path_name, 'a') as ver:
        print('=====================================================', file=ver)
        print('CBR8 Bootflash Occupation report', file=ver)
        print('=====================================================', file=ver)
        version_unique = list(set(version_list))
        print('-' * 70, file=ver)
        for i in version_unique:
            print('Number of chassis with version', i, ': ', version_list.count(i), file=ver)
        print('-' * 70, file=ver)
        print(' ' * 70, file=ver)
        print('{0:30} {1:30} {2}'.format('Hostname', 'Bootflash Occup %', 'Version'), file=ver)
        for tuplas in all_list_sorted:
            print('{0:30} {1:10} {2:^45}'.format(tuplas[0], tuplas[1], tuplas[2]), file=ver)

# Call functions to generate report:
gen_bootflash_report()

