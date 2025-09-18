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

### 🖥️ GUI Version (Optional)

python huffman_gui.py

---

## 🔎 How It Works

### 1. Compression Process
1. **Read Input File** → The program reads the file as bytes.  
2. **Build Frequency Table** → Counts how many times each byte occurs.  
3. **Construct Huffman Tree** → Builds a binary tree where:
   - Rare bytes → longer codes  
   - Frequent bytes → shorter codes  
4. **Generate Huffman Codes** → Each byte gets a unique prefix-free binary code.  
5. **Encode Data** → Original data is replaced with its Huffman codes (bit stream).  
6. **Add Padding & Header** →  
   - Extra bits are added so total length is divisible by 8.  
   - The frequency table is stored in the file header (so we can decode later).  
7. **Write Output** → Saves a compressed `.huff` file.

---

### 2. Decompression Process
1. **Read Compressed File** → Extracts the header (frequency table) and bit stream.  
2. **Rebuild Huffman Tree** → Uses the frequency table to reconstruct the original coding tree.  
3. **Decode Bit Stream** → Traverses the tree bit by bit to map codes back to original bytes.  
4. **Restore Original File** → Writes the decoded bytes to the output file.  

---

### 3. Why Huffman Coding?
- Lossless compression → Original file can be perfectly restored.  
- Efficient → Common characters use fewer bits.  
- Simple to implement and demonstrates how real-world compression works (e.g., in JPEG, MP3, ZIP).

---

### 📊 Example

Given example.txt:

This is a sample text file.

It will be used to test the Huffman compression utility.

---

### 🎯 Future Enhancements

  *Add support for other algorithms (LZW, DEFLATE)

  *Stream-based compression (for very large files)

  *Add file metadata (original filename, size)

  *Cross-platform installer using PyInstaller
