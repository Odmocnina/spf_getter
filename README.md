# Bulk SPF Record Fetcher

This project is a Python script designed to process a list of URLs from a CSV file, extract their domain names, query the DNS for their SPF (Sender Policy Framework) TXT records, and save the results into a new CSV file[cite: 9].

@Author: Michael Hladky

## 🌟 Key Features
* **Automatic URL Parsing:** The script cleans input URLs and extracts the base domain name, automatically adding an `http://` prefix if it's missing[cite: 9].
* **DNS TXT Lookup:** It queries the domain's DNS specifically for `TXT` records and filters for those starting with `v=spf1` to isolate the SPF configuration[cite: 9].
* **Robust Error Handling:** Gracefully handles and logs various DNS lookup errors, including timeouts (`DNS Timeout`), missing records (`No TXT records`), and non-existent domains (`Domain not found`)[cite: 9].
* **Automated CSV Processing:** Uses the `pandas` library to load the input file, apply the SPF lookup row-by-row, and generate a clean output file with an appended `spf_record` column[cite: 9].

## 🛠️ Requirements
To run this script, you need Python installed along with the following libraries:
```bash
pip install pandas dnspython
```
*(Note: `dnspython` is required for the `dns.resolver` module used in the script[cite: 9]. `urllib` is a built-in Python library[cite: 9].)*

## ⚙️ Configuration
By default, the script uses the following configuration variables inside the `main()` function[cite: 9]:
* **Input File:** `SPF2025-finale.csv`[cite: 9].
* **Output File:** `output_with_spf.csv`[cite: 9].
* **URL Column:** Looks for a column named `url` in the input file[cite: 9].
* **CSV Separator:** Expects a semicolon (`;`) as the delimiter[cite: 9].

You can modify these variables directly inside the `main()` function if your file names or column headers differ[cite: 9].

## 🚀 How to Run
1. Ensure your input CSV file (`SPF2025-finale.csv`) is in the same directory as the script[cite: 9].
2. Make sure the CSV uses a semicolon (`;`) separator and contains a column named `url`[cite: 9].
3. Run the script via your terminal:
```bash
   python script_name.py
   ```
4. The terminal will output its progress[cite: 9]. Depending on the size of the CSV, the DNS lookups may take a while[cite: 9].
5. Once finished, check the directory for the newly created `output_with_spf.csv` file[cite: 9].