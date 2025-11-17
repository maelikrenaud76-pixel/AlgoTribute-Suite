AlgoTribute — Finance Quantitative Utility Suite

Une suite de 4 outils Python indépendants, pratiques et simples, dédiés à l’analyse financière, l’optimisation et les tests de robustesse.
Pensé comme un hommage aux outils quantitatifs classiques, mais version light & fun.

📌 Contenu de la suite

AlgoTribute contient 4 modules autonomes, chacun avec une fonction financière utile :

🔍 1. AlgoTribute_FundamentalAnalyzer.py

Analyse fondamentale simple :

Télécharge les données financières d’une entreprise

Analyse ratios clés (PER, PEG, ROE, dette, etc.)

Renvoie un diagnostic basique (bon/moyen/mauvais)

📊 2. AlgoTribute_PortfolioOptimizer.py

Optimiseur de portefeuille :

Récupère les prix de plusieurs tickers

Calcule rendements + risque (variance, covariance)

Génère pondérations optimales (allocation équilibrée)

Version simple et rapide (sans CVXPY)

📈 3. AlgoTribute_Screener.py

Stock screener simple :

Liste de tickers US

Télécharge les données

Cherche momentum, variation 30 jours, variation 1 an

Classement des meilleures opportunités du moment

⚠️ 4. AlgoTribute_StressTest.py

Stress-test rapide sur 3 scénarios :

Crash (–20 %)

Boom (+15 %)

Volatilité extrême
Donne le comportement attendu d’un portefeuille (effet choc).
