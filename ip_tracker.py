

from bs4 import BeautifulSoup
import argparse
import urllib

def show_result(infos):
    show_info = (
                "IP {0}\n".format(infos["IP Address"]) +
                "Longitude {0}\n".format(infos["Longitude"]) +
                "Latitude {0}\n".format(infos["Latitude"]) +
                "Estado {0}\n".format(infos["Region"]) +
                "Horario Local {0}\n".format(infos["Local time"]) +
                "Pais {0}".format(infos["Country Code"])
    )
    print (show_info)

def command_line():
    parse = argparse.ArgumentParser(
        description = "Get information of IP address")
    parse.add.argument("-i","--ip",help="IP to get informations")
    args = parse._args()
    if args.ip:
        get_data(args.ip)
    else:
        parse.print_help()

def get_data(ip_address):
    url = "http://www.geoiptool.com/en/?ip=" + ip_address
    response = urllib2.urlopen(url)
    if response.code ==200:
        infos = search_informations(response.read())
        return show_result(infos)
    return None
def search_informations(data):
    if data is not None:
        informations = BeautifulSoup(data)
        data_ip = informations.findAll(
            "div" ,
            {"class: sidebar-data hidden-xs hidden-sm"}
        )
        return take_informations(data_ip)

def take_informations(bs_data_found):
    data = bs_data_found[0]
    all_informations = data.findAll("span")
    dict_data = {}
    i=0
    while i< len(all_informations):
        key = str(all_informations[i].string).replace(":")
        value = str(all_informations[i+1].string)
        dict_data[key]=value
        i+=2
    return dict_data


command_line()











