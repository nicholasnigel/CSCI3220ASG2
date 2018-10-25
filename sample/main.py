from Graph import Graph

G = Graph()

# prompt
codon = raw_input()

while bool(codon) :
    # divide codon into k-1 prefix and k-1 suffix
    prefix = codon[:len(codon)-1]
    suffix = codon[1:]
    G.add_node(prefix)
    G.add_node(suffix)

    if prefix != suffix:
        G.add_edge(prefix, suffix, codon)

    try:
        codon = raw_input()
    except(EOFError):
        break


# Commands to run in ordcer to do the eulerian path
start = G.find_start()
G.euler(start)
G.print_euler()




