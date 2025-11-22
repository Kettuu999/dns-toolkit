import sys
import argparse
import dns.resolver

# Fetches DNS records of a specified type for a given domain using optional custom resolvers.
def get_records(domain, record_type, resolver_list=None):
    resolver = dns.resolver.Resolver()
    if resolver_list:
        resolver.nameservers = resolver_list
    try:
        answers = resolver.resolve(domain, record_type)
        if record_type.upper() == 'NS':
            return sorted([str(rdata.target).rstrip('.') for rdata in answers])
        else:
            return [rdata.to.text() for rdata in answers]
    except Exception as e:
        print(f"Error fetching {record_type} records: {e}")
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

# Evaluates redundancy based on the number of nameservers.
def redundancy_score(nameservers):
    if len(nameservers) >= 4:
        return "Excellent"
    elif len(nameservers) == 2:
        return "Good"
    elif len(nameservers) == 1:
        return "Poor"
    else:
        return "Unknown"
    
# Main function to parse arguments and execute the scanning logic 
def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="DNS Toolkit Scanner v0.2")
    parser.add_argument("-d", "--domain", required=True, help="Target domain to scan")
    parser.add_argument("--resolver", nargs="+", help="Custom DNS resolver IPs")
    parser.add_argument("-t", "--type", default="NS", help="DNS record type to query (default: NS)")
    args = parser.parse_args()
    
    # Extract arguments
    domain = args.domain
    record_type = args.type.upper()
    resolver_list = args.resolver
    
    # Display header and scan results
    print(f"\n=== DNS Toolkit Scanner v0.2 ===")
    print(f"Scanning domain: {domain}\n")
    if resolver_list:
        print(f"Using custom resolvers: {', '.join(resolver_list)}\n")
    print()
    
    records = get_records(domain, record_type, resolver_list)
    
    print(f"{record_type} Records:")
    if records: 
        for r in records:
            print(f" - {r}")
    else:
        print(" No records found.")
        
    if record_type == "NS":
        provider = detect_provider(records)
        score = redundancy_score(records)
        
        print(f"\nDetected Provider: {provider}")
        print(f"Redundancy Score: {score}\n")
        
    print() 


# Main execution block. 
if __name__ == "__main__":
    main()
    
    

        