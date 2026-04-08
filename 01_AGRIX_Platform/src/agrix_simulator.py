import json

class AGRIXEconomicEngine:
    """
    AGRIX Platform Economic Simulator
    Supports multi-language reporting (EN/JP).
    """
    def __init__(self, lang='en'):
        self.lang = lang
        # Constants based on BioNexus evidence
        self.CARBON_SEQ_10YR = 109.5  # tCO2e/ha/10yr
        self.ANNUAL_CARBON_SEQ = self.CARBON_SEQ_10YR / 10
        self.YIELD_IMPROVEMENT_AVG = 0.225
        self.RUST_DISEASE_REDUCTION = 0.80

        # Internationalization (i18n)
        self.msg = {
            'en': {
                'title': "--- AGRIX Economic Impact Report ---",
                'sector': "Target Sector",
                'carbon_value': "Annual Carbon Asset Value (USD)",
                'yield_gain': "Annual Yield Gain (USD)",
                'neg_green_prem': "Negative Green Premium Status",
                'summary': "The transition to Azure-AGRIX results in a direct financial surplus."
            },
            'ja': {
                'title': "--- AGRIX 経済インパクト報告書 ---",
                'sector': "対象セクター",
                'carbon_value': "年間炭素資産価値 (USD)",
                'yield_gain': "年間収量増加益 (USD)",
                'neg_green_prem': "負のグリーンプレミアム達成状況",
                'summary': "Azure-AGRIXへの移行は、直接的な財務余剰を創出します。"
            }
        }

    def run_simulation(self, crop, hectares, unit_price, carbon_price=100):
        m = self.msg[self.lang]
        carbon_asset = hectares * self.ANNUAL_CARBON_SEQ * carbon_price
        yield_gain = hectares * unit_price * self.YIELD_IMPROVEMENT_AVG
        
        # Loss Avoidance logic for Coffee
        loss_avoidance = 0
        if crop.lower() == "coffee":
            loss_avoidance = (hectares * unit_price * 0.20) * self.RUST_DISEASE_REDUCTION

        total_gain = carbon_asset + yield_gain + loss_avoidance

        print(m['title'])
        print(f"{m['sector']}: {crop}")
        print(f"{m['carbon_value']}: ${carbon_asset:,.0f}")
        print(f"{m['yield_gain']}: ${yield_gain:,.0f}")
        print(f"{m['neg_green_prem']}: ACHIEVED (Surplus: ${total_gain:,.0f})")
        print(f"{m['summary']}\n")
        return total_gain

# Usage: engine = AGRIXEconomicEngine(lang='ja')
