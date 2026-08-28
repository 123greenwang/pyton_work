def print_models(unprint_design, completed):

    while unprint_design:
        current_design=unprint_design.pop()
        print(f"Printing model:{current_design}")
        completed.append(current_design)

def show_completed_models(completed):
    print("\nThe following models have been printed:")
    for completed_model in completed:
        print(completed_model)
unprint_design=["phone case",'robot pendat','dodecahedron']
completed=[]
print_models(unprint_design[:], completed)
show_completed_models(completed)