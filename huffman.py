# huffman.py
# Python 3.8+
# Usage:
#   python huffman.py compress input.bin output.huff
#   python huffman.py decompress input.huff output.bin

import sys
import heapq
import collections
import json
import struct
from typing import Dict, Tuple

class Node:
    def __init__(self, freq, byte=None, left=None, right=None):
        self.freq = freq
        self.byte = byte
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(data: bytes) -> Dict[int, int]:
    return dict(collections.Counter(data))

def build_huffman_tree(freq_table: Dict[int, int]) -> Node:
    heap = []
    for b, freq in freq_table.items():
        heapq.heappush(heap, Node(freq, byte=b))
    if len(heap) == 0:
        return None
    if len(heap) == 1:
        # special-case: only one symbol — duplicate to make tree valid
        only = heapq.heappop(heap)
        parent = Node(only.freq, left=only, right=Node(0, byte=None))
        return parent
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        parent = Node(a.freq + b.freq, left=a, right=b)
        heapq.heappush(heap, parent)
    return heapq.heappop(heap)

def build_code_map(root: Node) -> Dict[int, str]:
    codes = {}
    def dfs(node, path):
        if node is None:
            return
        if node.byte is not None:
            codes[node.byte] = path or "0"  # handle single-symbol case
            return
        dfs(node.left, path + "0")
        dfs(node.right, path + "1")
    dfs(root, "")
    return codes

def encode_data(data: bytes, code_map: Dict[int, str]) -> Tuple[bytes, int]:
    bit_str = "".join(code_map[b] for b in data)
    padding = (8 - len(bit_str) % 8) % 8
    if padding:
        bit_str += "0" * padding
    out = bytearray()
    for i in range(0, len(bit_str), 8):
        byte = bit_str[i:i+8]
        out.append(int(byte, 2))
    return bytes(out), padding

def decode_bits(bit_bytes: bytes, padding: int, root: Node) -> bytes:
    # traverse tree bit-by-bit
    bit_str = "".join(f"{b:08b}" for b in bit_bytes)
    if padding:
        bit_str = bit_str[:-padding]
    out = bytearray()
    node = root
    for ch in bit_str:
        node = node.left if ch == "0" else node.right
        if node.byte is not None:
            out.append(node.byte)
            node = root
    return bytes(out)

def compress_file(in_path: str, out_path: str):
    with open(in_path, "rb") as f:
        data = f.read()
    freq_table = build_frequency_table(data)
    root = build_huffman_tree(freq_table)
    if root is None:
        # empty file: write empty header + zero padding
        with open(out_path, "wb") as out:
            out.write(struct.pack(">I", 0))
        print("Compressed empty file.")
        return

    code_map = build_code_map(root)
    encoded_bytes, padding = encode_data(data, code_map)

    # Store header as: 4-byte length N, then JSON of freq_table (keys are ints), then 1 byte padding
    header_json = json.dumps(freq_table).encode('utf-8')
    header_len = len(header_json)
    with open(out_path, "wb") as out:
        out.write(struct.pack(">I", header_len))
        out.write(header_json)
        out.write(struct.pack("B", padding))
        out.write(encoded_bytes)
    orig = len(data)
    comp = 4 + header_len + 1 + len(encoded_bytes)
    print(f"Compressed {in_path} -> {out_path} | original={orig} bytes, compressed={comp} bytes")

def decompress_file(in_path: str, out_path: str):
    with open(in_path, "rb") as f:
        header_len_bytes = f.read(4)
        if not header_len_bytes:
            # treat empty file
            with open(out_path, "wb") as out:
                out.write(b"")
            print("Decompressed empty file.")
            return
        header_len = struct.unpack(">I", header_len_bytes)[0]
        header_json = f.read(header_len)
        freq_table = json.loads(header_json.decode('utf-8'))
        padding_byte = f.read(1)
        if not padding_byte:
            print("Corrupt file: missing padding byte.")
            return
        padding = struct.unpack("B", padding_byte)[0]
        bit_bytes = f.read()
    # rebuild tree
    freq_table = {int(k): v for k, v in freq_table.items()}
    root = build_huffman_tree(freq_table)
    if root is None:
        with open(out_path, "wb") as out:
            out.write(b"")
        print("Decompressed empty file.")
        return
    decoded = decode_bits(bit_bytes, padding, root)
    with open(out_path, "wb") as out:
        out.write(decoded)
    print(f"Decompressed {in_path} -> {out_path} | output bytes={len(decoded)}")

def main():
    if len(sys.argv) < 4:
        print("Usage:")
        print("  python huffman.py compress input_file output_file.huff")
        print("  python huffman.py decompress input_file.huff output_file")
        return
    cmd = sys.argv[1].lower()
    if cmd == "compress":
        compress_file(sys.argv[2], sys.argv[3])
    elif cmd == "decompress":
        decompress_file(sys.argv[2], sys.argv[3])
    else:
        print("Unknown command:", cmd)

if __name__ == "__main__":
    main()
