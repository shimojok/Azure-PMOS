import streamlit as st
import sys
import os
import pandas as pd

# --- パス設定の修正 ---
# 現在のファイル(app.py)から見て、プロジェクトのルート(Azure-PMOS)を探し、パスに追加します
current_dir = os.path.dirname(os.path.abspath(__file__)) # dashboard
project_root = os.path.abspath(os.path.join(current_dir, "../../")) # Azure-PMOS
sys.path.append(project_root)

# 各プラットフォームのsrcフォルダを明示的に追加
sys.path.append(os.path.join(project_root, "01_AGRIX_Platform/src"))
sys.path.append(os.path.join(project_root, "02_HealthBook_Platform/src"))

# --- エンジンのインポート試行 ---
try:
    # フォルダ構成に基づいてインポート
    from agrix_simulator import AGRIXEconomicEngine
    from metabolic_intelligence import MetabolicIntelligence
    engine_loaded = True
except ImportError as e:
    st.error(f"Engine Import Error: {e}")
    engine_loaded = False

def main():
    st.set_page_config(page_title="Azure-PMOS Management Console", layout="wide")
    
    lang = st.sidebar.selectbox("Language / 言語", ["en", "ja"])
    st.sidebar.markdown("---")
    st.sidebar.write("Project: **Azure-PMOS**")
    st.sidebar.write("Strategic Value: **Planetary Sustainability**")

    title = "Azure-PMOS: Executive Decision Support" if lang == 'en' else "Azure-PMOS: 経営意思決定支援ダッシュボード"
    st.title(f"🌐 {title}")

    if not engine_loaded:
        st.warning("Engines are not loaded. Please ensure agrix_simulator.py and metabolic_intelligence.py exist in their respective src folders.")
        return

    tab1, tab2, tab3 = st.tabs(["AGRIX (Environment)", "HealthBook (Metabolic)", "M&A Impact"])

    # --- Tab 1: AGRIX ---
    with tab1:
        st.header("AGRIX: Soil & Carbon Finance")
        col1, col2 = st.columns([1, 2])
        with col1:
            crop = st.selectbox("Industry Sector", ["Coffee", "Rice", "Cacao", "Wheat"])
            hectares = st.number_input("Cultivation Area (ha)", value=1000)
            c_price = st.slider("Carbon Price (USD/tCO2e)", 50, 200, 100)
        
        # ここで正しくクラスを呼び出し
        engine = AGRIXEconomicEngine(lang=lang)
        carbon_seq = hectares * 10.95
        total_profit = engine.run_simulation(crop, hectares, 4000, carbon_price=c_price)
        
        with col2:
            st.metric("Total Economic Impact (Annual)", f"${total_profit:,.0f}")
            st.bar_chart(pd.DataFrame({
                "Category": ["Carbon Asset", "Yield Increase", "Risk Avoidance"],
                "Value": [carbon_seq * c_price, hectares * 4000 * 0.225, (hectares * 4000 * 0.16 if crop == "Coffee" else 0)]
            }).set_index("Category"))

    # --- Tab 2: HealthBook ---
    with tab2:
        st.header("HealthBook: Metabolic Intelligence")
        if st.button("Run MI Analysis Demo"):
            mi_engine = MetabolicIntelligence(lang=lang)
            st.success("Connected to 137 Disease Matrix & 293 Formula Library.")
            st.info("Demo: Predicting Optimization Pathway...")

if __name__ == "__main__":
    main()
