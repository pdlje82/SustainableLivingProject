from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np


class Cost:
    VALID_COST_CATEGORIES = {"running": "yearly cost in €",
                             "purchase": "fixed, occur only once, in €",
                             "restoration": "fixed and / or running cost, €",
                             "taxes": "yearly taxes in €"}

    VALID_COST_TYPES = ['fixed', 'running']

    def __init__(self):
        self.costs = {}

    def add_cost(self, cost_type, cost_category, amount):
        if cost_type not in self.VALID_COST_TYPES:
            raise ValueError(f"{cost_type} is not a valid cost type")
        if cost_category not in self.VALID_COST_CATEGORIES:
            raise ValueError(f"{cost_category} is not a valid cost category")
        if cost_type not in self.costs:
            self.costs[cost_type] = {cost_category: amount}
        else:
            if cost_category in self.costs[cost_type]:
                self.costs[cost_type][cost_category] += amount
            else:
                self.costs[cost_type][cost_category] = amount

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
        dict: A dictionary with the total fixed and running costs for each category and node.
        """

        # Use a dictionary with default value of an empty dictionary for summing costs
        fixed_total_costs = defaultdict(lambda: defaultdict(int))
        running_total_costs = defaultdict(lambda: defaultdict(int))

        # Start the depth-first search with the given node
        nodes_to_visit = [node]

        while nodes_to_visit:
            current_node = nodes_to_visit.pop()
            if hasattr(current_node, '_cost'):
                for cost_type, cost_categories in current_node._cost.costs.items():
                    for cost_category, cost_value in cost_categories.items():
                        if cost_type == 'fixed':
                            fixed_total_costs[cost_category][current_node.name] += cost_value
                        elif cost_type == 'running':
                            running_total_costs[cost_category][current_node.name] += cost_value

            # Add all children to the list of nodes to visit
            for children in current_node._children.values():
                nodes_to_visit.extend(children)

        # Convert the nested defaultdicts to regular dictionaries
        fixed_total_costs = {k: dict(v) for k, v in fixed_total_costs.items()}
        running_total_costs = {k: dict(v) for k, v in running_total_costs.items()}

        return fixed_total_costs, running_total_costs

    def plot_costs(self, total_costs):
        """
        Plot a stacked bar chart of the total costs.

        Parameters:
        total_costs (dict): A dictionary with the total cost for each category and node.
        """

        cost_types = list(total_costs.keys())
        node_names = sorted(set(name for costs in total_costs.values() for name in costs.keys()))
        num_nodes = len(node_names)

        data = np.zeros((num_nodes, len(cost_types)))

        # Map node names to index
        node_index = {node: i for i, node in enumerate(node_names)}

        # Populate data matrix
        for j, costs in enumerate(total_costs.values()):
            for node, cost in costs.items():
                i = node_index[node]
                data[i, j] = cost

        fig, ax = plt.subplots()

        colors = plt.cm.viridis(np.linspace(0, 1, num_nodes))

        # Draw bars, one category at a time
        for i in range(num_nodes):
            ax.bar(cost_types, data[i], bottom=np.sum(data[:i], axis=0), color=colors[i])

        # Compute and plot the total cost across all categories
        total_cost_across_all_categories = np.sum(data)
        ax.bar('Total Costs', total_cost_across_all_categories, color='red')

        ax.set_ylabel('Total Cost')
        ax.set_title('Total Costs by Category and Node')
        ax.legend(node_names, title="Nodes")
        plt.show()


class Loan:
    def __init__(self, principal, down_payment, interest_rate, term_years):
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
        self.down_payment = down_payment
        self.interest_rate = interest_rate
        self.term_years = term_years

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment for the loan.

        Returns
        -------
        dict
            A dictionary with input parameters and the monthly payment amount (in €).
        """
        # The number of monthly payments over the term
        num_payments = self.term_years * 12
        # The monthly interest rate
        monthly_rate = self.interest_rate / 12
        # The loan amount after the down payment
        loan_amount = self.principal - self.down_payment

        # Use the formula for calculating the monthly payment on an amortizing loan
        monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)

        # Total amount repaid over the loan's term
        total_repaid = monthly_payment * num_payments

        # Total interest paid is the total amount repaid minus the principal
        total_interest_paid = total_repaid - loan_amount

        # Create a dictionary to store input parameters and the calculated values
        result = {
            'principal': round(self.principal, 2),
            'down_payment': round(self.down_payment, 2),
            'loan_amount_after_down_payment': round(loan_amount, 2),
            'interest_rate': round(self.interest_rate, 3),
            'term_years': self.term_years,
            'monthly_payment': round(monthly_payment, 2),
            'total_repaid': round(total_repaid, 2),
            'total_interest_paid': round(total_interest_paid, 2),
        }
        # create a bar chart
        plt.figure(figsize=(10, 6))  # set figure size
        plt.bar(list(result.keys()), list(result.values()), color='blue')
        plt.ylabel('Amount (€)')
        plt.title('Loan Summary')
        for index, value in enumerate(result.values()):
            plt.text(index, value, str(value), ha='center', va='bottom')  # add text on bars
        plt.xticks(rotation=45)  # rotate x-axis labels for better readability
        plt.tight_layout()  # adjust layout to prevent overlapping labels
        plt.show()

        return result

        return result