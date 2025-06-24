# Hardcoded stock prices (in USD)
stock_prices = {
    "AAPL": 180.25,
    "TSLA": 250.75,
    "MSFT": 300.50,
    "AMZN": 120.30,
    "GOOGL": 140.65,
    "META": 350.20,
    "NVDA": 450.90,
    "NFLX": 500.40
}

def display_welcome():
    print("\n" + "="*60)
    print(" STOCK PORTFOLIO TRACKER ".center(60, '#'))
    print("="*60)
    print("\nWelcome to your personal stock portfolio manager!")
    print("This tool helps you track your investments and calculate")
    print("your total portfolio value based on current stock prices.\n")
    input("Press Enter to continue...")

def display_menu():
    print("\n" + "="*60)
    print(" MAIN MENU ".center(60, '#'))
    print("="*60)
    print("\n1. Tutorial: How to use this tracker")
    print("2. View available stocks and prices")
    print("3. Calculate my portfolio value")
    print("4. Save my portfolio to file")
    print("5. Add custom stock price (admin)")
    print("6. Exit program")
    print("\n" + "-"*60)

def show_tutorial():
    print("\n" + "="*60)
    print(" TUTORIAL ".center(60, '#'))
    print("="*60)
    print("\nThis program helps you track your stock investments:")
    print("\n1. First, view available stocks (Option 2)")
    print("2. Then calculate your portfolio (Option 3)")
    print("   - Enter each stock symbol you own")
    print("   - Enter the quantity of shares")
    print("   - Type 'done' when finished")
    print("3. You can save your results (Option 4)")
    print("\nTips:")
    print("- Type 'menu' anytime to return to main menu")
    print("- Type 'list' during entry to see available stocks")
    print("- Stock symbols are not case sensitive (AAPL = aapl)")
    print("\n" + "-"*60)
    input("\nPress Enter to return to menu...")

def view_stocks():
    print("\n" + "="*60)
    print(" AVAILABLE STOCKS ".center(60, '#'))
    print("="*60)
    print("\n{:<10} {:<15} {:<30}".format("Symbol", "Price ($)", "Company"))
    print("-"*60)
    stocks_info = {
        "AAPL": "Apple Inc.",
        "TSLA": "Tesla Inc.",
        "MSFT": "Microsoft Corporation",
        "AMZN": "Amazon.com Inc.",
        "GOOGL": "Alphabet Inc.",
        "META": "Meta Platforms Inc.",
        "NVDA": "NVIDIA Corporation",
        "NFLX": "Netflix Inc."
    }
    for stock, price in stock_prices.items():
        company = stocks_info.get(stock, "Unknown Company")
        print("{:<10} ${:<14.2f} {:<30}".format(stock, price, company))
    print("\nNote: Prices are for demonstration purposes only")
    print("-"*60)
    input("\nPress Enter to return to menu...")

