import sys
import dns.resolver

# Feteches NS (nameserver) records.
def get_nameservers(domain):
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        return sorted([str(rdata.target).rstrip('.') for rdata in answers])
    except Exception as e:
        print(f"Error detching NS records: {e}")
        return []
    
# Attempts to detect the DNS provider being used. 
def detect_provider(nameservers):
    # Common DNS providers
    providers = {
        'Cloudflare': ['cloudflare', 'ns.cloudflare.com'],
        'Google': ['google', 'ns1.google.com'],
        'Amazon Route 53': ['awsdns', 'route53'],
        'GoDaddy': ['godaddy', 'domaincontrol.com'],
        'Bluehost': ['bluehost', 'ns1.bluehost.com'],
    }

    # Loops through every proivder to see if any keywords match. 
    for provider, keywords in providers.items():
        for ns in nameservers:
            if any(keyword in ns.lower() for keyword in keywords):
                return provider.capitalize()
            
    return 'Unknown'

# Rates DNS redundacy based on number of nameservers.
def reducnacy_score(nameservers):
    if len(nameservers) >= 4:
        return "Excellent"
    elif len(nameservers) == 2:
        return "Good"
    elif len(nameservers) == 1:
        return "Poor"
    else:
        return "Unknown"
    
# Main execution block. 
if __name__ == "__main__":
    # Ensures user enters domain name as argument.
    if len(sys.argv) != 2:
        print("Usage: python3 scanner.py <domain>")
        sys.exit(1)
    
    domain = sys.argv[1]
    
    print(f"\n=== DNS Toolkit Scanner v0.1 ===")
    print(f"Scanning domain: {domain}\n")


    # Grabs NS records.
    ns_records = get_nameservers(domain)
    
    print("Nameservers:")
    if ns_records:
        for ns in ns_records:
            print(f" - {ns}")
    else:
        print(" No nameservers found.")
        
    # Detects provider and rates redundancy.
    provider = detect_provider(ns_records)
    score = reducnacy_score(ns_records)
    
    print(f"\nDetected Provider: {provider}")
    print(f"Redundancy Score: {score}\n")
    
    

        