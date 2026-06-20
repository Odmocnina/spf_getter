# Bulk SPF Record Fetcher

This project is a Python script designed to process a list of URLs from a CSV file, extract their domain names, query the DNS for their SPF (Sender Policy Framework) TXT records, and save the results into a new CSV file.

@Author: Michael Hladky

## 🌟 Key Features
* **Automatic URL Parsing:** The script cleans input URLs and extracts the base domain name, automatically adding an `http://` prefix if it's missing.
* **DNS TXT Lookup:** It queries the domain's DNS specifically for `TXT` records and filters for those starting with `v=spf1` to isolate the SPF configuration.
* **Robust Error Handling:** Gracefully handles and logs various DNS lookup errors, including timeouts (`DNS Timeout`), missing records (`No TXT records`), and non-existent domains (`Domain not found`).
* **Automated CSV Processing:** Uses the `pandas` library to load the input file, apply the SPF lookup row-by-row, and generate a clean output file with an appended `spf_record` column.

## 🛠️ Requirements
To run this script, you need Python installed along with the following libraries:
```bash
pip install pandas dnspython
```
*(Note: `dnspython` is required for the `dns.resolver` module used in the script. `urllib` is a built-in Python library.)*

## ⚙️ Configuration
By default, the script uses the following configuration variables inside the `main()` function:
* **Input File:** `SPF2025-finale.csv`.
* **Output File:** `output_with_spf.csv`.
* **URL Column:** Looks for a column named `url` in the input file.
* **CSV Separator:** Expects a semicolon (`;`) as the delimiter.

You can modify these variables directly inside the `main()` function if your file names or column headers differ.

## 🚀 How to Run
1. Ensure your input CSV file (`SPF2025-finale.csv`) is in the same directory as the script.
2. Make sure the CSV uses a semicolon (`;`) separator and contains a column named `url`.
3. Run the script via your terminal:
```bash
   python script_name.py
   ```
4. The terminal will output its progress. Depending on the size of the CSV, the DNS lookups may take a while.
5. Once finished, check the directory for the newly created `output_with_spf.csv` file.