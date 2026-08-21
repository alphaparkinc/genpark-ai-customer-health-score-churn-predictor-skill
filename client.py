class AiCustomerHealthScoreChurnPredictorClient:
    def score_account(self, account_id='ACC-001', usage_signals=None):
        usage_signals = usage_signals or {}
        signals = [
            {'signal': 'DAU/MAU ratio', 'value': 0.31, 'benchmark': 0.50, 'weight': 'HIGH', 'status': 'RED'},
            {'signal': 'Feature adoption depth', 'value': 3, 'benchmark': 7, 'weight': 'HIGH', 'status': 'YELLOW'},
            {'signal': 'Support ticket volume (30d)', 'value': 12, 'benchmark': 3, 'weight': 'MEDIUM', 'status': 'RED'},
            {'signal': 'Last login days ago', 'value': 11, 'benchmark': 3, 'weight': 'MEDIUM', 'status': 'YELLOW'}
        ]
        return {
            'account_id': account_id,
            'health_score': 38.2,
            'churn_risk': 'HIGH',
            'churn_probability_pct': 73.4,
            'health_signals': signals,
            'recommended_playbook': 'ESCALATE_TO_CSM_EBR_30_DAYS'
        }
