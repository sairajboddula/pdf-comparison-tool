
# PDF Comparison Tool

This Python script compares PDF files from two directories and generates an Excel report highlighting differences. It also checks for empty PDF files and generates checksums for file integrity.

## Pre-requisites

- **Python 3.x**: The script is written in Python, so you need Python installed. You can download it from [python.org](https://www.python.org/).
- **Required Python Libraries**:
  - `openpyxl`: For working with Excel files.
  - `pypdf`: For reading and extracting text from PDF files.
  - `hashlib`: For generating checksums (included in Python's standard library).
  - `filecmp`: For comparing files (included in Python's standard library).
  - `json`: For reading the `ignore.json` configuration file (included in Python's standard library).

Install the required libraries using pip:
```bash
pip install openpyxl pypdf

## How to Run the Code

1. **Prepare Your Directories**:
   - Create two directories: one for the baseline PDF files and another for the generated PDF files.
   - Ensure that the folder structures in both directories are identical.

2. **Update the Script**:
   - Open the `Compare.py` file and update the following variables at the bottom of the script:
     ```python
     a = "Enter your base line location"  # Replace with the path to your baseline directory
     b = "replace_with_generated_location"  # Replace with the path to your generated directory
     outpt = "Output_Location"  # Replace with the path where you want the output Excel file
     ```

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using the following command:
     ```bash
     python Compare.py
     ```

4. **Check the Output**:
   - The script will generate an Excel file in the specified output directory.
   - The Excel file will contain a summary of the comparison, including differences, checksums, and error details.

---

## Configuration

The `ignore.json` file contains configuration settings for the PDF comparison, such as the coordinates for text extraction. You can modify this file to adjust the comparison settings.

Example `ignore.json`:
```json
{
    "pdf_py": {
        "coordinates": {
            "x_min": 50,
            "x_max": 790,
            "y_min": 50,
            "y_max": 790
        }
    }
}
```

---

## Example Directory Structure

Here’s an example of how your directories should be structured:

```
Baseline_Directory/
├── Subfolder1/
│   ├── file1.pdf
│   ├── file2.pdf
├── Subfolder2/
│   ├── file3.pdf

Generated_Directory/
├── Subfolder1/
│   ├── file1.pdf
│   ├── file2.pdf
├── Subfolder2/
│   ├── file3.pdf
```

---

## Output

The script generates the following outputs:
1. **Excel Report**: A detailed comparison report in Excel format, including:
   - Matched files.
   - Differences between files.
   - Checksums for file integrity.
   - Error logs for files with issues (e.g., empty PDFs or mismatched pages).
2. **Folder Summary**: A summary of the number of files in each subfolder and any differences in file counts.

---

## Pros & Cons

### Pros
- **Automated Comparison**: Automatically compares PDF files in two directories.
- **Detailed Report**: Generates an Excel report with detailed differences, checksums, and error logs.
- **Customizable**: The `ignore.json` file allows customization of the comparison process.

### Cons
- **Limited to PDF Files**: The script only works with PDF files.
- **Coordinate-Based Extraction**: The text extraction is based on coordinates, which may not work well for all PDF layouts.
- **No GUI**: The script is command-line based, which may not be user-friendly for non-technical users.

---

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues on GitHub.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
