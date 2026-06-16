"""
package_demo.py
---------------
Demonstrates how to use a third-party package called 'colorama'.
colorama lets us print colored text in the terminal.

To install it, run:
    pip install colorama
"""

# Import colorama tools
from colorama import init, Fore, Style

if __name__ == "__main__":
    # init() makes colorama work correctly on all platforms (including Windows)
    init(autoreset=True)

    # --- Print colored messages ---

    # Green text for a success message
    print(Fore.GREEN + "Success! colorama is working perfectly.")

    # Yellow text for a warning
    print(Fore.YELLOW + "Warning: This is just a demo message.")

    # Red text for an error example
    print(Fore.RED + "Error: Something went wrong (just for demo).")

    # Cyan text for info
    print(Fore.CYAN + "Info: colorama makes terminal output colorful and fun!")

    # Bold white text using Style
    print(Style.BRIGHT + Fore.WHITE + "Bold White: Python third-party packages are easy to use!")
