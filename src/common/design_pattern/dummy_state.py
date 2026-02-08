from abc import ABC, abstractmethod

"""The ticket can be in one of the following states: New, Assigned, Resolved, and Closed. Each state has its own behaviour, and the ticket can transition between states based on certain conditions."""


# Step 1: Define the abstract base class TicketState
class TicketState(ABC):

    @abstractmethod
    def assign(self, ticket):
        pass

    @abstractmethod
    def resolve(self, ticket):
        pass

    @abstractmethod
    def close(self, ticket):
        pass


# Step 2: Implement the concrete state classes
class NewState(TicketState):

    def assign(self, ticket):
        # Implement the behavior for assigning a new ticket
        ticket.state = AssignedState()

    def resolve(self, ticket):
        # Implement the behavior for resolving a new ticket
        ticket.state = ResolvedState()

    def close(self, ticket):
        # Implement the behavior for closing a new ticket
        ticket.state = ClosedState()


# Implement the other concrete state classes: AssignedState, ResolvedState, and ClosedState
class AssignedState(TicketState):

    def assign(self, ticket):
        # Implement the behavior for assigning a new ticket
        raise Exception("Transition error, ticket already assigned")

    def resolve(self, ticket):
        # Implement the behavior for resolving a new ticket
        ticket.state = ResolvedState()

    def close(self, ticket):
        # Implement the behavior for closing a new ticket
        ticket.state = ClosedState()


class ResolvedState(TicketState):

    def assign(self, ticket):
        # Implement the behavior for assigning a new ticket
        raise Exception("Transition error, ticket already resolved")

    def resolve(self, ticket):
        # Implement the behavior for resolving a new ticket
        raise Exception("Transition error, ticket already resolved")

    def close(self, ticket):
        # Implement the behavior for closing a new ticket
        ticket.state = ClosedState()


class ClosedState(TicketState):

    def assign(self, ticket):
        # Implement the behavior for assigning a new ticket
        raise Exception("Transition error, ticket already closed")

    def resolve(self, ticket):
        # Implement the behavior for resolving a new ticket
        raise Exception("Transition error, ticket already closed")

    def close(self, ticket):
        # Implement the behavior for closing a new ticket
        raise Exception("Transition error, ticket already closed")


# Step 3: Implement the Ticket class
class Ticket:

    def __init__(self):
        # Initialize the ticket's state attribute with an instance of the NewState class
        self.state = NewState()

    def assign(self):
        # Delegate the assign method call to the current state object
        self.state.assign(self)

    def resolve(self):
        # Delegate the resolve method call to the current state object
        self.state.resolve(self)

    def close(self):
        # Delegate the close method call to the current state object
        self.state.close(self)


# Step 4: Test the behavior of the ticket and its state transitions
def main():
    ticket = Ticket()

    # Test the initial state and transitions
    ticket.assign()
    ticket.resolve()
    ticket.close()

    # Test invalid transitions
    ticket.assign()
    ticket.resolve()


if __name__ == "__main__":
    main()
