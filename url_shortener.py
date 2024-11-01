import random
import string

class URLShortener:
    def __init__(self):
        # Dictionary to store our URL mappings
        self.url_mapping = {}
        
    def generate_short_code(self, length=6):
        """Generate a random short code of specified length"""
        # string.ascii_letters contains all ASCII letters (both lowercase and uppercase)
        # string.digits contains 0-9
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
    
    def shorten_url(self, long_url):
        """Create a short URL and store the mapping"""
        # Generate a unique short code
        while True:
            short_code = self.generate_short_code()
            if short_code not in self.url_mapping:
                break
        
        # Store the mapping
        self.url_mapping[short_code] = long_url
        return short_code
    
    def get_long_url(self, short_code):
        """Retrieve the original URL"""
        return self.url_mapping.get(short_code)

# Example usage
def main():
    shortener = URLShortener()
    
    while True:
        print("\nURL Shortener Menu:")
        print("1. Shorten URL")
        print("2. Get original URL")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            long_url = input("Enter the URL to shorten: ")
            short_code = shortener.shorten_url(long_url)
            print(f"Shortened URL code: {short_code}")
            
        elif choice == "2":
            short_code = input("Enter the short code: ")
            long_url = shortener.get_long_url(short_code)
            if long_url:
                print(f"Original URL: {long_url}")
            else:
                print("Short code not found!")
                
        elif choice == "3":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()