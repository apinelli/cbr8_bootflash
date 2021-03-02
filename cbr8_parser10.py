import os
import json

homepath = os.getcwd()
reportpath = os.path.join(homepath, 'REPORTS')

def Sort_Tuple(tup):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    return(sorted(tup, reverse=True, key = lambda x: x[1]))

def gen_bootvar_report():  # Defines the function to generate a report for bootvar
    folderpath = os.path.join(homepath, 'bootvar', 'HW')
    filepaths = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
    bootvar_list = []
    with open(path, 'r') as f:
        destino_dict = json.load(f)
        bootvar = destino_dict['stdout']
        bootvar_list.append(bootvar)
    report_path_name = os.path.join(reportpath, 'report_bootvar.txt')
    with open(report_path_name, 'a') as ver:
        print('=====================================================', file=ver)
        print('CBR8 Boot variable report', file=ver)
        print('=====================================================', file=ver)
        for sub_list in bootvar_list:
            print('{0:40}  {1}'.format(sub_list[0], sub_list[1]), file=ver)

def gen_logging_report():  # Defines the function to generate a report for logging buffered
    folderpath = os.path.join(homepath, 'logging', 'HW')
    filepaths = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
    logging_list = []
    for path in filepaths:
        with open(path, 'r') as f:
            destino_dict = json.load(f)
            logging = destino_dict['stdout']
            logging_list.append(logging)
    report_path_name = os.path.join(reportpath, 'report_logging.txt')
    with open(report_path_name, 'a') as ver:
        print('=====================================================', file=ver)
        print('CBR8 logging report', file=ver)
        print('=====================================================', file=ver)
        for sub_list in logging_list:
            print('{0:40}  {1}'.format(sub_list[0], sub_list[1]), file=ver)
            print(sub_list[2], file=ver)
            print("------------------------------------------------------", file=ver)

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
            spacefree = destino_dict['ansible_facts']['ansible_net_filesystems_info']['bootflash:']['spacefree_kb']
            spacetotal = destino_dict['ansible_facts']['ansible_net_filesystems_info']['bootflash:']['spacetotal_kb']
            hostname = destino_dict['ansible_facts']['ansible_net_hostname']
            version = destino_dict['ansible_facts']['ansible_net_version']
            version_list.append(version)
            occup = round((spacefree / spacetotal) * 100)
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

def gen_uptime_report():  # Defines the function to generate a report for uptime
    folderpath = os.path.join(homepath, 'uptime', 'HW')
    filepaths = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
    uptime_list = []
    for path in filepaths:
        with open(path, 'r') as f:
            destino_dict = json.load(f)
            uptime = destino_dict['stdout']
            uptime_list.append(uptime)
    report_path_name = os.path.join(reportpath, 'report_uptime.txt')
    with open(report_path_name, 'a') as ver:
        print('=====================================================', file=ver)
        print('CBR8 Uptime report', file=ver)
        print('=====================================================', file=ver)
        for sub_list in uptime_list:
            print('{0:40}  {1}'.format(sub_list[0], sub_list[1]), file=ver)

def gen_oid_report():  # Defines the function to generate a report for oid
    folderpath = os.path.join(homepath, 'oid', 'HW')
    filepaths = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
    oid_list = []
    for path in filepaths:
        with open(path, 'r') as f:
            destino_dict = json.load(f)
            oid = destino_dict['stdout']
            oid_list.append(oid)
    report_path_name = os.path.join(reportpath, 'report_oid.txt')
    with open(report_path_name, 'a') as ver:
        print('=====================================================', file=ver)
        print('CBR8 OID report', file=ver)
        print('=====================================================', file=ver)
        for sub_list in oid_list:
            print('{0:40}  {1}'.format(sub_list[0], sub_list[1]), file=ver)
            for i in range(2,len(sub_list)):
                print(sub_list[i], file=ver)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++', file=ver)

def gen_aaa_report():
    folderpath = os.path.join(homepath, 'aaa', 'HW')
    filepaths = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
    aaa_list = []
    for path in filepaths:
        with open(path, 'r') as f:
            destino_dict = json.load(f)
            aaa = destino_dict['stdout']
            aaa_list.append(aaa)
    report_path_name = os.path.join(reportpath, 'report_aaa.txt')
    with open(report_path_name, 'a') as ver:
        print('=====================================================', file=ver)
        print('CBR8 AAA report', file=ver)
        print('=====================================================', file=ver)
        for sub_list in aaa_list:
            for i in sub_list:
                if i == "% Authorization failed.":
                    print('{0:40}  {1}'.format(sub_list[0], i), file=ver)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++', file=ver)

# Call functions to generate report:
#gen_bootvar_report()
gen_bootflash_report()
#gen_logging_report()
#gen_uptime_report()
#gen_oid_report()
#gen_aaa_report()
