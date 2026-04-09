import json
import os

class MetabolicIntelligence:
    """
    HealthBook Metabolic Intelligence (MI) Engine - Full Implementation
    30万人の臨床知見に基づき、200問診から137疾病リスクを推論する。
    """
    def __init__(self, lang='ja'):
        self.lang = lang
        # ファイルパスの定義
        data_dir = os.path.join(os.path.dirname(__file__), '../data')
        
        self.paths = {
            'questions': f"{data_dir}/questionnaire_200_{lang}.json",
            'matrix': f"{data_dir}/disease_matrix_137_en.json",
            'library': f"{data_dir}/mbt_kampo_library.json" # 明日日英版へ差し替え
        }
        self.load_all_data()

    def load_all_data(self):
        with open(self.paths['questions'], 'r', encoding='utf-8') as f:
            self.questions_data = json.load(f)['questions']
        with open(self.paths['matrix'], 'r', encoding='utf-8') as f:
            self.matrix_data = json.load(f)['matrix']
        with open(self.paths['library'], 'r', encoding='utf-8') as f:
            self.kampo_library = json.load(f)['formulas']

    def analyze(self, user_responses):
        """
        user_responses: { "Q001": True, "Q005": False, ... }
        """
        # 1. 疾病ごとの累積スコア計算
        disease_scores = {disease: 0.0 for disease in self.matrix_data.keys()}

        for q_id, answered_yes in user_responses.items():
            if answered_yes and q_id in self.questions_data:
                # 各質問が持つ疾病への重み付け(Weight)を反映
                relevant_impacts = self.questions_data[q_id].get('impacts', {})
                for disease, weight in relevant_impacts.items():
                    if disease in disease_scores:
                        disease_scores[disease] += weight

        # 2. スコアの高い順にソート (Top 5)
        top_risks = sorted(disease_scores.items(), key=lambda x: x[1], reverse=True)[:5]
        
        # 3. 解決策（漢方・ファイトケミカル）のマッピング
        return self._build_report(top_risks)

    def _build_report(self, top_risks):
        report = []
        for disease, score in top_risks:
            # 疾病に関連する代謝経路(Pathways)をマトリックスから取得
            pathways = self.matrix_data.get(disease, {}).get('pathways', [])
            
            # ライブラリーから最適な処方を検索
            recommendation = self._match_library(disease, pathways)
            
            report.append({
                "disease_risk": disease,
                "confidence_score": round(score, 2),
                "affected_pathways": pathways,
                "suggested_solution": recommendation
            })
        return report

    def _match_library(self, disease, pathways):
        # 代謝経路または疾病名でライブラリーと照合
        for formula in self.kampo_library:
            if disease in formula['indications']['primary'] or \
               any(p in formula['formula_synergy']['primary_pathway'] for p in pathways):
                return {
                    "name": formula['name'],
                    "components": formula['components'],
                    "mechanism": formula['formula_synergy']
                }
        return "Custom MBT Probiotics Formulation Required"
