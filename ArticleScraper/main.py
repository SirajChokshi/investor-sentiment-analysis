from scraper import scrape
from ansi import colors
import sys

# CLI to interact with scrape.py functions
def main():
    if (len(sys.argv) == 2):
        if (sys.argv[1] == '--help'):
            print(f"""
{colors.HEADER}Article Scraper Help{colors.RESET}
Pass a stock ticker (e.g. MSFT, DOW, AMZN, etc) as the first and only argument
and view a list of recent and relevant articles from Yahoo Finance.

$ {colors.GREEN}python{colors.RESET} main.py {colors.BLUE}<TICKER>{colors.RESET}""")
        else:
            scrape.scrapeArticles(sys.argv[1], True)
    else:
        if len(sys.argv) > 2:
            print(colors.RED + "\nERROR: Too many arguments!" + colors.RESET + "\nFor Help: $ " + colors.GREEN + "python" + colors.RESET + " main.py " + colors.BLUE + "--help" + colors.RESET)
        else:
            print(colors.RED + "\nERROR: Too few arguments!" + colors.RESET + "\nFor Help: $ " + colors.GREEN + "python" + colors.RESET + " main.py " + colors.BLUE + "--help" + colors.RESET)
main()