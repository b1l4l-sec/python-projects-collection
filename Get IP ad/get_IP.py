#import the module
import socket

def get_ips_for_host(host):
    try:
        ips = socket.gethostbyname_ex(host)
    except socket.gaierror:
        ips=[]
    return ips

ips = get_ips_for_host('www.google.com') # i have another code do the same work
print(repr(ips))
#hello long tome no see so in this video we ll see how to get websites IP just fropm the URL of the website 
# as all of us know that the DNS domain name server translate the ip into a url so with this code well do like reverse engineering of DNS (get IP adress by URL) let s see 