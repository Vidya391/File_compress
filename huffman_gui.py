# huffman_gui.py
# Requires huffman.py in same folder.
import tkinter as tk
from tkinter import filedialog, messagebox
from huffman import compress_file, decompress_file

def choose_compress():
    infile = filedialog.askopenfilename(title="Select file to compress")
    if not infile:
        return
    outfile = filedialog.asksaveasfilename(defaultextension=".huff", title="Save compressed as")
    if not outfile:
        return
    compress_file(infile, outfile)
    messagebox.showinfo("Done", f"Compressed to {outfile}")

def choose_decompress():
    infile = filedialog.askopenfilename(title="Select .huff file to decompress", filetypes=[("Huffman", "*.huff"), ("All files", "*.*")])
    if not infile:
        return
    outfile = filedialog.asksaveasfilename(title="Save decompressed as")
    if not outfile:
        return
    decompress_file(infile, outfile)
    messagebox.showinfo("Done", f"Decompressed to {outfile}")

root = tk.Tk()
root.title("Huffman File Compression")
root.geometry("400x150")
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True, fill="both")
tk.Button(frame, text="Compress File", command=choose_compress, width=20).pack(pady=8)
tk.Button(frame, text="Decompress File", command=choose_decompress, width=20).pack(pady=8)
tk.Button(frame, text="Quit", command=root.quit, width=20).pack(pady=8)
root.mainloop()
