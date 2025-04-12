# Q1: Network Loops

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
