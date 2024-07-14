import psutil
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

width = 800
height = 600
title = 'System and Network'
main_frame_bg = '#4090BB'
heading_font = ('Ariel', 30, 'bold')
content_font = ('Ariel', 20, 'bold')


root = ctk.CTk()
root.geometry(f'{width}x{height}')
root.title(title)
root.resizable(False, False)



left_frame = ctk.CTkFrame(root, width=width / 2.5, height= height)
left_frame.place(x = 0)

memory_heading_label = ctk.CTkLabel(left_frame, text= 'Memory: ', font= heading_font)
memory_heading_label.place(x = 20, y = 50)

total_memory_label = ctk.CTkLabel(left_frame, font= content_font)
total_memory_label.place(x = 50, y = 100)

available_memory_label = ctk.CTkLabel(left_frame, font= content_font)
available_memory_label.place(x = 50, y = 150)

used_memory_label = ctk.CTkLabel(left_frame, font= content_font)
used_memory_label.place(x = 50, y = 200)

percent_memory_label = ctk.CTkLabel(left_frame, font= content_font)
percent_memory_label.place(x = 50, y = 250)

cpu_heading_label = ctk.CTkLabel(left_frame, text= 'CPU: ', font= heading_font)
cpu_heading_label.place(x = 20, y = 350)

cpu_usage_label = ctk.CTkLabel(left_frame, font= content_font)
cpu_usage_label.place(x = 50, y = 400)

cpu_clock_speed = ctk.CTkLabel(left_frame, font= content_font)
cpu_clock_speed.place(x = 50, y = 450)

main_frame = tk.Frame(root, width= (width - (width / 2.5)), height= height, bg= main_frame_bg)
main_frame.place(x = width / 2.5)

network_heading_label = ctk.CTkLabel(main_frame, text= 'Network : ', font= heading_font)
network_heading_label.place(x = 175, y = 100)

upload_label = ctk.CTkLabel(main_frame,text= 'Upload: ', font= content_font)
upload_label.place(x = 100, y = 200)

download_label = ctk.CTkLabel(main_frame,text= 'Download: ', font= content_font)
download_label.place(x = 300, y = 200)

upload_speed = ctk.CTkLabel(main_frame, font= content_font)
upload_speed.place(x = 100, y = 250)

download_speed = ctk.CTkLabel(main_frame, font= content_font)
download_speed.place(x = 300, y = 250)

bytes_to_mb = 1024 ** 2

prev_download_traffic = psutil.net_io_counters().bytes_recv / bytes_to_mb

prev_upload_traffic = psutil.net_io_counters().bytes_sent/ bytes_to_mb

def system_and_network_info():

    global prev_download_traffic, prev_upload_traffic

    memory_info = psutil.virtual_memory()

    cpu_usage = psutil.cpu_percent(interval= 1)

    clock_speed = psutil.cpu_freq().current

    total_memory_label.configure(text = f'Total Memory: {memory_info.total / (1024 ** 3):.2f} GB')

    available_memory_label.configure(text = f'Available Memory: {memory_info.available / (1024 ** 3):.2f} GB')

    used_memory_label.configure(text = f'Used Memory: {memory_info.used / (1024 ** 3):.2f} GB')

    percent_memory_label.configure(text = f'Used: {memory_info.percent} %')

    cpu_usage_label.configure(text = f'Cpu Usage: {cpu_usage} %')

    cpu_clock_speed.configure(text = f'Clock Speed: {clock_speed} GHz')

    current_download_traffic = psutil.net_io_counters().bytes_recv / bytes_to_mb

    current_upload_traffic = psutil.net_io_counters().bytes_sent / bytes_to_mb

    download_speed.configure(text = f'{current_download_traffic - prev_download_traffic :.2f} MB/s')

    upload_speed.configure(text = f'{current_upload_traffic - prev_upload_traffic:.2f} MB/s')

    prev_upload_traffic = current_upload_traffic

    prev_download_traffic = current_download_traffic

    root.after(100, system_and_network_info)


system_and_network_info()

root.mainloop()