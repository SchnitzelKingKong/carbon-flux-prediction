
# 1. Feature Reduktion
# Nur die Top 100-150 Features verwenden (nicht alle 680)
top_features = feat_imp.head(150)["Feature"].tolist()
X_train_reduced = X_train_balanced[top_features]
X_test_reduced = X_test[top_features]

# 2. Regularisierung verstärken
rf_improved = RandomForestClassifier(
    n_estimators=300,      # Reduziert von 500
    max_depth=15,          # Baum-Tiefe begrenzen
    min_samples_split=10,  # Minimum Samples pro Split
    min_samples_leaf=5,    # Minimum Samples pro Blatt
    max_features='sqrt',   # Feature-Sampling reduzieren
    random_state=42,
    class_weight="balanced"
)

# 3. Cross-Validation statt nur Train/Test
from sklearn.model_selection import cross_validate
scores = cross_validate(rf_improved, X_train_reduced, y_train_balanced, 
                        cv=5, scoring='f1_macro')
print("CV F1 Macro:", scores['test_score'].mean())

# 4. Balancing-Strategie überdenken
# Besser: SMOTE statt Undersampling/Oversampling
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42, k_neighbors=5)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)


# 5. use XGboost as model
