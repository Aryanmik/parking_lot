class TicketsDB:
    tickets = {}

    def save(self, ticket):
        self.tickets[ticket.ticket_id] = ticket

    def get(self, ticket_id):
        ticket = self.tickets.get(ticket_id)
        if not ticket:
            raise Exception(f"Invalid ticket id: {ticket_id}")
        return ticket