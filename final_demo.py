cat << 'EOF' > final_demo.py
import streamlit as st
import pandas as pd

# 下條さんのロジックを統合した単一ファイル
def main():
    st.set_page_config(page_title="Azure-PMOS Executive", layout="wide")
    st.sidebar.title("🌐 Azure-PMOS")
    lang = st.sidebar.selectbox("Language / 言語", ["ja", "en"])
    
    title = "Azure-PMOS: 経営意思決定支援" if lang == 'ja' else "Azure-PMOS: Executive Decision Support"
    st.title(title)
    st.markdown("---")

    tab1, tab2, tab3, tab4 = st.tabs(["AGRIX", "HealthBook", "Strategic Impact", "Iwanuma Evidence"])

    with tab1:
        st.header("AGRIX: 土壌生態制御 (Soil Ecological Control)")
        col1, col2 = st.columns([1, 2])
        with col1:
            ha = st.number_input("面積 / Area (ha)", value=1000)
            mbt = st.toggle("MBT55 (5x Yield Boost)", value=True)
            yield_val = 5.0 if mbt else 1.0
        with col2:
            impact = ha * 4000 * yield_val
            st.metric("経済インパクト / Economic Impact", f"${impact:,.0f}")
            st.success("✅ Negative Green Premium Achieved" if mbt else "Traditional")

    with tab2:
        st.header("HealthBook: 代謝インテリジェンス")
        st.write("200問診 × 137疾病マトリックス × 293漢方ライブラリ")
        if st.button("分析デモ実行 / Run Analysis"):
            st.json({"Status": "Optimal", "Target": "Mitochondrial Activation"})

    with tab3:
        st.header("M&A Strategy / 時価総額予測")
        df = pd.DataFrame({
            "Entity": ["Microsoft", "Yara International"],
            "Value": ["+$300B - $400B", "5.5x Growth"],
            "Logic": ["Ecological Data Monopoly", "Waste-to-Asset"]
        })
        st.table(df)

    with tab4:
        st.header("Proven Results: 岩沼の実績")
        st.video("https://www.youtube.com/watch?v=urH8fNTZQ2Q")

if __name__ == "__main__":
    main()
EOF