def calculate_portfolio():
    print("\n" + "="*60)
    print(" PORTFOLIO CALCULATOR ".center(60, '#'))
    print("="*60)
    print("\nEnter each stock you own and the quantity of shares.")
    print("Type 'done' when finished or 'menu' to cancel.\n")
    
    portfolio = {}
    while True:
        stock = input("Enter stock symbol (or 'list' to see options): ").strip().upper()
        
        if stock == 'DONE':
            break
        if stock == 'MENU':
            return None
        if stock == 'LIST':
            view_stocks()
            continue
        if stock not in stock_prices:
            print(f"'{stock}' not found. Type 'list' to see available stocks.")
            continue
        
        try:
            quantity = float(input(f"Enter quantity of {stock} shares: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                continue
            portfolio[stock] = quantity
        except ValueError:
            print("Please enter a valid number (e.g., 5 or 3.5 for fractional shares).")
    
    if not portfolio:
        print("No stocks entered. Returning to menu.")
        return None
    
    # Calculate and display results
    total = 0
    print("\n" + "="*60)
    print(" PORTFOLIO SUMMARY ".center(60, '#'))
    print("="*60)
    print("\n{:<10} {:<15} {:<15} {:<15}".format("Stock", "Price", "Shares", "Value"))
    print("-"*60)
    
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = quantity * price
        total += value
        print("{:<10} ${:<14.2f} {:<14.2f} ${:<14.2f}".format(stock, price, quantity, value))
    
    print("-"*60)
    print("TOTAL PORTFOLIO VALUE:".ljust(45) + "${:.2f}".format(total))
    print("="*60 + "\n")
    
    return portfolio

def save_portfolio(portfolio):
    if not portfolio:
        print("\nNo portfolio data to save. Please calculate a portfolio first.")
        input("Press Enter to continue...")
        return
    
    print("\n" + "="*60)
    print(" SAVE PORTFOLIO ".center(60, '#'))
    print("="*60)
    print("\nChoose file format:")
    print("1. Text file (.txt) - Human readable format")
    print("2. CSV file (.csv) - For spreadsheet import")
    print("3. Return to main menu")
    
    while True:
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '3':
            return
        if choice not in ('1', '2'):
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        filename = input("Enter filename (without extension): ").strip()
        if not filename:
            print("Filename cannot be empty.")
            continue
        
        try:
            if choice == '1':
                filename += ".txt"
                with open(filename, 'w') as f:
                    f.write("="*60 + "\n")
                    f.write(" PORTFOLIO SUMMARY ".center(60, '#') + "\n")
                    f.write("="*60 + "\n\n")
                    f.write("{:<10} {:<15} {:<15} {:<15}\n".format("Stock", "Price", "Shares", "Value"))
                    f.write("-"*60 + "\n")
                    for stock, quantity in portfolio.items():
                        price = stock_prices[stock]
                        value = quantity * price
                        f.write("{:<10} ${:<14.2f} {:<14.2f} ${:<14.2f}\n".format(stock, price, quantity, value))
                    f.write("-"*60 + "\n")
                    total = sum(quantity * stock_prices[stock] for stock, quantity in portfolio.items())
                    f.write("TOTAL PORTFOLIO VALUE:".ljust(45) + "${:.2f}\n".format(total))
                    f.write("="*60 + "\n")
                    f.write(f"\nSaved on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                print(f"\nPortfolio successfully saved to {filename}")
            
            elif choice == '2':
                filename += ".csv"
                with open(filename, 'w') as f:
                    f.write("Stock,Price,Shares,Value\n")
                    for stock, quantity in portfolio.items():
                        price = stock_prices[stock]
                        value = quantity * price
                        f.write(f"{stock},{price:.2f},{quantity:.2f},{value:.2f}\n")
                    total = sum(quantity * stock_prices[stock] for stock, quantity in portfolio.items())
                    f.write(f"Total,,,{total:.2f}\n")
                    f.write(f"Date,{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                print(f"\nPortfolio successfully saved to {filename}")
            
            input("\nPress Enter to continue...")
            return
            
        except Exception as e:
            print(f"\nError saving file: {e}")
            input("Press Enter to try again...")

def add_custom_stock():
    print("\n" + "="*60)
    print(" ADD CUSTOM STOCK ".center(60, '#'))
    print("="*60)
    print("\nWarning: This will add a temporary stock that disappears when")
    print("the program closes. For permanent additions, edit the code.\n")
    
    symbol = input("Enter stock symbol (e.g., IBM): ").strip().upper()
    if not symbol:
        print("Symbol cannot be empty.")
        return
    
    if symbol in stock_prices:
        print(f"{symbol} already exists in the database.")
        return
    
    try:
        price = float(input(f"Enter current price for {symbol}: $"))
        if price <= 0:
            print("Price must be positive.")
            return
        
        company = input(f"Enter company name for {symbol}: ").strip()
        stock_prices[symbol] = price
        print(f"\nSuccessfully added {symbol} ({company}) at ${price:.2f}")
    except ValueError:
        print("Invalid price. Please enter a number (e.g., 150.25).")
    
    input("\nPress Enter to continue...")

def main():
    import datetime
    current_portfolio = None
    
    display_welcome()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            show_tutorial()
        elif choice == '2':
            view_stocks()
        elif choice == '3':
            current_portfolio = calculate_portfolio()
        elif choice == '4':
            save_portfolio(current_portfolio)
        elif choice == '5':
            add_custom_stock()
        elif choice == '6':
            print("\n" + "="*60)
            print(" Thank you for using Stock Portfolio Tracker! ".center(60, '#'))
            print("="*60 + "\n")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
