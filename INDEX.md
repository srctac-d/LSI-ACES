# LSI-ACES Master Architectural Index & Volume Mapping

This file serves as the definitive directory index mapping all technical specifications, engineering volumes, and subsystems across the LSI-ACES repository structure.

---

## 📂 Repository Directory Matrix

```text
LSI-ACES-1/
├── INDEX.md                            <-- You are here
├── README.md                           <-- Project landing page & overview
├── SPEC_SITE_MASTER_2026.md            <-- Primary master spec baseline
├── Baseline Alignment Record.md        <-- Cross-volume integration & handshakes
├── Initial Set Up Habitat.md           <-- 10ft cell & 15ft bulkhead setup
├── CHANGELOG.md                        <-- System revision history
│
├── 01_ISRU_Refinery/                  
│   ├── MOE_Crucible_Architecture.md    <-- Vol 33: Plasma arc, 80kW IR, inside electrode
│   └── Optical_Growth_Sapphire.md      <-- Vol 33: Coudé tower optics & laser sweeps
│
├── 02_Civil_Engineering/              
│   ├── Trench_Jacking_Alignment.md     <-- Vol 24: 80ft saddle trench & screw jacks
│   └── Bottom_Foam_Sliders.md          <-- Vol 24: Insulation panels & backfilling
│
├── 03_Structural_Outfitting/          
│   ├── Split_Joist_Decking.md          <-- Vol 21-22: 5+2ft split joists & clam-shells
│   ├── In_Situ_Geocrete_Casting.md     <-- Vol 23, 25: Thermal curing bed (+25°C)
│   └── Fluid_Sump_Containment.md       <-- Vol 24-25: Polymer bladders & vacuum reclaim
│
└── 04_Power_ECLSS/                    
    └── Power_Distribution_Vanadium.md  <-- Solid-state vanadium matrix & radiation immunity



    📖 Subsystem Volume Cross-ReferenceDomain DirectoryFile NameAssociated Volume(s)Key Technical Focus01_ISRU_RefineryMOE_Crucible_Architecture.mdVol 33Transportable crucible, plasma melt, 80kW susceptor, spot heat control01_ISRU_RefineryOptical_Growth_Sapphire.mdVol 33Single-crystal sapphire growth, Coudé optical arrays02_Civil_EngineeringTrench_Jacking_Alignment.mdVol 2480-foot saddle trench alignment, X-assembly screw jacks03_Structural_OutfittingSplit_Joist_Decking.mdVol 21, 225-foot fairing-constrained joists, 2-foot center bridges03_Structural_OutfittingIn_Situ_Geocrete_Casting.mdVol 23, 25Regolith-alkali geocrete cold-casting, unbonded regolith shims03_Structural_OutfittingFluid_Sump_Containment.mdVol 24, 25Sub-floor basin bladders, 0.1 psi vacuum reclaim pumps04_Power_ECLSSPower_Distribution_Vanadium.mdHardware SpecSolid-state vanadium transformers, radiation immunity, 480V/120V bus