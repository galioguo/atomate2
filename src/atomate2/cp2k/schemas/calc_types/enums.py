"""
Autogenerated Enums for CP2K RunType, TaskType, and CalcType
Do not edit this by hand. Edit generate.py or run_types.yaml instead
"""
from emmet.core.utils import ValueEnum


class RunType(ValueEnum):
    """ CP2K calculation run types """

    PBE = "PBE"
    GGA = "GGA"
    R2SCAN = "R2SCAN"
    METAGGA = "METAGGA"
    HYBRID = "HYBRID"
    HSE06 = "HSE06"
    PBE0 = "PBE0"
    RSH = "RSH"
    PBE_U = "PBE+U"
    GGA_U = "GGA+U"
    R2SCAN_U = "R2SCAN+U"
    METAGGA_U = "METAGGA+U"
    HYBRID_U = "HYBRID+U"
    HSE06_U = "HSE06+U"
    PBE0_U = "PBE0+U"
    RSH_U = "RSH+U"
    LDA = "LDA"
    LDA_U = "LDA+U"


class TaskType(ValueEnum):
    """ CP2K calculation task types """

    Static = "Static"
    Structure_Optimization = "Structure Optimization"
    Constrained_Structure_Optimization = "Constrained Structure Optimization"
    Molecular_Dynamics = "Molecular Dynamics"
    NSCF_Line = "NSCF Line"
    NSCF_Uniform = "NSCF Uniform"
    Unrecognized = "Unrecognized"


