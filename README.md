# DNS Toolkit (v0.2)

A lightweight open-source DNS scanner written in Python. 

DNS Toolkit helps you:
- Retrieve any DNS record type (NS, A, MX, TXT, AAAA, etc.)
- Detect the DNS provider based on nameserver patterns
- Score DNS redundancy for NS setups
- Use custom DNS resolvers (e.g., **1.1.1.1, 8.8.8.8**)

# Features Added in V0.2
- CLI support using **argparse**
- -d/--domain - target domain
- -t/--type - DNS record type 
- --resolver - custom resolver IPs 
- Unified get_records() function for all record types.

# Installation:
- **Requires dnspython:** pip install dnspython
- **Clone the repo:** git clone https://github.com/Kettuu999/dns-toolkit.git -> cd dns-toolkit

## Usage:
**Basic Scan (NS records):**
python3 scanner.py -d example.com

**Query a specific DNS record type:**
python3 scanner.py -d example.com -t A

**Use custom resolvers:**
python3 scanner.py -d example.com -t MX --resolver 1.1.1.1 8.8.8.8


## Example Output:

=== DNS Toolkit Scanner v0.2 ===
Scanning domain: cloudflare.com

Using custom resolvers: 1.1.1.1, 8.8.8.8

NS Records:
 - ns3.cloudflare.com
 - ns4.cloudflare.com
 - ns5.cloudflare.com

Detected Provider: Cloudflare
Redundancy Score: Excellent
