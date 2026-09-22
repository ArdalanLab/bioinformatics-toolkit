#calculate the Percentage of GC in a DNA sequence using for loop instead of count function:
dna = "ATGATACCGATG"
#creating a list and adding all the Gs and Cs inside it using a loop:
gc_content = list()
for x in dna:
    if x == "G" or x=="C":
        gc_content.append(x)
#using len() function to calculate the rest:
total_gc_count = len(gc_content) 
dna_len = len(dna)
print(total_gc_count/dna_len*100)

