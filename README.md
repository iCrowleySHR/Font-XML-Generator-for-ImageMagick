# 🖋️ Font XML Generator for ImageMagick

This Python script generates an XML file (`type.xml`) with metadata for all installed TrueType (`.ttf`) and OpenType (`.otf`) fonts on a Windows system.  
The output is compatible with **ImageMagick**'s font configuration format.

---

## 📌 Purpose

ImageMagick can be configured to recognize system fonts using a `type.xml` file.  
This script automates the creation of that file by scanning the default Windows font directories.

---

## ⚙️ How It Works

1. **Font Directories Scanned**:
   - `C:/Windows/Fonts`
   - `C:/Users/<USERNAME>/AppData/Local/Microsoft/Windows/Fonts`

2. **Supported Extensions**:
   - `.ttf`
   - `.otf`

3. **Duplicate Handling**:
   - Fonts with the same name (based on filename without extension) are only added once.

4. **Generated XML Structure**:
   Each font entry includes:
   - `name`: font file name (without extension)
   - `fullname`: same as name
   - `family`: same as name
   - `style`: `"Normal"`
   - `stretch`: `"Normal"`
   - `weight`: `"400"`
   - `glyphs`: full path to the font file

5. **Output**:
   - Writes all font entries to a `type.xml` file in the current directory.
