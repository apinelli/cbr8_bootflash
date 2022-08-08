----------------------------------------------------------------------------
This script will generate a report with bootflash occupation on CBR8s
----------------------------------------------------------------------------

1) Go to your home directory:
$ cd ~

2) Clone the repository:
$ git clone https://github.com/apinelli/cbr8_bootflash.git

3) Add hostnames or ip addresses to the inventory_cisco file

4) Now run the playbook:
$ ansible-playbook -i inventory_cisco gather_hw_cisco5_hw.yaml -u ww -k

where "ww" is the user name (for all CBR8s)
It will prompt you for the SSH password (for all CBR8s)

5) Check if the files have been written under bootflash/HW

6) Run the following to get the report:
$ python3 cbr8_parser10.py

7) Check if the report has been created under REPORTS/
