from datetime import datetime


class TicketManager:

    def __init__(self):
        self.tickets = []

    def create_ticket(
        self,
        customer_query,
        reason,
        confidence,
        category="General",
        priority="Medium"
    ):

        ticket_number = len(self.tickets) + 1

        ticket_id = (
            f"CS-{datetime.now().strftime('%Y%m%d')}-"
            f"{ticket_number:03d}"
        )

        ticket = {
            "ticket_id": ticket_id,
            "customer_query": customer_query,
            "reason": reason,
            "confidence": confidence,
            "category": category,
            "priority": priority,
            "status": "OPEN",
            "created_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

        self.tickets.append(ticket)

        return ticket

    def get_tickets(self):
        return self.tickets