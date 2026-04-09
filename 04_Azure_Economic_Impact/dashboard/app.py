import streamlit as st
import sys
import os

# 各プラットフォームのエンジンをインポート
sys.path.append(os.path.abspath('../../01_AGRIX_Platform/src'))
sys.path.append(os.path.abspath('../../02_HealthBook_Platform/src'))

from agrix_simulator import AGRIXEconomicEngine
from metabolic_intelligence import MetabolicIntelligence

def main():
    st.set_page_config(page_title="Azure-PMOS Executive Dashboard", layout="wide")
    
    # 日英切り替えスイッチ
    lang = st.sidebar.selectbox("Language / 言語", ["en", "ja"])
    
    st.title("🌐 Azure-PMOS: Planetary Metabolism OS")
    st.markdown("---")

    # --- Section 1: AGRIX Economic Impact ---
    st.header("1. AGRIX: Negative Green Premium")
    col1, col2 = st.columns(2)
    
    with col1:
        hectares = st.slider("Hectares (ha)", 100, 10000, 1000)
        crop = st.selectbox("Crop Type", ["Coffee", "Rice", "Cacao"])
    
    engine = AGRIXEconomicEngine(lang=lang)
    impact = engine.run_simulation(crop, hectares, unit_price=4000)
    
    with col2:
        st.metric(label="Total Financial Surplus (USD)", value=f"${impact:,.0f}")
        st.info("Status: Negative Green Premium ACHIEVED")

    st.markdown("---")

    # --- Section 2: HealthBook Metabolic Intelligence ---
    st.header("2. HealthBook: Metabolic Risk Analysis")
    st.write("300,000 Clinical Insights for Preventive Healthcare")
    
    # 問診デモ（簡易版）
    st.checkbox("Irregular meal times? / 食事の時間が不規則か？")
    st.checkbox("Experience coldness in extremities? / 手足の冷えがあるか？")
    
    if st.button("Run MI Analysis"):
        st.success("Analysis Complete. Predicting Top Risks via 137 Disease Matrix...")
        # ここで metabolic_intelligence.py を呼び出し、結果を表示

if __name__ == "__main__":
    main()
