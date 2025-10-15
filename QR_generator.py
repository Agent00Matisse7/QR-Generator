import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import os
'''
    Make a QR code t pr,ote your business, event, or your socials for free with this automated code. Works with either MacOS, Linux, and WindowsOS
'''
PORT = 8000
# Convert to Windows path if necessarily
mac_desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
share_dir_name = "You're_Preferred_Name"
share_path = os.path.join(mac_desktop_path, share_dir_name)


if not os.path.exists(share_path):
    os.makedirs(share_path)
os.chdir(share_path)
print(f"Serving files from: {share_path}")

Handler = http.server.SimpleHTTPRequestHandler

# Get the local IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("8.8.8.8", 80))
    local_ip_address = s.getsockname()[0]
finally:
    s.close()
link_to_encode = "http://Your_Link_Here" # Add your link here
server_ip_link = f"http://{local_ip_address}:{PORT}"
qr_code = pyqrcode.create(link_to_encode)
qr_filename_svg = "You're_Preferred_Name.svg" # Change to file name
qr_code.svg(qr_filename_svg, scale=8)
svg_file_path = os.path.join(share_path, qr_filename_svg)
print(f"Opening QR code: {svg_file_path}")
webbrowser.open(f'file://{svg_file_path}')
with socketserver.TCPServer((local_ip_address, PORT), Handler) as httpd:
    print("-" * 30)
    print("🚀 Server Started Successfully 🚀")
    print(f"Serving files from: {share_path}")
    print(f"Type this in your Browser: {server_ip_link}")
    print(f"QR Code links to: {link_to_encode}")
    print("-" * 30)
    httpd.serve_forever()