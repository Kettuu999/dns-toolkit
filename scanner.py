import sys
import dns.resolver

def get_nameservers(domain):
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        return sorted([str(rdata.target).rstrip('.') for rdata in answers])
    except Exception as e:
        print(f"Error detching NS records: {e}")
        return []

def detect_provider(nameservers):
    providers = {
        'Cloudflare': ['cloudflare', 'ns.cloudflare.com'],
        'Google': ['google', 'ns1.google.com'],
        'Amazon Route 53': ['awsdns', 'route53'],
        'GoDaddy': ['godaddy', 'domaincontrol.com'],
        'Bluehost': ['bluehost', 'ns1.bluehost.com'],
    }

    for provider, keywords in providers.items():
        for ns in nameservers:
            if any(keyword in ns.lower() for keyword in keywords):
                return provider.capitalize()
    return 'Unknown'


def reducnacy_score(nameservers):
    if len(nameservers) >= 4:
        return "Excellent"
    elif len(nameservers) == 2:
        return "Good"
    elif len(nameservers) == 1:
        return "Poor"
    else:
        return "Unknown"
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scanner.py <domain>")
        sys.exit(1)
    
    domain = sys.argv[1]
    print(f"\n=== DNS Toolkit Scanner v0.1 ===")
    print(f"Scanning domain: {domain}\n")
    
    ns_records = get_nameservers(domain)
    
    print("Nameservers:")
    if ns_records:
        for ns in ns_records:
            print(f" - {ns}")
    else:
        print(" No nameservers found.")
        
    provider = detect_provider(ns_records)
    score = reducnacy_score(ns_records)
    
    print(f"\nDetected Provider: {provider}")
    print(f"Redundancy Score: {score}\n")
    
    

        