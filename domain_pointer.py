#!/usr/bin/python3
import argparse,os,subprocess
parser=argparse.ArgumentParser(description="This is DNS tool to find all types of records.")
parser.add_argument('-d',type=str,help="Use with domain ", required=True)
parser.add_argument('-reconall',help="Use this to find all the records ", required=False, action='store_true')

a=parser.parse_args()
domain=a.d
recon=a.reconall
ips,ns,soas,mxs,ptrs,txt_ls=[],[],[],[],[],[]
f=open("output.txt", "w+")

def all_ipv4():
    ip_list=os.popen("host -t A "+ domain).read()
    if "has address" in ip_list:
    	s=ip_list.split()
    	for i in range(3,len(s),4):
    		ips.append(s[i])
    	output="\nAll IP records are ", ", ".join(ips)
    	print("\nAll IP records are ", ", ".join(ips))
    else:
    	output="\n0 Ip records found."
    	print("\n 0 Ip records found.")
    f.writelines(ip_list)
    f.writelines(output)
    

def all_ipv6():
    # ipv6 =str(subprocess.check_output("host -t AAAA "+ domain, shell=True), 'UTF-8')  
    ipv6 = os.popen("host -t AAAA "+ domain).read()
    print("\n",ipv6)
    f.writelines(ipv6)


def all_ns_list():
    ns_list=os.popen("host -t NS "+ domain).read()
    if "name server" in ns_list:
    	s=ns_list.split()
    	for i in range(3,len(s),4):
    		ns.append(s[i])
    	output="\nAll NS records are " , domain , "are ", ", ".join(ns)
    	print("\nAll NS records are " , domain , "are ", ", ".join(ns))
    else:
    	output="\n0 NS records found."
    	print("\n 0 NS records found.")
    f.writelines(ns_list)
    f.writelines(output)


def all_soa_list():
    soa_list=os.popen("host -t SOA "+ domain).read()
    if "has SOA record " in soa_list:
        soa_list=soa_list.split("has SOA record ")[1]
        soa_list=soa_list.split()
        for i in soa_list:
            if i.isdigit()==False and "." in i:
                soas.append(i)
        output="\nAll SOA records are :", ', '.join(soas)
        print("\nAll SOA records are :", ', '.join(soas))
    else:
    	output="\n0 SOA records found."
    	print("\n 0 SOA records found.")
    f.writelines(soa_list)
    f.writelines(output)
    
def all_mx_list():
    #mx_list = str(subprocess.check_output("host -t MX "+ domain, shell=True), 'UTF-8')
    mx_list = os.popen("host -t MX "+ domain).read()
    if "is handled by" in mx_list:
        s=mx_list.split()
        for i in range(6,len(s),7):
        	mxs.append(s[i])
        output="\nAll MX record are ", ", ".join(mxs)
        print("\nAll MX record are ", ", ".join(mxs))
    else:
    	output="\n0 MX records found."
    	print("\n 0 MX records found.")
    f.writelines(mx_list)
    f.writelines(output)


def all_txt_ls():
    if len(mxs)==0:
    	output="\n0 TXT records found."
    	print("\n0 TXT records found.")
    else:
        for i in mxs:
           
            try:
                txt=os.popen("host -t TXT "+ i).read()
                txt_ls.append(txt)
            except:
                txt_ls.append("TXT not found for this {}".format(i))
            f.writelines(txt)
        output="\nAll TXT records are ", ", ".join(txt_ls)
        print("\nAll TXT records are ", ", ".join(txt_ls))

    f.writelines(output)
 
def all_ptr_ls():
    if len(ips)==0:
    	output="\n0 PTR records found."
    	print("\n0 PTR records found.")
    else:
        for i in ips:
            ptr_ls = os.popen("host -t PTR "+ i).read()
            s=ptr_ls.split()
            ptrs.append(s[0])
            f.writelines(ptr_ls)
        output="\nAll ptr records are: ", ", ".join(ptrs)
        print("\nAll ptr records are: ", ", ".join(ptrs))
    f.writelines(output)
        
        
    
if recon is False:
    all_ipv4()
    print("================Complete====================")
else:
    
    all_ipv4()
    print("============================================")
    f.writelines("\n============================================\n")

    all_ipv6()
    print("============================================")
    f.writelines("\n============================================\n")

    all_ns_list()
    print("============================================")
    f.writelines("\n============================================\n")

    all_soa_list()
    print("============================================")
    f.writelines("\n============================================\n")

    all_mx_list()
    print("============================================")
    f.writelines("\n============================================\n")

    all_txt_ls()
    print("============================================")
    f.writelines("\n============================================\n")

    all_ptr_ls()
    print("================Complete====================")
    f.writelines("\n================Complete====================")

f.close()
    
    
    

    
    
    
    
    
    

    

