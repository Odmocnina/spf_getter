import pandas as pd
import dns.resolver
from urllib.parse import urlparse


"""
This function get stf of a domain from a given URL

param url: str: URL of the domain
return: str: SPF record or error message
"""
def get_domain_spf(url):
    
    # clear url input
    domain = str(url).strip()
    
    # if domain does not start with http or https, add http
    if not domain.startswith(('http://', 'https://')):
        domain = 'http://' + domain
        
    try:
        parsed_uri = urlparse(domain)
        domain_name = parsed_uri.netloc
    except Exception:
        return "Invalid URL format"

    # 2. DNS dotaz na TXT záznamy
    try:
        answers = dns.resolver.resolve(domain_name, 'TXT')
        spf_records = []
        
        for rdata in answers:
            # Záznamy jsou v bytech nebo stringu, převedeme na text a zbavíme se uvozovek
            txt_record = rdata.to_text().strip('"')
            
            # Hledáme ten, co začíná 'v=spf1'
            if txt_record.startswith('v=spf1'):
                spf_records.append(txt_record)
        
        if spf_records:
            return "; ".join(spf_records) # Občas jich může být víc (i když by nemělo)
        else:
            return "No SPF record found"

    except dns.resolver.NXDOMAIN:
        return "Domain not found"
    except dns.resolver.NoAnswer:
        return "No TXT records"
    except dns.resolver.Timeout:
        return "DNS Timeout"
    except Exception as e:
        return f"Error: {str(e)}"

# main function of the script
def main():
    # load input CSV
    INPUT_FILE = 'domains.csv'  # input CSV file
    OUTPUT_FILE = 'output_with_spf.csv'  # output csv file
    URL_COLUMN = 'url'  # name of the column with URLs
    SPF_COLUMN = 'spf_record'  # name of the new column for SPF records

    csv_separator = ';'  # define the separator used in the CSV file

    print(f"Loading {INPUT_FILE}...")
    
    try:
        # load CSV file into DataFrame
        df = pd.read_csv(INPUT_FILE, sep=csv_separator)

        # Remove unnamed columns if any
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        
        # Check if the column exists
        if URL_COLUMN not in df.columns:
            print(f"Error: Column '{URL_COLUMN}' does not exist in the table!")
            return

        print("Getting SPF records (this may take a while)...")
        
        # Apply the function to each row (creates a new column 'spf_record')
        # We use .apply(), which goes through row by row
        df[SPF_COLUMN] = df[URL_COLUMN].apply(get_domain_spf) # apply the function to each URL, this is for each
        
        # Save to a new file
        df.to_csv(OUTPUT_FILE, index=False, sep=csv_separator)
        print(f"Done! Saved to {OUTPUT_FILE}")

    except FileNotFoundError:
        print("Error: Input file not found.")

if __name__ == "__main__":
    main()