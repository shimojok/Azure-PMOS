import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="Azure-PMOS Executive", layout="wide")
    
    # サイドバーで言語選択
    st.sidebar.title("🌐 Azure-PMOS")
    lang = st.sidebar.selectbox("Language / 言語", ["en", "ja"])
    st.sidebar.markdown("---")
    st.sidebar.write("Strategic OS for Planetary Metabolism")

    # 言語リソースの定義
    texts = {
        "en": {
            "title": "Azure-PMOS: Executive Decision Support",
            "tab1": "AGRIX (Eco-Control)",
            "tab2": "HealthBook (Metabolic)",
            "tab3": "Strategic Impact",
            "tab4": "Iwanuma Evidence",
            "agrix_h": "AGRIX: Soil Ecological Control",
            "area": "Cultivation Area (ha)",
            "mbt_toggle": "Activate MBT55 (5x Yield Boost)",
            "impact_label": "Economic Impact (Annual)",
            "status_active": "24h Waste-to-Resource & Bio-Security: ACTIVE",
            "hb_h": "HealthBook: Metabolic Intelligence",
            "hb_desc": "200-Question Matrix x 137 Disease Models x 293 Formula Library",
            "run_btn": "Run Diagnostic Analysis",
            "ma_h": "M&A Strategic Value / Market Cap Prediction",
            "iw_h": "Proven Results: Iwanuma Legacy (2011)"
        },
        "ja": {
            "title": "Azure-PMOS: 経営意思決定支援ダッシュボード",
            "tab1": "AGRIX (土壌生態制御)",
            "tab2": "HealthBook (代謝解析)",
            "tab3": "戦略的インパクト",
            "tab4": "岩沼の実績 (エビデンス)",
            "agrix_h": "AGRIX: 土壌生態制御システム",
            "area": "耕作面積 (ha)",
            "mbt_toggle": "MBT55起動 (収穫量5倍ブースト)",
            "impact_label": "年間経済インパクト",
            "status_active": "24時間資源化 & バイオセキュリティ: 稼働中",
            "hb_h": "HealthBook: 代謝インテリジェンス",
            "hb_desc": "200問診 × 137疾病マトリックス × 293漢方ライブラリ",
            "run_btn": "診断・解析デモ実行",
            "ma_h": "M&A戦略価値 / 時価総額予測",
            "iw_h": "実証済み成果: 岩沼レガシー (東日本大震災)"
        }
    }

    t = texts[lang]

    # メイン表示
    st.title(t["title"])
    st.markdown("---")

    tab1, tab2, tab3, tab4 = st.tabs([t["tab1"], t["tab2"], t["tab3"], t["tab4"]])

    # --- AGRIX ---
    with tab1:
        st.header(t["agrix_h"])
        col1, col2 = st.columns([1, 2])
        with col1:
            ha = st.number_input(t["area"], value=1000)
            mbt = st.toggle(t["mbt_toggle"], value=True)
            yield_val = 5.0 if mbt else 1.0
        with col2:
            impact = ha * 4000 * yield_val
            st.metric(t["impact_label"], f"${impact:,.0f}")
            st.success("✅ Negative Green Premium Achieved" if mbt else "Traditional Model")
            st.info(t["status_active"])

    # --- HealthBook ---
    with tab2:
        st.header(t["hb_h"])
        st.write(t["hb_desc"])
        if st.button(t["run_btn"]):
            st.success("✅ Analysis Complete" if lang=="en" else "✅ 解析完了")
            st.json({"Status": "Optimal", "Target": "Mitochondrial Activation", "Formula": "MBT_Custom_042"})

    # --- Strategic Impact ---
    with tab3:
        st.header(t["ma_h"])
        df = pd.DataFrame({
            "Entity": ["Microsoft (Azure)", "Yara International", "Gates Foundation"],
            "Value Impact": ["+$300B - $400B", "5.5x Growth", "510M Tons GHG Red."],
            "Logic": ["Planetary OS Monopoly", "Waste-to-Asset", "Carbon Neutrality"]
        })
        st.table(df)

    # --- Tab 4: Iwanuma Evidence (Reliable Link Version) ---
    with tab4:
        st.header(t["iw_h"])
        
        # YouTubeのサムネイル画像をボタンとして配置
        video_id = "urH8fNTZQ2Q"
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        watch_url = f"https://www.youtube.com/watch?v={video_id}"
        
        st.write("### 🎬 Evidence: 1-Week Transformation (2011)")
        
        # 画像をクリックすると動画へ飛ぶリンク（確実な方法）
        st.markdown(f'''
            <a href="{watch_url}" target="_blank">
                <img src="{thumbnail_url}" style="width:100%; border-radius:10px; border: 2px solid #0078D4;">
            </a>
            <p style="text-align:center; color:#0078D4; font-weight:bold;">
                👉 Click to play video in a new tab / クリックして動画を再生
            </p>
        ''', unsafe_allow_html=True)
        
        st.markdown("---")
        st.success("Result: Transformation of toxic sludge into bio-fertilizer." if lang=="en" else "実績：震災汚泥を1週間で無害化・肥料化。")
        st.write("This evidence proves the MBT logic can modulate planetary-scale waste into vital resources." if lang=="en" else "この実績は、MBTロジックが地球規模の廃棄物を資源に変える力を持つことを証明しています。")

if __name__ == "__main__":
    main()
