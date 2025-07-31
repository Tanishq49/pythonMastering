from colorama import Fore,Style,init

init(autoreset=True)
#Decorators in python

#Making an welcome function
def welcome(fx):
    def mfx():
        print("Welcome to this code")
        fx()
        print("Thanks for using this code")
    return mfx

@welcome #Modifying the sum function with the welcome function 
def use_of_python():
    python_uses = f"""{Fore.CYAN}
1. Web Development        ➤ Flask, Django
2. Data Science           ➤ Pandas, NumPy, Matplotlib
3. Machine Learning       ➤ scikit-learn, TensorFlow, PyTorch
4. Automation/Scripting   ➤ Automate boring tasks (pyautogui, os)
5. Game Development       ➤ Pygame
6. Desktop Apps           ➤ Tkinter, PyQt
7. Cybersecurity          ➤ Scripting tools, Ethical hacking
8. APIs & Web Scraping    ➤ requests, BeautifulSoup, Selenium
9. AI & Chatbots          ➤ OpenAI API, Langchain
10. Finance & Trading     ➤ Crypto bots, Stock analysis
11. IoT & Hardware        ➤ Raspberry Pi, Arduino Python libs
12. DevOps & CLI Tools    ➤ Fabric, Click, Rich
"""
    print(python_uses)
    
use_of_python()