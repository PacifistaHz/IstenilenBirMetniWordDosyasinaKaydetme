import docx

# Belgenin yolunu belirtin
doc_path = "32.docx"

# Word belgesini aç
doc = docx.Document(doc_path)

# Tüm paragrafları al
all_paras = doc.paragraphs

# Her bir paragrafı yazdır
for para in all_paras:
    print(para.text)
