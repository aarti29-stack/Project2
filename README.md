# Transmission & Distribution Networks with pandapower 

This project explores **power-flow analysis** and **visualization** of transmission networks using
[pandapower] 
Shows IEEE **9-bus**, **118-bus**, and **1354-bus (PEGASE)** test systems to:

- run power flow (AC load flow)
- inspect bus and line results (voltages, injections, flows, losses)
- verify energy balance
- visualize grids and **line loading** (overload detection)
- study the effect of **increased demand** on congestion

---

## Contents

- `Project2.py` – end-to-end script:
  - load IEEE test cases from `pandapower.networks`
  - run `pp.runpp(net)` (power flow)
  - analyze `net.res_bus`, `net.res_line`
  - plot networks (9, 118, 1354 bus)
  - overload visualization 

---
## Key Analysis & Checks
- Bus Results (`net.res_bus`)
 vm_pu – voltage magnitude (p.u.)
 p_mw – active power injection (negative = generation, positive = load)
 q_mvar – reactive power injection

- Line Results (`net.res_line`)
 p_from_mw, p_to_mw – directional flows
 pl_mw – active power loss per line
 loading_percent – thermal loading (bottleneck indicator)
