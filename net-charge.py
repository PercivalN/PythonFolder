# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

# Creates a dictionary
pKR = {
    "y": "10.07",
    "c": "8.18",
    "k": "10.53",
    "h": "6.00",
    "r": "12.48",
    "d": "3.65",
    "e": "4.25"
}

# Using count() to count the numbers of each amino acid
yAminoAcids = str(float(insulin.count("y")))
print("There are " + yAminoAcids + " Y Amino Acids in the sequence.")

# Code for counting each amino acid 
seqCount = ({x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']})
print(seqCount)

#
pH = 0
while (pH <= 14):
    netCharge = (
        +(sum({x: (seqCount[x]*(10**float(pKR[x])))/((10**pH)+(10**float(pKR[x]))) \
            for x in ['k','h','r']}.values()))
        -(sum({x: (seqCount[x]*(10**pH))/((10**pH)+(10**float(pKR[x]))) \
            for x in ['y','c','d','e']}.values()))
    )
    print('{0:.2f}'.format(pH), netCharge)
    pH += 1


