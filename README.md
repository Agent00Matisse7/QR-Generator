 Local QR Code & File Share Server

This script automates the process of generating a QR code for any link, saving it to your desktop, and instantly launching a local HTTP server so you can easily share the generated file (or any other files in the directory) with others on your local network.

 Features

Automated QR Generation: Creates an SVG file containing a scannable QR code for a link you define.

Instant Access: Automatically opens the generated QR code image in your default web browser for quick viewing.

Local Server: Starts an HTTP server on your local IP address and a defined port (8000 by default), allowing anyone on the same Wi-Fi or local network to access the files in the share folder.

Cross-Platform: Designed to work on macOS, Linux, and Windows.

 Prerequisites

You must have Python 3.x installed on your system.

Dependencies

This script requires two external Python packages: pyqrcode and pypng.

You can install them using pip:

------------------------------------------------------------
      pip install pyqrcode pypng
------------------------------------------------------------

 Setup and Configuration

Before running the script, you must configure the following three variables inside the qr_server_starter.py file to customize your QR code and server environment.

link_to_encode (MANDATORY)

The URL (e.g., your website, social media, event registration) that the QR code will link to.

Example: link_to_encode = "http://Your_Link_Here"

share_dir_name

The name of the folder that will be created on your Desktop to hold the QR code and other shareable files.

Example: share_dir_name = "You're_Preferred_Name"

qr_filename_svg

The filename for the generated SVG image.

Example: qr_filename_svg = "My_Event_Poster.svg"

▶Usage

Configure: Edit the three variables listed in the Setup and Configuration section of the qr_server_starter.py file.

Run the script: Navigate to the directory where you saved the Python file and execute it:

python qr_server_starter.py


Check Output: The console will display a clear welcome script with the server status, the local IP address, and the URL for access. The script will also automatically open the generated SVG file in your browser.


QR Code Link Server Running

Local IP Address (for sharing): 192.168.x.x
Serving Port:                   8000
Serving Files From:             /Users/user/Desktop/QR_Share_Files
------------------------------------------------------------
Access URL: The direct link to use is displayed below.
    -> [http://192.168.x.x:8000](http://192.168.x.x:8000)
------------------------------------------------------------
QR Code Destination: The link encoded in the SVG file.
    -> [https://your-business-site.com](https://your-business-site.com)
------------------------------------------------------------
Action: The QR code file (.svg) has been opened in your default browser.
Note: Keep this window open. The server will run until you manually stop it.
------------------------------------------------------------


Share the Link: Share the Access URL (e.g., http://192.168.x.x:8000) with anyone on your network. They can use that link in their browser to view and download the QR code or any other files you place in the share folder.

Stop the Server: The server will run indefinitely. Press Ctrl + C in the terminal window to stop the server.