class CalcType(ValueEnum):
    """ CP2K calculation types """

    PBE_Static = "PBE Static"
    PBE_Structure_Optimization = "PBE Structure Optimization"
    PBE_Constrained_Structure_Optimization = "PBE Constrained Structure Optimization"
    PBE_Molecular_Dynamics = "PBE Molecular Dynamics"
    PBE_NSCF_Line = "PBE NSCF Line"
    PBE_NSCF_Uniform = "PBE NSCF Uniform"
    PBE_Unrecognized = "PBE Unrecognized"
    GGA_Static = "GGA Static"
    GGA_Structure_Optimization = "GGA Structure Optimization"
    GGA_Constrained_Structure_Optimization = "GGA Constrained Structure Optimization"
    GGA_Molecular_Dynamics = "GGA Molecular Dynamics"
    GGA_NSCF_Line = "GGA NSCF Line"
    GGA_NSCF_Uniform = "GGA NSCF Uniform"
    GGA_Unrecognized = "GGA Unrecognized"
    R2SCAN_Static = "R2SCAN Static"
    R2SCAN_Structure_Optimization = "R2SCAN Structure Optimization"
    R2SCAN_Constrained_Structure_Optimization = "R2SCAN Constrained Structure Optimization"
    R2SCAN_Molecular_Dynamics = "R2SCAN Molecular Dynamics"
    R2SCAN_NSCF_Line = "R2SCAN NSCF Line"
    R2SCAN_NSCF_Uniform = "R2SCAN NSCF Uniform"
    R2SCAN_Unrecognized = "R2SCAN Unrecognized"
    METAGGA_Static = "METAGGA Static"
    METAGGA_Structure_Optimization = "METAGGA Structure Optimization"
    METAGGA_Constrained_Structure_Optimization = "METAGGA Constrained Structure Optimization"
    METAGGA_Molecular_Dynamics = "METAGGA Molecular Dynamics"
    METAGGA_NSCF_Line = "METAGGA NSCF Line"
    METAGGA_NSCF_Uniform = "METAGGA NSCF Uniform"
    METAGGA_Unrecognized = "METAGGA Unrecognized"
    HYBRID_Static = "HYBRID Static"
    HYBRID_Structure_Optimization = "HYBRID Structure Optimization"
    HYBRID_Constrained_Structure_Optimization = "HYBRID Constrained Structure Optimization"
    HYBRID_Molecular_Dynamics = "HYBRID Molecular Dynamics"
    HYBRID_NSCF_Line = "HYBRID NSCF Line"
    HYBRID_NSCF_Uniform = "HYBRID NSCF Uniform"
    HYBRID_Unrecognized = "HYBRID Unrecognized"
    HSE06_Static = "HSE06 Static"
    HSE06_Structure_Optimization = "HSE06 Structure Optimization"
    HSE06_Constrained_Structure_Optimization = "HSE06 Constrained Structure Optimization"
    HSE06_Molecular_Dynamics = "HSE06 Molecular Dynamics"
    HSE06_NSCF_Line = "HSE06 NSCF Line"
    HSE06_NSCF_Uniform = "HSE06 NSCF Uniform"
    HSE06_Unrecognized = "HSE06 Unrecognized"
    PBE0_Static = "PBE0 Static"
    PBE0_Structure_Optimization = "PBE0 Structure Optimization"
    PBE0_Constrained_Structure_Optimization = "PBE0 Constrained Structure Optimization"
    PBE0_Molecular_Dynamics = "PBE0 Molecular Dynamics"
    PBE0_NSCF_Line = "PBE0 NSCF Line"
    PBE0_NSCF_Uniform = "PBE0 NSCF Uniform"
    PBE0_Unrecognized = "PBE0 Unrecognized"
    RSH_Static = "RSH Static"
    RSH_Structure_Optimization = "RSH Structure Optimization"
    RSH_Constrained_Structure_Optimization = "RSH Constrained Structure Optimization"
    RSH_Molecular_Dynamics = "RSH Molecular Dynamics"
    RSH_NSCF_Line = "RSH NSCF Line"
    RSH_NSCF_Uniform = "RSH NSCF Uniform"
    RSH_Unrecognized = "RSH Unrecognized"
    PBE_U_Static = "PBE+U Static"
    PBE_U_Structure_Optimization = "PBE+U Structure Optimization"
    PBE_U_Constrained_Structure_Optimization = "PBE+U Constrained Structure Optimization"
    PBE_U_Molecular_Dynamics = "PBE+U Molecular Dynamics"
    PBE_U_NSCF_Line = "PBE+U NSCF Line"
    PBE_U_NSCF_Uniform = "PBE+U NSCF Uniform"
    PBE_U_Unrecognized = "PBE+U Unrecognized"
    GGA_U_Static = "GGA+U Static"
    GGA_U_Structure_Optimization = "GGA+U Structure Optimization"
    GGA_U_Constrained_Structure_Optimization = "GGA+U Constrained Structure Optimization"
    GGA_U_Molecular_Dynamics = "GGA+U Molecular Dynamics"
    GGA_U_NSCF_Line = "GGA+U NSCF Line"
    GGA_U_NSCF_Uniform = "GGA+U NSCF Uniform"
    GGA_U_Unrecognized = "GGA+U Unrecognized"
    R2SCAN_U_Static = "R2SCAN+U Static"
    R2SCAN_U_Structure_Optimization = "R2SCAN+U Structure Optimization"
    R2SCAN_U_Constrained_Structure_Optimization = "R2SCAN+U Constrained Structure Optimization"
    R2SCAN_U_Molecular_Dynamics = "R2SCAN+U Molecular Dynamics"
    R2SCAN_U_NSCF_Line = "R2SCAN+U NSCF Line"
    R2SCAN_U_NSCF_Uniform = "R2SCAN+U NSCF Uniform"
    R2SCAN_U_Unrecognized = "R2SCAN+U Unrecognized"
    METAGGA_U_Static = "METAGGA+U Static"
    METAGGA_U_Structure_Optimization = "METAGGA+U Structure Optimization"
    METAGGA_U_Constrained_Structure_Optimization = "METAGGA+U Constrained Structure Optimization"
    METAGGA_U_Molecular_Dynamics = "METAGGA+U Molecular Dynamics"
    METAGGA_U_NSCF_Line = "METAGGA+U NSCF Line"
    METAGGA_U_NSCF_Uniform = "METAGGA+U NSCF Uniform"
    METAGGA_U_Unrecognized = "METAGGA+U Unrecognized"
    HYBRID_U_Static = "HYBRID+U Static"
    HYBRID_U_Structure_Optimization = "HYBRID+U Structure Optimization"
    HYBRID_U_Constrained_Structure_Optimization = "HYBRID+U Constrained Structure Optimization"
    HYBRID_U_Molecular_Dynamics = "HYBRID+U Molecular Dynamics"
    HYBRID_U_NSCF_Line = "HYBRID+U NSCF Line"
    HYBRID_U_NSCF_Uniform = "HYBRID+U NSCF Uniform"
    HYBRID_U_Unrecognized = "HYBRID+U Unrecognized"
    HSE06_U_Static = "HSE06+U Static"
    HSE06_U_Structure_Optimization = "HSE06+U Structure Optimization"
    HSE06_U_Constrained_Structure_Optimization = "HSE06+U Constrained Structure Optimization"
    HSE06_U_Molecular_Dynamics = "HSE06+U Molecular Dynamics"
    HSE06_U_NSCF_Line = "HSE06+U NSCF Line"
    HSE06_U_NSCF_Uniform = "HSE06+U NSCF Uniform"
    HSE06_U_Unrecognized = "HSE06+U Unrecognized"
    PBE0_U_Static = "PBE0+U Static"
    PBE0_U_Structure_Optimization = "PBE0+U Structure Optimization"
    PBE0_U_Constrained_Structure_Optimization = "PBE0+U Constrained Structure Optimization"
    PBE0_U_Molecular_Dynamics = "PBE0+U Molecular Dynamics"
    PBE0_U_NSCF_Line = "PBE0+U NSCF Line"
    PBE0_U_NSCF_Uniform = "PBE0+U NSCF Uniform"
    PBE0_U_Unrecognized = "PBE0+U Unrecognized"
    RSH_U_Static = "RSH+U Static"
    RSH_U_Structure_Optimization = "RSH+U Structure Optimization"
    RSH_U_Constrained_Structure_Optimization = "RSH+U Constrained Structure Optimization"
    RSH_U_Molecular_Dynamics = "RSH+U Molecular Dynamics"
    RSH_U_NSCF_Line = "RSH+U NSCF Line"
    RSH_U_NSCF_Uniform = "RSH+U NSCF Uniform"
    RSH_U_Unrecognized = "RSH+U Unrecognized"
    LDA_Static = "LDA Static"
    LDA_Structure_Optimization = "LDA Structure Optimization"
    LDA_Constrained_Structure_Optimization = "LDA Constrained Structure Optimization"
    LDA_Molecular_Dynamics = "LDA Molecular Dynamics"
    LDA_NSCF_Line = "LDA NSCF Line"
    LDA_NSCF_Uniform = "LDA NSCF Uniform"
    LDA_Unrecognized = "LDA Unrecognized"
    LDA_U_Static = "LDA+U Static"
    LDA_U_Structure_Optimization = "LDA+U Structure Optimization"
    LDA_U_Constrained_Structure_Optimization = "LDA+U Constrained Structure Optimization"
    LDA_U_Molecular_Dynamics = "LDA+U Molecular Dynamics"
    LDA_U_NSCF_Line = "LDA+U NSCF Line"
    LDA_U_NSCF_Uniform = "LDA+U NSCF Uniform"
    LDA_U_Unrecognized = "LDA+U Unrecognized"
