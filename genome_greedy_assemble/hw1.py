import graph
import util
import time

# Code for PROBLEM 1
# You are welcome to develop your code as a separate Python module
# and import it here if that is more convenient for you.
def greedy_assemble(reads):
    q = []

    init_time = time.time()

    for i in range(len(reads)):
        for j in range(len(reads)):
            if i == j:
                continue
            # Add object to queue
            n = (i, j, -util.overlap_length(reads[i], reads[j]))
            q.append(n)
    
    # Sort
    q.sort(key = lambda x: (x[2], reads[x[0]], reads[x[1]]))
    
    list_creation_time = time.time()
    print("List creation: ", list_creation_time - init_time)

    G = graph.AdjacencyListDirectedGraph(len(reads))
    while not G.is_connected():
        e = q.pop(0)
        if G.outdegree(e[0]) is 0 and G.indegree(e[1]) is 0:
            G.add_edge(e[0], e[1])
            #print("+ ", reads[e[0]], reads[e[1]])
            if G.has_cycle():
                G.remove_edge(e[0], e[1])
                #print("- ", reads[e[0]], reads[e[1]])
    
    algo_time = time.time()
    print("Algorithm: ", algo_time - list_creation_time)

    start = 0
    for i in range(G.num_vertices()):
        if G.isConnectedUtil(i) == True:
            start = i 
            break
    
    ordered_reads = []
    ordered_reads.append(reads[start])

    nxt = G.out_edges(start)

    while len(nxt) > 0:
        nxt = nxt[0][1]
        ordered_reads.append(reads[nxt])
        nxt = G.out_edges(nxt)

    result = util.merge_ordered_reads(ordered_reads)

    final_time = time.time()
    print("Merge time: ", final_time - algo_time)

    return result


def read_strings_from_file(filename):
    return [line.rstrip() for line in open(filename)]
    

def test_greedy_assemble_with_files(reads_filename, superstring_filename):
    reads = read_strings_from_file(reads_filename)
    [superstring] = read_strings_from_file(superstring_filename)
    assert greedy_assemble(reads) == superstring 

if __name__ == '__main__':
    # TEST: greedy_assemble returns a string
    sanity_test_reads = read_strings_from_file("tests/test_reads.txt")
    assert isinstance(greedy_assemble(sanity_test_reads), str)
    print("SUCCESS: greedy_assemble returns a string passed!")
    print()

    # TEST: greedy_assemble returns a superstring
    def is_superstring(s, reads):
        return all(read in s for read in reads)
    assert is_superstring(greedy_assemble(sanity_test_reads), sanity_test_reads)
    print("SUCCESS: greedy_assemble returns a superstring passed!")
    print()

    # TEST: greedy_assemble_small_test_1
    small_test1_reads = ["GTT", "ATCTC", "CTCAA"]
    assert greedy_assemble(small_test1_reads) == "ATCTCAAGTT"
    print("SUCCESS: greedy_assemble_small_test_1 passed!")
    print()

    # TEST: greedy_assemble_small_test_2
    small_test2_reads = ["CGAAG", "ATCGA", "AGAG", "GGG"]
    assert greedy_assemble(small_test2_reads) == "ATCGAAGAGGG"
    print("SUCCESS: greedy_assemble_small_test_2 passed!")
    print()

    # TEST: greedy_assemble_small_test_3
    small_test3_reads = ["C", "T", "G", "A"]
    assert greedy_assemble(small_test3_reads) == 'ACGT'
    print("SUCCESS: greedy_assemble_small_test_3 passed!")
    print()

    # TEST: greedy_assemble large test 1
    test_greedy_assemble_with_files("tests/large_test1_reads.txt", "tests/large_test1_superstring.txt")
    print("SUCCESS: greedy_assemble large test 1 passed!")
    print()

    # List creation:  3.1494038105010986
    # Algorithm:  27.507272958755493
    # Merge time:  0.0910341739654541
    # reads = read_strings_from_file("ebola_reads.txt")
    # result = greedy_assemble(reads)
    # print(result)
    # print("SUCCESS: ebola_reads.txt fin")
    # print()

    # List creation:  40.04826307296753
    # Algorithm:  1464.8457050323486
    # Merge time:  2.029806137084961
    # reads = read_strings_from_file("ebola_full_genome_reads.txt")
    # result = greedy_assemble(reads)
    # print(result)
    # print("SUCCESS: ebola_full_genome_reads.txt fin")
    # print()
