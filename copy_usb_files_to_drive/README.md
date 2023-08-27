# USB to Hard Drive File Transfer (Windows)
I had to copy files from a whole bunch of USBs over to a hard drive so I created this little script to help automate the process a little.

This Python script automates the process of copying files from multiple USB drives to a hard drive. It identifies newly inserted USB drives, creates a root folder named "USB-files-python" on the hard drive (modifiable), and copies all files and folders from the USB to a labeled subfolder within the root folder. The script supports concurrent file transfer from multiple USB drives.

## Setup 
1. Run `copy_drives.py` (Requires Python 3.10 or higher).
2. Input the letter of your hard drive where you want to transfer files (e.g., "D").
3. Specify the number of USB ports you intend to use.

## Usage
1. Insert your USB.
2. Input the port number where you inserted the USB. (Note: Due to limitations, you need to manually assign labels to the ports. For instance, if your machine has four ports, you could label the top port as 0, the rightmost side port as 1, and so on.)
3. The script will now copy the files from the USB. You can insert another USB into a different port for concurrent file transfer.
4. Repeat as needed.

The process is logged to the console. Upon completion of file transfer from a USB, the console will display "Finished" along with the port number of the USB and the path to the subfolder that the files have been copied to.
