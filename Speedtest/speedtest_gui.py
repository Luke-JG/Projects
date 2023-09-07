import tkinter as tk
import speedtest

def get_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    
    download_speed = st.download() / 10**6  # Mbps
    upload_speed = st.upload() / 10**6  # Mbps
    
    download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
    upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")

# Create the main application window
app = tk.Tk()
app.title("Internet Speed Test")

# Create labels for displaying speed results
download_label = tk.Label(app, text="")
download_label.pack()
upload_label = tk.Label(app, text="")
upload_label.pack()

# Create a button to trigger the speed test
test_button = tk.Button(app, text="Run Speed Test", command=get_speed)
test_button.pack()

# Run the GUI application
app.mainloop()
