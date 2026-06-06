import os
import sys

# ─────────────────────────────────────────
# PDF MERGER TOOL — by Faizal Khan
# Merges multiple PDF files into one,
# or splits a PDF into individual pages.
# ─────────────────────────────────────────

try:
    from pypdf import PdfWriter, PdfReader
except ImportError:
    print("❌ pypdf not installed. Run: pip install pypdf")
    sys.exit(1)


def merge_pdfs(pdf_files, output_filename=None):
    """
    Merges a list of PDF files into one single PDF.

    pdf_files: list of PDF file paths
    output_filename: name for the merged output file
    """

    if len(pdf_files) < 2:
        print("❌ Please provide at least 2 PDF files to merge.")
        return

    # Check all files exist
    for f in pdf_files:
        if not os.path.exists(f):
            print(f"❌ File not found: {f}")
            return
        if not f.lower().endswith('.pdf'):
            print(f"❌ Not a PDF file: {f}")
            return

    if not output_filename:
        output_filename = "merged_output.pdf"

    # Create a PDF writer object
    writer = PdfWriter()

    print(f"\n📎 Merging {len(pdf_files)} PDF files...\n")

    total_pages = 0

    for pdf_path in pdf_files:
        # Create a reader for each PDF
        reader = PdfReader(pdf_path)
        pages = len(reader.pages)

        # Add every page from this PDF to the writer
        for page in reader.pages:
            writer.add_page(page)

        total_pages += pages
        print(f"  ✅ Added: {os.path.basename(pdf_path)} ({pages} pages)")

    # Write the final merged PDF to disk
    with open(output_filename, 'wb') as output_file:
        writer.write(output_file)

    print(f"\n🎉 Merged successfully!")
    print(f"   Output file : {output_filename}")
    print(f"   Total pages : {total_pages}")


def split_pdf(input_file, output_folder=None):
    """
    Splits a PDF into individual pages.
    Each page becomes its own PDF file.
    """

    if not os.path.exists(input_file):
        print(f"❌ File not found: {input_file}")
        return

    if not output_folder:
        base = os.path.splitext(os.path.basename(input_file))[0]
        output_folder = f"{base}_split_pages"

    os.makedirs(output_folder, exist_ok=True)

    reader = PdfReader(input_file)
    total = len(reader.pages)

    print(f"\n✂️  Splitting '{os.path.basename(input_file)}' ({total} pages)...\n")

    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)

        output_path = os.path.join(output_folder, f"page_{i+1}.pdf")
        with open(output_path, 'wb') as f:
            writer.write(f)

        print(f"  ✅ Saved: page_{i+1}.pdf")

    print(f"\n🎉 Split complete! {total} pages saved to '{output_folder}/'")


def get_pdf_info(pdf_path):
    """Shows basic information about a PDF."""
    if not os.path.exists(pdf_path):
        print(f"❌ File not found: {pdf_path}")
        return

    reader = PdfReader(pdf_path)
    print(f"\n📄 PDF Info: {os.path.basename(pdf_path)}")
    print(f"   Pages     : {len(reader.pages)}")
    print(f"   Encrypted : {reader.is_encrypted}")


# ─── MAIN PROGRAM ───
if __name__ == "__main__":
    print("=" * 45)
    print("       📄 Python PDF Merger Tool")
    print("=" * 45)
    print("\nWhat do you want to do?")
    print("  1. Merge multiple PDFs into one")
    print("  2. Split a PDF into individual pages")
    print("  3. Get PDF info")

    choice = input("\nEnter choice (1/2/3): ").strip()

    if choice == '1':
        print("\nEnter PDF file paths one by one.")
        print("Press ENTER with empty input when done.\n")
        files = []
        while True:
            path = input(f"PDF file {len(files)+1}: ").strip()
            if not path:
                break
            files.append(path)

        if files:
            output = input("\nOutput filename (press Enter for 'merged_output.pdf'): ").strip()
            output = output if output else "merged_output.pdf"
            merge_pdfs(files, output)

    elif choice == '2':
        path = input("\nEnter PDF file path to split: ").strip()
        split_pdf(path)

    elif choice == '3':
        path = input("\nEnter PDF file path: ").strip()
        get_pdf_info(path)

    else:
        print("❌ Invalid choice.")
