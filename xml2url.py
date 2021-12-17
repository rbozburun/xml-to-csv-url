#!/usr/bin/env python3

import argparse
import xml.etree.ElementTree as ET
import sys

def main():
    parser = argparse.ArgumentParser(description="NMAP XML PARSER TO CREATE URLS")
    parser.add_argument('-f','--xml_file', help="Nmap XML output.")
    parser.add_argument('-o','--output', help="If you want to create an output, give the CSV filename.")
    parser.add_argument('-n', '--no_headers', action='store_true', help='This flag removes the header from the CSV output File')
    parser.add_argument('-pI', '--print_ip', action='store_true', help='Print URLS with IP addresses.')
    parser.add_argument('-pH', '--print_hostname', action='store_true', help='Print URLS with hostnames.')
    args = parser.parse_args()
    xml_file = args.xml_file
    output = args.output
    no_headers = args.no_headers

    #urls[0] => IP
    #urls[1] => Hostname
    urls = createCSV(xml_file,output,no_headers)

    if args.print_ip == True:
        printURLS(urls[0])

    if args.print_hostname == True:
        printURLS(urls[1])
    
def printURLS(urls):
    for i in urls:
        print(i)


def isHTTP(port):
    http_ports = [80, 81, 82, 443,  554,  591, 4791, 5554,  5060,  5800, 5900, 6638,  8008,  8080, 8081, 8181, 8090, 8443, 8554]
    return port in http_ports


def createCSV(xml_file,output,no_headers):
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()

        except ET.ParseError as e:
            print ("Parse error({0}): {1}".format(e.errno, e.strerror))
            sys.exit(2)

        except IOError as e:
            print ("IO error({0}): {1}".format(e.errno, e.strerror))
            sys.exit(2)

        except:
            print ("Unexpected error:", sys.exc_info()[0])
            sys.exit(2)

        outputF = open(output,'w+')
        if (no_headers != True):
            out = "ip,hostname,portnum,protocol,service,osver\n"
            
            outputF.write (out)

        ip_urls = []
        hostname_urls = []
        
        for host in root.findall('host'):
            ip = host.find('address').get('addr')
            isUp = host.find('status').get('state')
            hostname = ""
            if isUp is not "down":
                if host.find('hostnames') is not None:
                    if host.find('hostnames').find('hostname') is not None:
                        hostnames = host.find('hostnames').findall("hostname")
                        for temp_hostname in hostnames:
                            if temp_hostname.get("type") == "user":
                                hostname = temp_hostname.get("name")
                        
                    for child in host:
                        for children in child.findall('.//'):
                            osver = str(children.text)
                
                for port in host.find('ports').findall('port'):
                    protocol = port.get('protocol')
                    if protocol is None:
                        protocol = ""
                    portnum = port.get('portid')
                    if portnum is None:
                        portnum = ""
                    else:
                        p_portnum = int(portnum)
                        if isHTTP(p_portnum):
                            if p_portnum == 443 or p_portnum == 8443: 
                                url = "https://{0}:{1}".format(ip, p_portnum)
                                ip_urls.append(url)

                                if hostname != "":
                                    url = "https://{0}:{1}".format(hostname, p_portnum)
                                    hostname_urls.append(url)

                            else:
                                url = "http://{0}:{1}".format(ip, p_portnum)
                                ip_urls.append(url)

                                if hostname != "":
                                    url = "http://{0}:{1}".format(hostname, p_portnum)
                                    hostname_urls.append(url)

                                

                    service = ""
                    if port.find('service') is not None:
                        if port.find('service').get('name') is not None:
                            service = port.find('service').get('name')
            
                    out = ip + ',' + hostname + ','  + portnum + ','+  protocol + ',' +service + ',' + osver + '\n'
                    outputF.write(out)

        outputF.close()

        return [ip_urls, hostname_urls]


if __name__ == "__main__":
    main()

