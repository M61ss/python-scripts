#!/usr/bin/env python3
import argparse
from PyPDF2 import PdfReader, PdfWriter

"""
Usage is:
    python remove_pdf_password.py secret.pdf secret_unlocked.pdf -p "mypassword"
"""

def remove_password(input_path: str, output_path: str, password: str) -> None:
    """Open encrypted PDF, decrypt with given password, write an unencrypted copy."""
    reader = PdfReader(input_path)
    if reader.is_encrypted:
        # decrypt returns 0/1/2 depending on PyPDF2 version; raise if failed
        ok = reader.decrypt(password)
        if not ok and getattr(reader, "is_encrypted", False):
            raise SystemExit("Decryption failed: wrong password or unsupported encryption.")
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    with open(output_path, "wb") as out_f:
        writer.write(out_f)

def main():
    p = argparse.ArgumentParser(description="Remove password from a PDF (requires password).")
    p.add_argument("input", help="Path to input (encrypted) PDF")
    p.add_argument("output", help="Path for output (unencrypted) PDF")
    p.add_argument("-p", "--password", required=True, help="Password for the input PDF")
    args = p.parse_args()
    remove_password(args.input, args.output, args.password)
    print(f"Saved unencrypted PDF to: {args.output}")

if __name__ == "__main__":
    main()
