import socket

def get_ip_address(domain):
    try:
        # Use socket.gethostbyname() to retrieve the IP address of the domain
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.error as e:
        # Handle any potential errors, such as an invalid domain
        return f"Error: {e}"

# Example usage:
website_domain = "www.google.com"

# Call the get_ip_address function to get the IP address of the specified website
ip_address = get_ip_address(website_domain)

# Print the result
print(f"The IP address of {website_domain} is: {ip_address}") # see yall