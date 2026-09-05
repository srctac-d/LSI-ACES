import os
import re
import sys

# Automatically set working directory to the directory where this script lives
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Baseline Expected Files matching actual disk layout
EXPECTED_FILES = [
    "INDEX.md",
    "README.md",
    "SPEC_SITE_MASTER_2026.md",
    "Baseline_Alignment_Record.md",
    "Initial_Set_Up_Habitat.md",
    "CHANGELOG.md",
    "01_ISRU_Refinery/MOE_Crucible_Architecture.md",
    "01_ISRU_Refinery/MODULE_01_02_PRESSURIZED_HAB_OPTICS.md",
    "02_Mechanical_Engineering/MODULE_05_06_SOLAR_TOWER.md",
    "02_Civil_Engineering/REGOLITH_TO_RACK_MATRIX.md",
    "02_Civil_Engineering/MODULE_07_08_EXCAVATION.md",
    "03_Structural_Outfitting/IC WOVEN TRUSS NODE.md",
    "04_Power_ECLSS/Power_Distribution_Vanadium.md",
    "04_Power_ECLSS/MODULE_03_04_POWER_THERMAL_ROUTING.md",
]

# Baseline Technical Parameters to Audit
BASELINE_CHECKS = {
    "Baseline_Alignment_Record.md": [
        (r"4\.0\s*ft", "4.0 ft Sub-Floor Envelope"),
        (r"3\.8\s*ft", "~3.8 ft Net Basement Clear Space"),
    ],
    "02_Mechanical_Engineering/MODULE_05_06_SOLAR_TOWER.md": [
        (r"100\s*ft|250\s*ft", "100 ft to 250 ft Variable Tower Elevation"),
    ],
    "SPEC_SITE_MASTER_2026.md": [
        (r"100\s*ft|250\s*ft", "100 ft - 250 ft Tower Range"),
    ]
}

def run_audit():
    print("=== RUNNING LSI-ACES SYSTEM AUDIT ===")
    errors = 0
    warnings = 0

    # 1. Verify File Existence
    print("\n[1/2] Checking Repository File Tree...")
    for rel_path in EXPECTED_FILES:
        full_path = os.path.join(SCRIPT_DIR, rel_path)
        if os.path.exists(full_path):
            print(f"  [OK] Found: {rel_path}")
        else:
            print(f"  [ERROR] Missing expected file: {rel_path}")
            errors += 1

    # 2. Verify Baseline Parameters across Files
    print("\n[2/2] Verifying Cross-File Baseline Consistency...")
    for rel_path, checks in BASELINE_CHECKS.items():
        full_path = os.path.join(SCRIPT_DIR, rel_path)
        if not os.path.exists(full_path):
            continue
        
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        for pattern, label in checks:
            if re.search(pattern, content, re.IGNORECASE):
                print(f"  [OK] {rel_path} -> Verified: {label}")
            else:
                print(f"  [WARNING] {rel_path} -> Missing parameter match: {label}")
                warnings += 1

    print("\n=== AUDIT SUMMARY ===")
    print(f"Errors: {errors} | Warnings: {warnings}")
    
    if errors == 0 and warnings == 0:
        print("RESULT: All baseline parameters and file structures are FULLY INTEGRATED!")
        return 0
    else:
        print("RESULT: Audit complete with items requiring attention.")
        return 1

if __name__ == "__main__":
    sys.exit(run_audit())