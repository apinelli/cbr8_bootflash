----------------------------------------------------------------------------
This script will generate a report with bootflash occupation on CBR8s
----------------------------------------------------------------------------

1) Go to your home directory:
$ cd ~

2) Clone the repository:
$ git clone https://github.com/apinelli/cbr8_bootflash.git

3) Create a couple of directories:
$ cd cbr8_bootflash
$ mkdir bootflash/HW
$ mkdir REPORTS

4) Add hostnames or ip addresses to the inventory_cisco file

5) Now run the playbook:
$ ansible-playbook -i inventory_cisco gather_hw_cisco5_hw.yaml -u ww -k

where "ww" is the user name (for all CBR8s)
It will prompt you for the SSH password (for all CBR8s)

6) Check if the files have been written under bootflash/HW

7) Run the following to get the report:
$ python3 cbr8_parser10.py

8) Check if the report has been created under REPORTS/
