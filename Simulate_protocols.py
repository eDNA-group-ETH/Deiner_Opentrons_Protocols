
# to simulate the protocols on the command line create a conda environemnt 
# to install teh opentron simulator

conda create -n opentrons python=3
conda activate opentrons
conda search -c bioconda opentrons #check version
conda install -c bioconda opentrons


# simulate opentrons protocols #


# activate opentron conda environment 
conda activate opentrons


# simulate protocol
# -L is directory of custom labware definitions
# next path is protocol to simulate

cd ~/Documents/01_Work/03_Docs/Opentron/

opentrons_simulate -L Deiner_Opentrons_Protocols/Labware/custom_labware/ Deiner_Opentrons_Protocols/PCR/Index_PCR/

