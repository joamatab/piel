# # Run OpenLane Flow

import piel

# Assume we are starting from the iic-osic-home design directory, all our design files are there in the format as described in the piel sections/project_structure documentation.

# ## Define working directory

piel.run_openlane_flow(
    design_directory="/foss/designs/spm",
)
