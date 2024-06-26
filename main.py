import tkinter as tk
import speedtest
import threading


def check_network_speed():
    check_button.config(state=tk.DISABLED)
    check_button.config(text="Checking...")

    def check_speed():
        speed_test = speedtest.Speedtest()
        speed_test.get_best_server()

        download_speed = speed_test.download() / 1024 / 1024
        upload_speed = speed_test.upload() / 1024 / 1024

        download_result.config(text=f"{round(download_speed, 2)} Mbps")
        upload_result.config(text=f"{round(upload_speed, 2)} Mbps")

        check_button.config(state=tk.NORMAL)
        check_button.config(text="Start Test")

    thread = threading.Thread(target=check_speed)
    thread.start()


root = tk.Tk()
root.title("Check network speed")
root.config(background='green')
window_width = 500
window_height = 500
x_pos = int((root.winfo_screenwidth() - window_width) // 2)
y_pos = int((root.winfo_screenheight() - window_height) // 2)
root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

frame = tk.Frame(root, bg='green')
frame.pack(padx=50, pady=50)

label_style = {'font': ('Helvetica', 12), 'bg': 'green', 'fg': 'white', 'width': 40, 'height': 2,
               'highlightthickness': 1}

button_style = {'font': ('Helvetica', 12), 'bg': 'white', 'fg': 'green', 'width': 50, 'height': 2}

copyright_style = {'font': ('Helvetica', 10), 'bg': 'green', 'fg': 'white', 'border': 0}

download_label = tk.Label(frame, text="Download speed", **label_style)
download_label.pack(pady=7)

download_result = tk.Label(frame, text="0 Mbps", **label_style)
download_result.pack(pady=7)

upload_label = tk.Label(frame, text="Upload speed", **label_style)
upload_label.pack(pady=7)

upload_result = tk.Label(frame, text="0 Mbps", **label_style)
upload_result.pack(pady=7)

check_button = tk.Button(frame, text="Start Test", command=check_network_speed, **button_style)
check_button.pack(pady=7)

copyright_label = tk.Label(root, text="Copyright@vu.lct", **copyright_style)
copyright_label.pack(pady=7)

root.mainloop()
