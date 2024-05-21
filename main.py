import tkinter as tk
import speedtest
import threading


def check_network_speed():
    check_button.config(state=tk.DISABLED)
    check_button.config(text="Đang kiểm tra...")

    def check_speed():
        speed_test = speedtest.Speedtest()
        speed_test.get_best_server()

        download_speed = speed_test.download() / 1024 / 1024
        upload_speed = speed_test.upload() / 1024 / 1024

        download_result.config(text=f"{round(download_speed, 2)} Mbps")
        upload_result.config(text=f"{round(upload_speed, 2)} Mbps")

        check_button.config(state=tk.NORMAL)
        check_button.config(text="Kiểm tra tốc độ")

    thread = threading.Thread(target=check_speed)
    thread.start()


root = tk.Tk()
root.title("Check network speed")
root.config(background='green')
root.geometry("500x500")

frame = tk.Frame(root, bg='green')
frame.pack(padx=50, pady=50)

download_label = tk.Label(frame, text="Tốc độ download", font=('Helvetica', 12), bg='green', fg='white', width=40,
                          height=2, highlightthickness=1)
download_label.pack(pady=7)

download_result = tk.Label(frame, text="0 Mbps", font=('Helvetica', 12), bg='green', fg='white', width=40, height=2,
                           highlightthickness=1)
download_result.pack(pady=7)

upload_label = tk.Label(frame, text="Tốc độ upload", font=('Helvetica', 12), bg='green', fg='white', width=40,
                        height=2, highlightthickness=1)
upload_label.pack(pady=7)

upload_result = tk.Label(frame, text="0 Mbps", font=('Helvetica', 12), bg='green', fg='white', width=40, height=2,
                         highlightthickness=1)
upload_result.pack(pady=7)

check_button = tk.Button(frame, text="Kiểm tra tốc độ", font=('Helvetica', 12), bg='white', fg='green', width=50,
                         height=2, command=check_network_speed)
check_button.pack(pady=7)

copyright_label = tk.Label(root, text="Copyright@vu.lct", font=('Helvetica', 10), bg='green', fg='white')
copyright_label.pack(pady=7)

root.mainloop()
