# DNS Toolkit (v0.1)

A simple open-source DNS scanner that checks:
- Nameserver (NS) records
- Attempts to detect DNS provider host the domain
- Scores the DNS redundancy (1 NS, 2 NS, 4 NS, etc.) 

## Usage:
python3 scanner.py example.com

## Example Output:

=== DNS Toolkit Scanner v0.1 ===
Scanning domain: cloudflare.com

Nameservers:
- ns1.cloudflare.com
- ns2.cloudflare.com

Detected Provider: Cloudflare

Redundancy Score: Good
