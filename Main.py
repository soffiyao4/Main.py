from tickets_module import generate_tickets

num = int(input("Enter how many tickets you want: "))

tickets = generate_tickets(num)

print("\nGenerated Tickets:")
for t in tickets:
    print(t)

print(f"\nTotal tickets generated: {len(tickets)}")