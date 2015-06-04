##: Pseudocode
##: Developing an algorithm

##: They are really useful
##: They are really clever
##: They make the world faster

##: They are problems that solve problems

def algorithm_development(problem_specs):
    correct = False
    while not correct or not fast_enough(running_time):
        algorithm = devise_algorithm(problem_specs)
        correct = analyze_correctness(algorithm)
        running_time = analyze_efficiency(algorithm)
    return algorithm

