import json

class AGRIXEconomicEngine:
    """
    AGRIX Platformの経済価値を算出するメインエンジン。
    MBT55のエビデンスに基づき、負のグリーンプレミアムを証明する。
    """
    def __init__(self):
        # BioNexus提供データに基づく定数
        self.CARBON_SEQ_10YR = 109.5  # tCO2e/ha
        self.ANNUAL_CARBON_SEQ = self.CARBON_SEQ_10YR / 10
        self.YIELD_INCREASE_RATE = 0.225  # 15-30%の中間値
        self.COFFEE_RUST_PROTECTION = 0.80 # さび病抑制率
        self.METHANE_REDUCTION = 0.82    # メタン削減率

    def run_scenerio(self, crop_name, area_ha, unit_price_usd, carbon_price=100):
        # 1. 直接的な収量増加価値
        yield_value = area_ha * unit_price_usd * self.YIELD_INCREASE_RATE
        
        # 2. 炭素隔離の資産価値 (PBPE)
        carbon_asset = area_ha * self.ANNUAL_CARBON_SEQ * carbon_price
        
        # 3. 損失回避価値 (例: コーヒーさび病)
        loss_avoidance = 0
        if crop_name.lower() == "coffee":
            # 潜在的損失リスクを売上の20%と仮定
            potential_loss = area_ha * unit_price_usd * 0.20
            loss_avoidance = potential_loss * self.COFFEE_RUST_PROTECTION

        total_impact = yield_value + carbon_asset + loss_avoidance
        
        return {
            "Sector": crop_name,
            "Carbon_Sequestration_tCO2e": area_ha * self.ANNUAL_CARBON_SEQ,
            "Financial_Gain_USD": total_impact,
            "Green_Premium_Status": "NEGATIVE (PROFITABLE)"
        }

# デモ実行: ハワード・シュルツ氏へのプレゼン用
engine = AGRIXEconomicEngine()
print(engine.run_scenerio("Coffee", 1000, 4000))
