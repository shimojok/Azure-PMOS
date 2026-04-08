import json
import os

class MetabolicIntelligence:
    """
    HealthBook Metabolic Intelligence (MI) Engine.
    Analyzes 200 questions to identify metabolic bottlenecks.
    """
    def __init__(self, lang='en'):
        self.lang = lang
        self.data_path = f"../data/questionnaire_200_{lang}.json"
        self.library_path = "../data/mbt_kampo_library.json"
        
        # Load datasets
        with open(self.data_path, 'r', encoding='utf-8') as f:
            self.questions = json.load(f)['questions']
        with open(self.library_path, 'r', encoding='utf-8') as f:
            self.kampo_library = json.load(f)['formulas']

    def analyze(self, responses):
        """
        responses: dict { "1": True, "2": False, ... }
        """
        scores = {}
        for q_id, val in responses.items():
            if val and q_id in self.questions:
                q = self.questions[q_id]
                weight = q.get('weight', 0.5)
                for disease in q.get('related_diseases', []):
                    scores[disease] = scores.get(disease, 0) + weight
        
        # Ranking top 3 risks
        sorted_risks = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
        return self._format_results(sorted_risks)

    def _format_results(self, risks):
        results = []
        for risk, score in risks:
            # Match with Kampo library phytochemicals
            matched_formula = self._find_best_formula(risk)
            results.append({
                "risk": risk,
                "score": round(score, 2),
                "intervention": matched_formula
            })
        return results

    def _find_best_formula(self, risk_key):
        # Simplified matching logic for the prototype
        for formula in self.kampo_library:
            if any(risk_key in str(ind).lower() for ind in formula['indications']['primary']):
                return formula['name']
        return "Custom MBT Probiotics Formulation"

# Usage: mi_engine = MetabolicIntelligence(lang='en')
