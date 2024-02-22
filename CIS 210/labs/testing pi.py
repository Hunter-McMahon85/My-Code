import p3mc
monte_carlo = 2
err_tol = .01
monte_margin = True
while monte_margin == True:
    monte_est = p3mc.pi_mc(monte_carlo)
    monte_percent_error = 1 - monte_est / pi
    if monte_percent_error <= err_tol:
        monte_margin = False
    else:
        monte_carlo += 1
