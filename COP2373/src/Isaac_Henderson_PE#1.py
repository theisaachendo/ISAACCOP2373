def get_ticket_purchase():
    while True:
        try:
            tickets_wanted = int(input(
                "Enter the number of tickets you wish to purchase (1-4): "))
            if 1 <= tickets_wanted <= 4:
                return tickets_wanted
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")


def process_ticket_sale():
    remaining_tickets = 10
    customer_count = 0

    print("Welcome to the Cinema Ticket Pre-Sale!")
    print(f"Total tickets available: {remaining_tickets}")
    print("Each buyer can purchase up to 4 tickets.")
    print("-" * 40)

    while remaining_tickets > 0:
        print(f"\nTickets remaining: {remaining_tickets}")

        tickets_wanted = get_ticket_purchase()

        if tickets_wanted <= remaining_tickets:
            remaining_tickets -= tickets_wanted
            customer_count += 1

            print(f"Purchase successful! You bought "
                  f"{tickets_wanted} ticket(s).")
            print(f"Tickets remaining: {remaining_tickets}")
        else:
            print(f"Sorry, only {remaining_tickets} tickets are available.")
            print("Please try again with a smaller number.")

    print("All tickets have been sold!")
    print(f"Total number of buyers: {customer_count}")
    print("Thank you for your business!")


if __name__ == "__main__":
    process_ticket_sale()
