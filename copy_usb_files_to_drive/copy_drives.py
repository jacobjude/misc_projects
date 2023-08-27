import os
import shutil
import win32file
import time
import threading

def get_drives():
    drives = []
    bitmask = win32file.GetLogicalDrives()
    for letter in map(chr, range(65, 91)):
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

def copy_files(src, dst, current_usb_number, port_number):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            os.makedirs(d, exist_ok=True)
            try:
                copy_files(s, d, current_usb_number, port_number)  # Recursive call
            except Exception as e:
                print(f"Error copying folder: {type(e)}: {e}")
        else:
            print(f"Copying file: {item} (Port {port_number}))")
            try:
                shutil.copy2(s, d)
            except Exception as e:
                print(f"Error copying file: {type(e)}: {e}")

def copy_from_drive(drive, current_usb_number, port_number):
    try:
        print(f"Copying files from {drive} to D:")
        # Create a new folder with a unique name
        new_folder = "D:\\USB files 4\\" + "USB " + str(current_usb_number)
        print("Creating new folder: " + new_folder)
        os.mkdir(new_folder)
        copy_files(f"{drive}:\\", new_folder, current_usb_number, port_number)
        print(f"(Done) Files copied from {drive}")
    except Exception as e:
        print(f"FATAL ERROR: {type(e)}: {e}")
        print(f"Error occurred while copying files from {drive}, current USB number: {current_usb_number}, port number: {port_number}")
    usb_status[port_number] = {f"Finished on port {port_number}": new_folder}

if __name__ == "__main__":
    current_usb_number = 0 # tracks the number of USBs that have been plugged in
    port_number = 0
    usb_status = ["None", "None", "None", "None"]  # track USBs in each of the four ports. usb_status[0] represents the first port, usb_status[1] represents the second port, etc.
    print("Monitoring for new USB devices...")
    old_drives = get_drives()
    while True:
        new_drives = get_drives()
        added = [drive for drive in new_drives if drive not in old_drives]
        if added:
            print(f"New drive(s) detected: {', '.join(added)}")
            for drive in added:
                try:
                    port_number = int(input("Which port is the USB in? "))
                    usb_status[port_number] = "Copying"
                except:
                    print("Invalid port number")
                    while True:
                        try:
                            port_number = int(input("Which port is the USB in? "))
                            usb_status[port_number] = "Copying"
                            break
                        except:
                            print("Invalid port number")
                threading.Thread(target=copy_from_drive, args=(drive, current_usb_number, port_number)).start()
                current_usb_number += 1
        old_drives = new_drives
        print(f"\n{usb_status}\n")  # Print the status of each USB
        time.sleep(2)
