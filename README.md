# CN_Assignment_3

## Q1: Network Loops

## Overview

This project demonstrates the effects of network loops in a simulated network topology using Mininet. The topology consists of four switches (s1, s2, s3, s4) and eight hosts (h1 to h8) with specified IP addresses. A network loop is intentionally created by adding an extra link between s1 and s3, which leads to issues such as broadcast storms and MAC table instability.

## Topology Details

- **Switches:** s1, s2, s3, s4
- **Hosts:** 
  - h1: 10.0.0.2/24  
  - h2: 10.0.0.3/24  
  - h3: 10.0.0.4/24  
  - h4: 10.0.0.5/24  
  - h5: 10.0.0.6/24  
  - h6: 10.0.0.7/24  
  - h7: 10.0.0.8/24  
  - h8: 10.0.0.9/24
- **Link Latencies:**
  - **Switch-to-Switch:** 7 ms for each link (s1-s2, s2-s3, s3-s4, s4-s1, s1-s3)
  - **Host-to-Switch:** 5 ms for each host link (h1-s1, h2-s1, h3-s2, h4-s2, h5-s3, h6-s3, h7-s4, h8-s4)

## Problem Statement

Due to the loop created by the extra s1-s3 link, the network experiences:
- **Broadcast storms:** Excessive propagation of ARP requests across the network.
- **MAC table instability:** Frequent changes in MAC address table entries resulting in dropped packets and failed communications.

### Test Commands

The following ping tests were performed in the Mininet CLI:
- `h3 ping -c 4 h1`
- `h5 ping -c 4 h7`
- `h8 ping -c 4 h2`

**Observation:**  
All pings fail or exhibit unpredictable behavior due to the broadcast storm induced by the network loop. Packet captures (using Wireshark) on interface s1-eth1 show repeated ARP requests for h1, confirming the loop-induced issues.

## Resolution Approach

### Enabling STP (Spanning Tree Protocol)
To resolve the issue without changing the network topology, STP was enabled on all switches. STP automatically blocks one or more redundant paths, eliminating the loop and stabilizing the network.

### After STP Implementation
- **Ping Tests:**  
  - `h3 ping -c 4 h1`
  - `h5 ping -c 4 h7`
  - `h8 ping -c 4 h2`
- **Results:**  
  Each test now succeeds with predictable delays (approximately 17 ms per hop based on the link latencies) across multiple iterations.
- **Packet Captures:**  
  Confirmed a stable network state with no duplicate frames or continuous ARP broadcasts.

## Running the Project

1. **Environment Setup:**
   - Ensure you have Mininet installed on your Ubuntu Linux device.
   - Python3 should be installed as well as necessary Mininet dependencies.

2. **Execute the Script:**
   - Open a terminal and navigate to the project directory.
   - Run the following command:
     ```bash
     sudo python3 q1_net.py
     ```
   - This will launch the Mininet CLI with the defined topology.

3. **Test the Topology:**
   - In the Mininet CLI, run:
     ```bash
     h3 ping -c 4 h1
     h5 ping -c 4 h7
     h8 ping -c 4 h2
     ```
   - Observe the ping results and note the failure due to the network loop.

4. **Enabling STP:**
   - Modify the script as shown in `q1_net_corrected.py` to enable STP on all switches.
   - Restart the network and rerun the ping tests to verify that the pings succeed.

## Files Included

- **q1_net.py:**  
  Original Mininet script creating the network loop topology.
- **q1_net_corrected.py:**  
  Modified Mininet script with STP enabled to resolve network loops.
- **Wireshark Packet Captures:**  
  Screenshots and capture files showing ARP flooding and stabilization post-STP.
- **This README.md:**  
  Documentation for the Q1 assignment.

## Conclusion

The Q1 assignment illustrates the problems caused by network loops in a Layer 2 environment. By enabling STP, the network stabilizes, allowing proper MAC learning and successful communication between hosts. The provided scripts and documentation offer a comprehensive view of the problem and its resolution.

---

## Q2: Configure Host-based NAT

## Overview

This project updates the original network topology to implement host-based NAT. A new host (H9) is added as a NAT gateway to provide external connectivity for internal hosts h1 and h2. H9 is configured with a public IP (172.16.10.10) and performs NAT for internal IP addresses 10.1.1.2 (h1) and 10.1.1.3 (h2).

## Topology Changes

- **New Host Addition:**  
  - **H9** is added to switch **S1** with a 5 ms host-to-switch link latency.

- **Link Reassignment:**  
  - The links that previously connected **h1** and **h2** to **S1** are now moved to **H9** (links h1–H9 and h2–H9, each with a 5 ms delay).

- **NAT Implementation on H9:**  
  - H9 is configured with a public IP of **172.16.10.10**.
  - NAT functionality is implemented on H9:
    - **Source NAT (SNAT):** Translates outbound traffic from the internal network (10.1.1.0/24) to the public IP.
    - **Destination NAT (DNAT):** Translates incoming traffic destined for the public IP (172.16.10.10) to the appropriate internal host (10.1.1.2 for h1 and 10.1.1.3 for h2).

## Implementation Details

### Topology Update and NAT Setup

- The updated topology is built using Mininet and a Python script (`q2_net.py`):
  - **H9** is added and linked to **S1** with a 5 ms delay.
  - **h1** and **h2** are reattached to **H9** instead of directly connecting to **S1**.
  
- **NAT Configuration on H9:**  
  - **SNAT Rule:**
   
  - **DNAT Rules:**

### Program Execution

- Run the topology with:
  ```bash
  sudo python3 q2_net.py

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


