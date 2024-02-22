import cplex
from cplex.exceptions import CplexError

# define our defenders utilities
def_utl = [
    [5, -4, -2, -7, -5],
    [-3, 7, -2, -7, -5],
    [-3, -4, 3, -7, -5],
    [-3, -4, -2, 6, -5],
    [-3, -4, -2, -7, 4]
]


def main():
    # create our cplex problem
    try:
        # Create a CPLEX problem
        maximin_prob = cplex.Cplex()

        # Define variables
        def_strat = [maximin_prob.variables.type.continuous] * 5

        maximin_prob.variables.add(names=["d1", "d2", "d3", "d4", "d5"], types=def_strat)

        # find the worst case scenario for each row
        utl_maximin = [min(def_utl[i]) for i in range(5)]
        maximin_prob.objective.set_linear(enumerate(utl_maximin))

        # find the best case scenario from our worst cases
        maximin_prob.objective.set_sense(maximin_prob.objective.sense.maximize)

        # Defender constraints; limit the defender to 1 pick
        maximin_prob.linear_constraints.add(
            lin_expr=[cplex.SparsePair(ind=["d1", "d2", "d3", "d4", "d5"], val=[1.0] * 5)],
            senses=["E"],
            rhs=[1.0]
        )

        maximin_prob.solve()
    except CplexError:
        raise

    # Display the results
    # the cplex problem will give us the utility as the objective value
    # using the get_values() function, we will get a binary array where indices equal to 1 are valid maximin strategies
    print("Maximin Utility:", maximin_prob.solution.get_objective_value())
    maximin_strats = maximin_prob.solution.get_values()
    for i in range(5):
        if maximin_strats[i] == 1.0:
            print("The strategy of defending target", i + 1, "is a Maximin Strategy for the defender\n")

    maximin_prob.write("Maximin.lp")


if __name__ == '__main__':
    main()
