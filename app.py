import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Carrier HVAC Diagnostic System",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Advanced Custom Styling
st.markdown("""
    <style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(180deg, #F8FAFC 0%, #F1F5F9 100%);
    }

    /* Modern Header Container */
    .app-header {
        background: #0F172A;
        padding: 24px 28px;
        border-radius: 16px;
        color: white;
        box-shadow: 0 10px 15px -3px rgba(15, 23, 42, 0.1);
        margin-bottom: 24px;
        border: 1px solid #1E293B;
    }
    .app-header h1 {
        color: #FFFFFF !important;
        font-size: 24px !important;
        font-weight: 700 !important;
        margin: 0 0 6px 0 !important;
    }
    .app-header p {
        color: #94A3B8 !important;
        font-size: 13px !important;
        margin: 0 !important;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }

    /* Option Action Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.4em;
        background-color: #FFFFFF;
        color: #0F172A;
        font-weight: 600;
        font-size: 15px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        transition: all 0.2s ease-in-out;
        margin-bottom: 8px;
        text-align: left;
        padding-left: 18px;
    }
    .stButton>button:hover {
        background-color: #2563EB;
        color: #FFFFFF;
        border-color: #2563EB;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
        transform: translateY(-1px);
    }

    /* Solution Card */
    .solution-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-top: 4px solid #2563EB;
        padding: 24px;
        border-radius: 14px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    .solution-title {
        color: #1E3A8A;
        font-size: 17px;
        font-weight: 700;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .solution-text {
        white-space: pre-line;
        font-size: 14px;
        line-height: 1.6;
        color: #334155;
    }

    /* Safety & Warning Badges */
    .safety-card {
        background-color: #FEF2F2;
        border: 1px solid #FECACA;
        border-left: 5px solid #EF4444;
        padding: 16px 20px;
        border-radius: 12px;
        margin-top: 16px;
    }
    .safety-title {
        color: #991B1B;
        font-weight: 700;
        font-size: 14px;
        margin-bottom: 4px;
    }
    .safety-desc {
        color: #7F1D1D;
        font-size: 13px;
        margin: 0;
    }

    /* Step / Breadcrumb Bar */
    .breadcrumb-bar {
        background: #E2E8F0;
        padding: 8px 16px;
        border-radius: 8px;
        font-size: 12px;
        color: #475569;
        font-weight: 500;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Custom App Header Component
st.markdown("""
    <div class="app-header">
        <p>African Natural Resources & Mines Limited</p>
        <h1>⚙️ Carrier HVAC Diagnostic Engine</h1>
    </div>
""", unsafe_allow_html=True)

class TroubleshootingNode:
    def __init__(self, question_or_result, options=None, solution=None, professional_needed=False, manual_ref=None):
        self.question_or_result = question_or_result
        self.options = options or {}
        self.solution = solution
        self.professional_needed = professional_needed
        self.manual_ref = manual_ref

    def is_leaf(self):
        return self.solution is not None

def build_professional_carrier_tree():
    s_code_12 = TroubleshootingNode(
        "Fault Code 12: Blower On After Power Up",
        solution="• Verify line voltage supplied to furnace/fan coil unit.\n• Inspect primary circuit breaker and door safety switch.\n• Verify control board sequence initialization.",
        manual_ref="Carrier Central Systems Service Manual - Section 4.1"
    )
    s_code_13 = TroubleshootingNode(
        "Fault Code 13: Limit Switch Circuit Open / Lockout",
        solution="• Turn off power and inspect main high-temperature limit switch.\n• Clean or replace clogged return air filters.\n• Open all supply registers and inspect evaporator coil for dust blockage.",
        manual_ref="Carrier Furnace & Air Handler Manual - Code 13"
    )
    s_code_31 = TroubleshootingNode(
        "Fault Code 31 / 33: Pressure Switch Fault / Airflow Cutout",
        solution="• Inspect outdoor condenser coil for heavy dirt accumulation or obstruction.\n• Verify outdoor fan motor operation and capacitor capacitance.\n• Check high-pressure switch contacts for electrical continuity.",
        professional_needed=True,
        manual_ref="Carrier Condensing Units Manual - High Pressure Protection"
    )
    s_code_e1 = TroubleshootingNode(
        "Fault Code E1: Indoor/Outdoor Communication Malfunction",
        solution="• Disconnect main power line completely.\n• Check connection tightness on signal terminals (S1 / S2 / S3).\n• Verify shield grounding continuity on long wiring runs.",
        professional_needed=True,
        manual_ref="Carrier Ductless Multi-Split Manual - Error E1"
    )
    s_code_e3 = TroubleshootingNode(
        "Fault Code E3: Indoor Fan Speed Signal Loss",
        solution="• Disconnect power and check cross-flow fan wheel for mechanical blockage.\n• Test indoor blower motor winding resistance.\n• Replace indoor control board if motor feedback signal is absent.",
        professional_needed=True,
        manual_ref="Carrier Mini-Split Service Manual - Blower Assembly"
    )
    s_code_e4 = TroubleshootingNode(
        "Fault Code E4 / T3: Sensor Open / Short Circuit",
        solution="• Inspect coil thermistor and room ambient temperature thermistor.\n• Measure sensor resistance using multimeter against Carrier Ohms-vs-Temp chart.\n• Replace damaged sensor assembly.",
        professional_needed=True,
        manual_ref="Carrier Sensor Resistance Technical Guide"
    )
    s_code_ec = TroubleshootingNode(
        "Fault Code EC: Refrigerant Leak Detection Active",
        solution="• Shut off unit immediately to protect compressor against oil starvation.\n• Perform nitrogen pressure leak test on flare connections and line set.\n• Repair leak site, evacuate system to <500 microns, and recharge by weight.",
        professional_needed=True,
        manual_ref="Carrier Inverter System Service Manual - Leak Diagnostics"
    )

    s_dirty_filter = TroubleshootingNode(
        "Diagnosis: Severe Airflow Restriction / Dirty Filter",
        solution="• Turn off equipment power supply.\n• Replace disposable pleated filters or wash mini-split mesh filters in warm water.\n• Verify return duct air velocities prior to restart.",
        manual_ref="Carrier Preventative Maintenance Schedule - Monthly Protocols"
    )
    s_frozen_coils = TroubleshootingNode(
        "Diagnosis: Evaporator Coil Freezing",
        solution="• Switch thermostat from COOL to FAN ONLY mode to defrost coil.\n• Inspect for restricted return air filters or blocked grilles.\n• If icing reoccurs, check operating suction pressure for refrigerant undercharge.",
        professional_needed=True,
        manual_ref="Carrier Technical Service Guide - Defrost Procedures"
    )
    s_drain_clog = TroubleshootingNode(
        "Diagnosis: Condensate Drain Blockage / Float Switch Trip",
        solution="• Clear primary condensate trap using wet/dry vacuum or nitrogen blow-out.\n• Inspect secondary float switch for standing water.\n• Flush drain line with clean water and test drain pump operation.",
        manual_ref="Carrier Installation Guidelines - Drainage Systems"
    )

    n_carrier_codes = TroubleshootingNode(
        "Select displayed Carrier status code or LED sequence:",
        options={
            "Code 12 — Blower On After Power Up": s_code_12,
            "Code 13 — Limit Circuit Lockout": s_code_13,
            "Code 31/33 — High Pressure Fault": s_code_31,
            "Code E1 — Communication Error": s_code_e1,
            "Code E3 — Indoor Fan Fault": s_code_e3,
            "Code E4/T3 — Sensor Resistance Error": s_code_e4,
            "Code EC — Refrigerant Leak Detected": s_code_ec,
            "Unlisted Diagnostic Flash Sequence": TroubleshootingNode(
                "Carrier Unlisted Diagnostic Code",
                solution="Inspect internal control board service label for unit-specific diagnostic tables or attach Carrier Service Tool.",
                manual_ref="Carrier Universal Field Guide"
            )
        }
    )

    n_carrier_minisplit = TroubleshootingNode(
        "Select Mini-Split / Ductless System Symptom:",
        options={
            "Displaying Error Code / Blinking LEDs": n_carrier_codes,
            "Indoor Unit Water Leak / Dripping": s_drain_clog,
            "Low Air Volume / Reduced Cooling": s_dirty_filter,
            "Frost / Ice Formation on Wall Unit": s_frozen_coils
        }
    )

    n_carrier_central = TroubleshootingNode(
        "Select Central AC / Package Unit Symptom:",
        options={
            "Control Board Flashing LED Code": n_carrier_codes,
            "System Running But Blowing Warm Air": TroubleshootingNode(
                "Carrier Central Unit Warm Air Delivery",
                solution="• Inspect outdoor circuit breaker.\n• Verify thermostat mode is set to COOL and setpoint is below room temp.\n• Check contactor coil voltage and dual-run capacitor capacitance.",
                professional_needed=True,
                manual_ref="Carrier Field Troubleshooting Protocol"
            ),
            "Weak Airflow at Supply Registers": s_dirty_filter,
            "Standing Water Around Air Handler": s_drain_clog
        }
    )

    return TroubleshootingNode(
        "Select Equipment Configuration:",
        options={
            "Central AC / Heat Pump / Package Unit": n_carrier_central,
            "Ductless Mini-Split / Multi-Split": n_carrier_minisplit,
            "Lookup by Specific Fault Code": n_carrier_codes
        }
    )

# Session State Initialization
if "history" not in st.session_state:
    st.session_state.history = []

root_node = build_professional_carrier_tree()

if "current_node" not in st.session_state:
    st.session_state.current_node = root_node

current_node = st.session_state.current_node

# Sidebar Configuration
with st.sidebar:
    st.markdown("### 🏢 ANRML Facility Operations")
    st.caption("Industrial Maintenance Division")
    st.divider()
    
    # Progress Tracker
    depth = len(st.session_state.history) + 1
    st.markdown(f"**Diagnostic Depth:** Level {depth}")
    st.progress(min(depth * 33, 100))
    st.divider()
    
    st.markdown("### 👨‍💻 System Architecture")
    st.markdown("""
    **Developer:** Thomarg Technologies  
    **Architect:** James Thomas Ijimari  
    **Standards:** Carrier Factory Manuals
    """)

# Navigation Breadcrumb
if st.session_state.history:
    st.markdown(f"""
        <div class="breadcrumb-bar">
            📍 Step {len(st.session_state.history) + 1} of Diagnostic Decision Path
        </div>
    """, unsafe_allow_html=True)

# Main Prompt / Title
st.markdown(f"### {current_node.question_or_result}")

def select_option(next_node):
    st.session_state.history.append(st.session_state.current_node)
    st.session_state.current_node = next_node

def go_back():
    if st.session_state.history:
        st.session_state.current_node = st.session_state.history.pop()

def restart():
    st.session_state.history.clear()
    st.session_state.current_node = root_node

# Render Node Body
if current_node.is_leaf():
    st.markdown(f"""
    <div class="solution-card">
        <div class="solution-title">📋 Recommended Technical Procedure</div>
        <div class="solution-text">{current_node.solution}</div>
    </div>
    """, unsafe_allow_html=True)

    if current_node.manual_ref:
        st.info(f"📖 **Manual Reference:** {current_node.manual_ref}")

    if current_node.professional_needed:
        st.markdown("""
        <div class="safety-card">
            <div class="safety-title">⚠️ CERTIFIED TECHNICIAN REQUIRED</div>
            <p class="safety-desc">
                High-voltage isolation or refrigerant handling required. Strictly adhere to ANRML Lockout/Tagout (LOTO) protocols.
            </p>
        </div>
        """, unsafe_allow_html=True)
else:
    for option_text, next_node in current_node.options.items():
        st.button(option_text, on_click=select_option, args=(next_node,))

st.divider()

# Navigation Controls
col1, col2 = st.columns(2)
with col1:
    if len(st.session_state.history) > 0:
        st.button("← Previous Step", on_click=go_back)
with col2:
    st.button("Reset Diagnostic Tree ↻", on_click=restart)
    
