# 📦 File Compression Utility (Huffman Coding)

This project is a **File Compression and Decompression Tool** built using **Python**.  
It uses the **Huffman Coding algorithm** to reduce file size (compression) and restore the original file (decompression).  

---

## 🚀 Features
- ✅ Compress any file into `.huff` format  
- ✅ Decompress `.huff` files back to the original  
- ✅ Command-line interface (CLI)  
- ✅ Optional GUI using Tkinter  
- ✅ Lossless compression (no data loss)  

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Algorithm:** Huffman Coding  
- **Libraries Used:**  
  - `heapq` (priority queue for Huffman tree)  
  - `json`, `struct`, `collections`  
  - `tkinter` (optional GUI)  

---

## 📂 Project Structure
File-compress/
│── huffman.py # Main CLI-based compressor & decompressor

│── huffman_gui.py # Optional Tkinter GUI wrapper

│── example.txt # Sample file for testing

│── README.md # Project documentation

---

## ⚡ Usage

### 1️⃣ Compression

python huffman.py compress example.txt example.huff

### 2️⃣ Decompression

python huffman.py decompress example.huff restored.txt

---

🖥️ GUI Version (Optional)

python huffman_gui.py

---

📊 Example

Given example.txt:

This is a sample text file.

It will be used to test the Huffman compression utility.

---

🎯 Future Enhancements

  *Add support for other algorithms (LZW, DEFLATE)

  *Stream-based compression (for very large files)

  *Add file metadata (original filename, size)

  *Cross-platform installer using PyInstaller
