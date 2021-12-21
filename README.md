
# xml-to-csv-url

Convert NMAP's XML output to CSV file and print URL addresses for HTTP/HTTPS ports.

NOTE:
OS Version Parsing is not working properly yet.


## Features

- Create only CSV file.
- Print URLs with hostnames.
- Print URLs with IP addresses.
- Remove CSV headers from the output file.


## Usage
First make the script executable.
```bash
  chmod 755 xml2url.py
```

Then, run.

```plaintext
.\xml2url.py -h
usage: xml2url.py [-h] [-f XML_FILE] [-o OUTPUT] [-n] [-pI] [-pH]

NMAP XML PARSER TO CREATE URLS

optional arguments:
  -h, --help            show this help message and exit
  -f XML_FILE, --xml_file XML_FILE
                        Nmap XML output.
  -o OUTPUT, --output OUTPUT
                        If you want to create an output, give the CSV
                        filename.
  -n, --no_headers      This flag removes the header from the CSV output File
  -pI, --print_ip       Print URLS with IP addresses.
  -pH, --print_hostname
                        Print URLS with hostnames.
```

```plaintext
.\xml2url.py -f nmap.xml -o nmap_csv_output.csv
```

```plaintext
.\xml2url.py -f nmap.xml -o nmap_csv_output.csv -pI
```

```plaintext
.\xml2url.py -f nmap.xml -o nmap_csv_output.csv -pI -pH
```

## Related

Here are some related projects

- [NMAP-XML-Parse](https://github.com/Cyb3r4rch3r/NMAP-XML-Parse)

- [Nmap-XML-to-CSV](https://github.com/NetsecExplained/Nmap-XML-to-CSV)





