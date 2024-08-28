#Natalia Raz

import nuke

def copy_to_to_from_and_remove_animation_for_selected():
    # Get the list of selected CornerPin2D nodes
    selected_nodes = nuke.selectedNodes('CornerPin2D')
    
    # Check if there are any selected CornerPin2D nodes
    if not selected_nodes:
        nuke.message("Please select at least one CornerPin2D node.")
        return
    
    for node in selected_nodes:
        # Clear any existing animation from the "from" parameters
        for i in range(1, 5):
            node['from{}'.format(i)].clearAnimated()
            # Set the values from "to" to "from"
            node['from{}'.format(i)].setValue(node['to{}'.format(i)].value())

# Execute the script
copy_to_to_from_and_remove_animation_for_selected()
