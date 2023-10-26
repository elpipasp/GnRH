#Author Elpiniki Paspali: elpiniki.paspali@strath.ac.uk
#usage source calculate_sasa.tcl
# Set the resolution for SASA calculation (1.4 Ångstrom is a common choice)
set resolution 1.4

# Create a selection for your protein (modify 'protein' to match your selection)
set sel [atomselect top "protein"]

# Open an output file to store the calculated SASA values
set output_file [open "SASA_results.dat" w]

# Get the number of frames in your trajectory
set num_frames [molinfo top get numframes]

# Loop through each frame
for {set frame 0} {$frame < $num_frames} {incr frame} {
    # Go to the current frame
    animate goto $frame

    # Calculate SASA for the current frame
    set sasa [measure sasa $resolution $sel]

    # Append the SASA value to the output file
    puts $output_file "$frame $sasa"

    # Print the progress to the console
    puts "Frame $frame: SASA = $sasa"
}

# Close the output file
close $output_file

# Delete the selection
$sel delete

# Exit VMD
exit
