from client import AiCustomerHealthScoreChurnPredictorClient

def main():
    client = AiCustomerHealthScoreChurnPredictorClient()
    signals = {'dau_mau': 0.31, 'features_used': 3, 'tickets_30d': 12, 'last_login_days': 11}
    res = client.score_account('ACC-44821', signals)
    print('Account: ' + res['account_id'])
    print('Health Score: ' + str(res['health_score']) + '/100 | Churn Risk: ' + res['churn_risk'])
    print('Churn Probability: ' + str(res['churn_probability_pct']) + '%')
    print('Playbook: ' + res['recommended_playbook'])
    print('Health Signals:')
    for s in res['health_signals']:
        print('  [' + s['status'] + '] ' + s['signal'] + ': ' + str(s['value']) + ' (benchmark: ' + str(s['benchmark']) + ')')

if __name__ == '__main__':
    main()
