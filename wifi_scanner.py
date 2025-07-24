import pywifi
from pywifi import const
import time

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Get the first wireless interface
    iface.scan()  # Start scanning
    time.sleep(3)  # Wait for the scan to complete

    results = iface.scan_results()

    print("\n🔍 Available Wi-Fi Networks:")
    print("-" * 40)
    for network in results:
        ssid = network.ssid
        signal = network.signal
        bssid = network.bssid
        print(f"SSID: {ssid}\nBSSID: {bssid}\nSignal Strength: {signal} dBm\n" + "-" * 40)

if __name__ == "__main__":
    scan_wifi()
