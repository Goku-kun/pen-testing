import socket
import optparse
from socket import *
def conn(target_host, target_port):
      try:
            skt = socket(AF_INET, SOCK_STREAM)
            skt.connect((target_host, target_port))
            skt.send("Violent Python \n")
            results = skt.receive(1024)
            print("[+] TCP port {} is open".format(target_port))
            print("[+] {}".format(str(results)))

      except:
            print("[+] TCP port {} is closed".format(target_port))

def port_scan(target_host, target_ports):
      try:
            tgtip = gethostbyname(target_host)
      except:
            print("[-] cannot resolve {}: Unknown host".format(target_host))
            return
      try:
            tgtName = gethostbyaddr(tgtip)
            print("[+] Scan results: {} for the host:".format(tgtName))
      except:
            print("[+] Scan results: {} for the target host:".format(target_host))
      setdefaulttimeout(1)

      for target_port in target_ports:
            print("Scanning port: {}".format(target_port))
            conn(target_host, target_port)

def main():
      parser = optparse.OptionParser(" usage%prog "+\
            "-H <target host> -p <target ports>")
      parser.add_option("-H", dest="thost", type="string", help="specify host target")
      parser.add_option("-p", dest="tport", type="string", help="specify target ports")
      (options, args) = parser.parse_args()
      thost = options.thost
      tport = str(options.tport).split(",")
      if (thost == None) | (tport[0] == None):
            print("You must specify target host and ports")
            exit(0)
      port_scan(thost, tport)

if __name__ == "__main__":
      main()