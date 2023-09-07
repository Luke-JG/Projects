import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import requests
from bs4 import BeautifulSoup

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Web Scraper')
        self.root.geometry('600x600')

        self.url_label = ttk.Label(root, text='Enter URL:')
        self.url_label.pack(pady=10)

        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.pack()

        self.links_var = tk.BooleanVar()
        self.links_check = ttk.Checkbutton(root, text='Scrape Links', variable=self.links_var)
        self.links_check.pack()

        self.images_var = tk.BooleanVar()
        self.images_check = ttk.Checkbutton(root, text='Scrape Images', variable=self.images_var)
        self.images_check.pack()

        self.headings_var = tk.BooleanVar()
        self.headings_check = ttk.Checkbutton(root, text='Scrape Headings', variable=self.headings_var)
        self.headings_check.pack()

        self.scrape_button = ttk.Button(root, text='Scrape', command=self.scrape_website)
        self.scrape_button.pack(pady=10)

        self.result_text = tk.Text(root, wrap=tk.WORD, width=60, height=20)
        self.result_text.pack(padx=10, pady=10)

        self.progress_bar = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
        self.progress_bar.pack(pady=10)

        format_label = ttk.Label(root, text='Select Output Format:')
        format_label.pack()

        self.format_var = tk.StringVar()
        self.format_var.set('Text')

        self.format_dropdown = ttk.OptionMenu(root, self.format_var, 'Text', 'CSV', 'JSON')
        self.format_dropdown.pack()

        self.edit_button = ttk.Button(root, text='Edit Data', command=self.edit_data)
        self.edit_button.pack(pady=5)

        self.save_button = ttk.Button(root, text='Save to File', command=self.save_to_file)
        self.save_button.pack()

    def scrape_website(self):
        url = self.url_entry.get()
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            selected_data = []
            if self.links_var.get():
                selected_data.extend(soup.find_all('a', href=True))
            if self.images_var.get():
                selected_data.extend(soup.find_all('img', src=True))
            if self.headings_var.get():
                selected_data.extend(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']))

            if selected_data:
                self.display_result(selected_data)
            else:
                self.display_result(['No data found.'])
                
        except requests.exceptions.RequestException as e:
            self.display_result([f'Error: {e}'])
        except Exception as e:
            self.display_result([f'Error: {str(e)}'])

    def display_result(self, data):
        self.clear_result_text()
        for item in data:
            self.result_text.insert(tk.END, str(item) + '\n')

    def clear_result_text(self):
        self.result_text.delete(1.0, tk.END)

    def edit_data(self):
        # Open a text editor to allow editing of scraped data
        data_to_edit = self.result_text.get(1.0, tk.END)
        if data_to_edit.strip():
            editor = tk.Toplevel(self.root)
            editor.title('Edit Data')
            editor.geometry('800x600')

            edit_text = tk.Text(editor, wrap=tk.WORD, width=80, height=25)
            edit_text.pack(padx=10, pady=10)
            edit_text.insert(tk.END, data_to_edit)

            save_button = ttk.Button(editor, text='Save Changes', command=lambda: self.save_edited_data(edit_text))
            save_button.pack()

    def save_edited_data(self, edit_text):
        edited_data = edit_text.get(1.0, tk.END)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, edited_data)

    def save_to_file(self):
        data_to_save = self.result_text.get(1.0, tk.END)
        if data_to_save.strip():
            file_path = filedialog.asksaveasfilename(defaultextension=self.format_var.get())
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(data_to_save)
                messagebox.showinfo('Save to File', 'Data saved successfully.')
        else:
            messagebox.showinfo('Save to File', 'No data to save.')

if __name__ == '__main__':
    root = tk.Tk()
    app = WebScraperApp(root)
    root.mainloop()
