import whois
import subprocess

def is_reg(d_name):
    try:
        whois_info = whois.whois(d_name)
        print("Domain Register: ",whois_info.register)
        print("Domain Server: ",whois_info.whois_server)
        print("Domain Creation Date: ",whois_info.creation_date)
        print("Domain Expiration Date: ",whois_info.expiration_date)
        print(whois_info)
    except Exception:
        print('Internet Not avialable')
        return False
  
def ip(ip_add):
    out = subprocess.run(["whois", ip_add],capture_output=True,text=True)       


    fdtxt = out.stdout.find("NetRange")
    fdtxt1 = out.stdout.find("OrgAbuseRef")

    print(out.stdout[int(fdtxt):int(fdtxt1)])