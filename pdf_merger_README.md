# 📄 Python PDF Merger & Splitter Tool

A simple command-line tool to merge multiple PDFs into one, or split a PDF into individual pages.

## 📌 What it does
- **Merge** — Combine 2 or more PDFs into a single file
- **Split** — Break a PDF into individual page files
- **Info** — Show page count and basic details of any PDF

## 🛠️ Requirements

```bash
pip install pypdf
```

## ▶️ How to run

```bash
python pdf_tool.py
```

Choose from the menu:
```
1. Merge multiple PDFs into one
2. Split a PDF into individual pages
3. Get PDF info
```

## 📂 Output example (Merge)

```
📎 Merging 3 PDF files...

  ✅ Added: invoice_jan.pdf (2 pages)
  ✅ Added: invoice_feb.pdf (2 pages)
  ✅ Added: invoice_mar.pdf (3 pages)

🎉 Merged successfully!
   Output file : merged_output.pdf
   Total pages : 7
```

## 📂 Output example (Split)

```
✂️  Splitting 'report.pdf' (5 pages)...

  ✅ Saved: page_1.pdf
  ✅ Saved: page_2.pdf
  ✅ Saved: page_3.pdf
  ✅ Saved: page_4.pdf
  ✅ Saved: page_5.pdf

🎉 Split complete! 5 pages saved to 'report_split_pages/'
```

## 👨‍💻 Author
**Faizal Khan** — Python Developer & Automation Specialist  
[Fiverr](https://www.fiverr.com/faizalpathan369) | [GitHub](https://github.com/faizal911)
