# Distributed Asynchronous Distance Vector Routing Simulation

## 1. Overview

This project simulates a Distributed Asynchronous Distance Vector Routing Algorithm across four nodes (node0 to node3). Each node maintains its own distance table and exchanges routing packets with its immediate neighbors in an emulated network environment. The algorithm proceeds asynchronously until all nodes converge to the correct routing tables.

## 2. Project Structure

Distributed-asynchronous-distance-vector-routing/
├── distance_vector.c         # Main simulator (emulator) source file (formerly distance_vector.c)
├── node0.c         # Implementation of Node 0's routing algorithm
├── node1.c         # Implementation of Node 1's routing algorithm
├── node2.c         # Implementation of Node 2's routing algorithm
├── node3.c         # Implementation of Node 3's routing algorithm
└── README.md       # This documentation file

## 3. Assignment Description

The assignment requires the implementation of a distributed, asynchronous distance vector routing protocol. The main tasks include:

- **Initialization (rtinitX):**  
  Each node initializes its distance table based on direct link costs and sends its initial distance vector to its connected neighbors.

- **Routing Updates (rtupdateX):**  
  When a node receives a routing packet from a neighbor, it updates its distance table if a better (lower-cost) route is found and, if necessary, notifies its neighbors of the change.

- **Extra Credit – Link Handlers:**  
  Some nodes (e.g., node0 and node1) include link handler routines to update the routing tables dynamically when the cost of a link changes.

## 4. Compilation and Execution

### Compilation

Use GCC (or your preferred compiler) to compile all source files together. For example:

    gcc -o simulation distance_vector.c node0.c node1.c node2.c node3.c


### Running the Simulation

Run the compiled executable:

    ./simulation

When prompted, you will be asked to enter a TRACE value. For example:

    Enter TRACE: 3

A TRACE value of 3 displays detailed log output, which is useful for debugging and analyzing how routing packets are exchanged and processed.

## 5. Problems Encountered

During the development of this project, several issues were encountered and resolved as follows:

### a. Multiple Definition of Global Variable `clocktime`

- **Problem:**  
  The linker generated errors because `clocktime` was defined in multiple files (distance_vector.c and the various node files).

- **Solution/Approach:**  
  - **Definition:** `clocktime` is defined only once in prog3.c as:
  
        float clocktime = 0.000;
  
  - **Declaration:** In all node files (node0.c, node1.c, node2.c, node3.c), `clocktime` is declared as an external variable:
  
        extern float clocktime;
  
  This ensures that all files reference the same variable, eliminating multiple definition errors.


## 6. Functioning of the Code

### Main Simulator (distance_vector.c)
- **Core Functionality:**  
  The main simulator sets up an event-driven simulation environment. It initializes global variables (like `clocktime`), reads the TRACE level from the user, and then calls the initialization routines (`rtinit0()`, `rtinit1()`, etc.) for each node.
  
- **Event Processing:**  
  The simulator maintains a list of events (e.g., packet arrivals, link changes). It processes each event in order, calling the appropriate update routine (e.g., `rtupdateX()`) when a routing packet arrives, and the link handler routines when link cost changes are scheduled.
  
- **Termination:**  
  The simulation runs until there are no further events, at which point it prints the final routing tables using functions like `printmincost0()`.

### Node Files (node0.c, node1.c, node2.c, node3.c)
- **Initialization (`rtinitX()`):**  
  Each node initializes its own distance table with the direct link costs. It then calculates the minimum cost to each destination and sends an initial routing packet (using functions like `sendpktX()`) to its direct neighbors.
  
- **Routing Updates (`rtupdateX()`):**  
  When a node receives a routing packet from a neighbor, it compares the received costs with its current distance table. If a lower-cost path is found via that neighbor, the node updates its table and sends out updated packets to its neighbors.
  
- **Link Handlers:**  
  In nodes that support dynamic link changes, routines like `linkhandler0()` and `linkhandler1()` adjust the distance table when the cost of a direct link changes. The node then recalculates the minimum path costs and notifies neighboring nodes if a change occurs.

## 7. Testing and Results

The simulation was thoroughly tested at various TRACE levels. Key observations include:

- **Initial Routing Tables:**  
  Each node correctly initializes its distance table based on the direct link costs provided.
  
- **Routing Updates & Convergence:**  
  Detailed TRACE logs show the exchange of routing packets and the progressive update and convergence of the distance tables across all nodes.
  
- **Final Output:**  
  Final routing tables are printed, confirming that all nodes have computed the lowest cost routes to every destination.

Refer to the attached screenshots and log files for detailed test results and outputs.


## 8. Conclusion

This project successfully implements a distributed, asynchronous distance vector routing protocol. The challenges encountered—such as handling multiple definitions of global variables and ensuring portable random number generation—were effectively addressed. The simulation demonstrates the propagation of routing information and the convergence of routing tables across a network of four nodes, fulfilling the requirements of the assignment.

