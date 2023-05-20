from collections import defaultdict


class Cost:
    VALID_COST_TYPES = {"running": "yearly cost in €",
                        "purchase": "fixed, occur only once, in €",
                        "restoration": "fixed and / or running cost, €",
                        "taxes": "yearly taxes in €"}

    def __init__(self):
        self.costs = {}

    def add_cost(self, cost_type, amount):
        if cost_type not in self.VALID_COST_TYPES:
            raise ValueError(f"{cost_type} is not a valid cost type")
        if cost_type not in self.costs:
            self.costs[cost_type] = amount
        else:
            self.costs[cost_type] += amount

    def remove_cost(self, cost_type):
        if cost_type in self.costs:
            del self.costs[cost_type]

    def modify_cost(self, cost_type, new_amount):
        if cost_type in self.costs:
            self.costs[cost_type] = new_amount

    def sum_costs(self, node):
        """
        Perform a depth-first search on the given node and its descendants,
        summing up all costs according to their categories.

        Parameters:
        node (CortijoObject): The node to start the search from.

        Returns:
        dict: A dictionary with the total cost for each category.
        """

        # Use a dictionary with default value 0 for summing costs
        total_costs = defaultdict(int)

        # Start the depth-first search with the given node
        nodes_to_visit = [node]

        while nodes_to_visit:
            current_node = nodes_to_visit.pop()
            if hasattr(current_node, 'cost'):
                for cost_type, cost_value in current_node.cost._cost.items():
                    total_costs[cost_type] += cost_value

            # Add all children to the list of nodes to visit
            for children in current_node._children.values():
                nodes_to_visit.extend(children)

        return dict(total_costs)


class Loan:
    def __init__(self, principal, interest_rate, term_years):
        """
        Initialize a Loan instance.

        Parameters
        ----------
        principal : float
            The principal amount of the loan (in €).

        interest_rate : float
            The annual interest rate of the loan (as a decimal; e.g., 0.05 represents a 5% interest rate).

        term_years : int
            The term of the loan in years.
        """
        self.principal = principal
        self.interest_rate = interest_rate
        self.term_years = term_years

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment for the loan.

        Returns
        -------
        float
            The monthly payment amount (in €).
        """
        # The number of monthly payments over the term
        num_payments = self.term_years * 12
        # The monthly interest rate
        monthly_rate = self.interest_rate / 12

        # Use the formula for calculating the monthly payment on an amortizing loan
        monthly_payment = (self.principal * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)
        return monthly_payment
