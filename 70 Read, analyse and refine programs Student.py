# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
resultsTable = [["Mattson", 686, 22.87], ["Blair", 380, 12.67],
                ["Leonhardt", 1051, 35.05], ["Miller", 406, 13.53],
                ["Rowan", 477, 15.90]]

layout = ""
totalVote = 0
totalPercent = 0.0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
layout = "{}  {}  {}"
print (layout.format ("Candidate", "Votes", "Percent"))

layout = "{:<10}  {:>7}  {:>6.5f}"
for row in resultsTable:
    totalVote = totalVote + row[2]
    totalPercent = totalPercent + row[2]
    print (layout.format (row[0], row[1], row[2]))

print ("="*30)
layout = "{:>10}  {:>7}  {:>6.5f}"
print (layout.format ("Total", totalVote, totalPercent))
