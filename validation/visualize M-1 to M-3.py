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
import networkx as nx
import matplotlib.pyplot as plt




filename = "validation/M-1.g6"
G : nx.graph.Graph = nx.read_graph6(filename)

pos = {0:(-.25,8), 1:(0,6), 2:(0,2), 3:(-.25,0),
       4:(1,7), 5:(1,5), 6:(1,3), 7:(1,1),
                8:(2,5), 9:(2,3),
               10:(3,5), 11:(3,3),
      12:(4,7), 13:(4,5), 14:(4,3), 15:(4,1),
      16:(5.25,8), 17:(5,6), 18:(5,2), 19:(5.25,0)}
plt.figure(figsize=(6.4, 4.8))
nx.draw_networkx(G, pos=pos)
plt.savefig('M-1 generated.png')
# plt.show()



filename = "M-2.g6"
G : nx.graph.Graph = nx.read_graph6(filename)

pos = {0:(-.25,8), 1:(0,6), 2:(0,2), 3:(-.25,0),
       4:(1,7), 5:(1,5), 6:(1,3), 7:(1,1),
                8:(2,5), 9:(2,3),
               10:(3,5), 11:(3,3),
      12:(4,7), 13:(4,5), 14:(4,3), 15:(4,1),
      16:(5,8), 17:(5,6), 18:(5,2), 19:(5,0),
      
      20:(6,8), 21:(6,6), 22:(6,2), 23:(6,0),
      24:(7,7), 25:(7,5), 26:(7,3), 27:(7,1),
                28:(8,5), 29:(8,3),
               30:(9,5), 31:(9,3),
      32:(10,7), 33:(10,5), 34:(10,3), 35:(10,1),
      36:(11.25,8), 37:(11,6), 38:(11,2), 39:(11.25,0)}
plt.figure(figsize=(6.4*2, 4.8))
nx.draw_networkx(G, pos=pos)
plt.savefig('M-2 generated.png')
# plt.show()


filename = "M-3.g6"
G : nx.graph.Graph = nx.read_graph6(filename)

pos = {0:(-.25,8), 1:(0,6), 2:(0,2), 3:(-.25,0),
       4:(1,7), 5:(1,5), 6:(1,3), 7:(1,1),
                8:(2,5), 9:(2,3),
               10:(3,5), 11:(3,3),
      12:(4,7), 13:(4,5), 14:(4,3), 15:(4,1),
      16:(5,8), 17:(5,6), 18:(5,2), 19:(5,0),
      
      20:(6,8), 21:(6,6), 22:(6,2), 23:(6,0),
      24:(7,7), 25:(7,5), 26:(7,3), 27:(7,1),
                28:(8,5), 29:(8,3),
               30:(9,5), 31:(9,3),
      32:(10,7), 33:(10,5), 34:(10,3), 35:(10,1),
      36:(11,8), 37:(11,6), 38:(11,2), 39:(11,0),
      
      40:(12,8), 41:(12,6), 42:(12,2), 43:(12,0),
      44:(13,7), 45:(13,5), 46:(13,3), 47:(13,1),
                48:(14,5), 49:(14,3),
               50:(14,5), 51:(14,3),
      52:(15,7), 53:(15,5), 54:(15,3), 55:(15,1),
      56:(16.25,8), 57:(16,6), 58:(16,2), 59:(16.25,0)}
plt.figure(figsize=(6.4*3, 4.8))
nx.draw_networkx(G, pos=pos)
plt.savefig('M-3 generated.png')
# plt.show()
