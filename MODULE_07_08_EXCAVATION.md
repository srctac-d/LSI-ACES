LSI-ACES SPECIFICATION: EXCAVATION, TRENCHING & HOLD-FAST ANCHORAGE
## DOCUMENT ID: SPEC-EXCAV-2026-V1

---

## 1. HALF-DEPTH TRENCH & SOIL MECHANICS

### 1.1 Trench Profile & Dimensions
* **Geometry:** A continuous, radius-bottom half-depth trench excavated directly into polar terrain.
* **Depth:** **6 feet (1.83 meters)** below native grade.
* **Width:** **16 feet (4.88 meters)** at floor level, designed to comfortably cradle **12-to-14-foot diameter structural habitat tubes**.
* **Under-Floor Cradle Planks:** Pre-cured, interlocking **1.5-inch thick structural polymer foam planks** (extruded in the Phase 1 workspace) are laid along the trench floor to serve as a low-friction, thermal-break cradle for inflatable bladder hulls.

### 1.2 Geotechnical Subsurface Physics
* **In-Situ Density:** At 6 to 12 feet deep, compacted polar regolith reaches densities up to **$1.96\text{ g/cm}^3$**.
* **Dilatancy Multiplier:** When excavated, highly angular interlocking grains cause a volumetric expansion into a loose state ($\sim 1.5\text{ g/cm}^3$).
* **Peak Shear Strength:** Compacted regolith exhibits a peak internal friction angle ($\Phi_p$) of **$61.7^\circ$**, requiring high starting torque on rover cutter heads and scraper teeth.

---

## 2. 3x3 LATTICE HOLD-FAST ANCHOR SYSTEM

To overcome low 1/6th $g$ wheel traction during heavy grading, the ACTER rover anchors itself to stationary hold-fast pads and winches against them.

  [ 3x3 LATTICE FRAME ]

┌───────┬───────┬───────┐  ◄── Titanium Ti-6Al-4V Welded Grid
│   O   │   O   │   O   │

├───────┼───────┼───────┤  ◄── Dual-Shear Eyelets at Node Outer Edges
│   O   │   O   │   O   │

├───────┼───────┼───────┤  ◄── 9-Post Hybrid Augers / Rock Bolts
│   O   │   O   │   O   │

└───────┴───────┴───────┘  ◄── Down-Force Lock-Collars Seated Flush


### 2.1 Titanium Lattice Frame Design
* **Material:** Welded **Titanium Alloy (Ti-6Al-4V)** structural lattice.
* **Geometry:** $3\times 3$ grid array providing 9 independent anchoring nodes.
* **Interface Shackles:** Each perimeter node features a **1.5-inch diameter dual-shear eyelet** accepting high-load titanium shackles, clevis pins, or quick-release winch hooks rated to $2\times$ maximum winch pull.

### 2.2 Pre-Drill Rotary Diagnostic & Hybrid Pinning (Module 7)
* **Subsurface Diagnostic:** The ACTER rover pre-drills each node location to sense subsurface substrate resistance in real-time.
* **Adaptive Anchoring:**
  * **Permafrost / Compacted Regolith:** Driven with hollow titanium **helical auger posts** featuring aggressive, low-profile continuous flights.
  * **Solid Bedrock / Boulders:** Driven with expanding **titanium rock bolts** inserted into pre-drilled pilot holes.
* **Uneven Surface Lock-Collars:** Because posts may drive to varying depths on irregular rock, each post is fitted with a heavy-duty **down-force lock collar / clamp**. Once maximum resistance is reached, the collar is torqued down flush against the lattice plate, preventing leverage bending moments on exposed post shafts.

### 2.3 Integrated Retroreflective Surveying Mast
* **Extension Mast:** At least one corner post features a vertical titanium mast protruding above local dust and regolith mounds.
* **Retroreflective Target Collar:** Fitted with a high-contrast micro-prism collar.
* **Function:** Serves as a localized positioning reference for autonomous rover grading and allows LiDAR on the **120-foot hexagonal tower** to detect micro-millimeter anchor drift under load.

---

## 3. POWER LOGISTICS, DUST DEFENSE & MOTOR COOLING

### 3.1 High-Voltage Tether & Ground-Skid Cooling
* **Direct 400V DC Power Feed:** High-voltage tether connected directly to site grid, avoiding onboard battery mass during heavy excavation.
* **Cryogenic Ground Conduction Cooling:** Closed-loop heat pipes carrying low-viscosity silicone fluid thread through motor casings. Heat is dumped directly into the cold ($-20^\circ\text{C}$ to $-50^\circ\text{C}$) native trench floor via copper drag-skids, using lunar bedrock as a passive radiator.
* **Tooth Heat Management:** Scraper bucket cutter teeth are enclosed in sealed double-hull chambers backed by solid thermal conduction straps and trace Nitrogen ($N_2$) heat-transfer gas.

### 3.2 Active Electrostatic Dust Shield (+1.5 kV to +2.0 kV)
* **Coulomb Repulsion:** Exterior metallic faces of excavation frames and tool linkages are energized to **$+1.5\text{ to }+2.0\text{ kV DC}$** relative to environment, repelling positively charged lunar micro-dust.
* **Floating Ground Isolation:** Polymer dielectric pads isolate high-voltage exterior frames from the rover's unified **Floating Chassis Ground Plane** for operational safety.
* **Scraper Sleeves:** All screw drives, hydraulic shafts, and winch drums feature positive-pressure trace gas bellows with self-scouring scraper sleeves.

---
*Copyright © 2026 Steve R Campbell. Licensed under CERN-OHL-S v2.*
