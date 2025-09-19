# Copyright 2025 Jim Haslett

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os
import networkx as nx


def usage():
    print('Usage: ')
    print(f'{sys.argv[0]} -M <filename>  \n\tConverts an edge list in <filename> to graph6 format')


def main():
    if len(sys.argv) < 2:
        usage()
        exit(0)

    infilename = sys.argv[1]
    
    outfilename, ext = os.path.splitext(os.path.basename(infilename))
    if ext in ['.gz', '.bz2', '.xz']:
        outfilename = os.path.splitext(outfilename)[0]
    outfilename += '.s6'
    print(outfilename)
    
    G : nx.graph.Graph = nx.read_edgelist(infilename)
    # nx.graph6.write_graph6(G, outfilename)
    nx.sparse6.write_sparse6(G, outfilename)
    print(f'Read edge list from {infilename} and wrote graph6 format to {outfilename}')
    
    
if __name__ == '__main__':
    main()    