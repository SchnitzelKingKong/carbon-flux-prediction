"""
Extract ablation results from Chapter 7 output and create JSON file for Chapter 7.1
"""
import json
from pathlib import Path

# Data extracted from Chapter 7 execution output
ablation_results = [
    {
        "epochs": 8,
        "best_val_loss": 0.8052,
        "best_epoch": 2,
        "final_train_loss": None,  # Not in output
        "final_train_acc": None,
        "final_val_loss": None,
        "final_val_acc": 0.7441,
        "final_val_macro_f1": 0.7220,
        "final_val_bal_acc": None,
        "checkpoint": "3_Model\\checkpoints\\finetune_best_ep8.keras"
    },
    {
        "epochs": 12,
        "best_val_loss": 0.8115,
        "best_epoch": 2,
        "final_train_loss": None,
        "final_train_acc": None,
        "final_val_loss": None,
        "final_val_acc": 0.7460,
        "final_val_macro_f1": 0.7269,
        "final_val_bal_acc": None,
        "checkpoint": "3_Model\\checkpoints\\finetune_best_ep12.keras"
    },
    {
        "epochs": 15,
        "best_val_loss": 0.8084,
        "best_epoch": 2,
        "final_train_loss": None,
        "final_train_acc": None,
        "final_val_loss": None,
        "final_val_acc": 0.7526,
        "final_val_macro_f1": 0.7317,
        "final_val_bal_acc": None,
        "checkpoint": "3_Model\\checkpoints\\finetune_best_ep15.keras"
    }
]

# Best overall is epochs=8 according to output
best_overall = ablation_results[0].copy()
best_overall["final_train_loss"] = 0.2430
best_overall["final_train_acc"] = None  # Not in output
best_overall["final_val_loss"] = 0.8052
best_overall["final_val_acc"] = None  # Not in output (but we have 0.7441 from ablation)
best_overall["final_val_macro_f1"] = 0.7290
best_overall["final_val_bal_acc"] = 0.7227

results_data = {
    "ablation_results": ablation_results,
    "best_overall": best_overall,
    "y_val_true": None,  # Will need to be regenerated if needed
    "y_val_pred": None   # Will need to be regenerated if needed
}

# Save to JSON
checkpoint_dir = Path("3_Model") / "checkpoints"
checkpoint_dir.mkdir(parents=True, exist_ok=True)
results_path = checkpoint_dir / "ablation_results.json"

with open(results_path, 'w') as f:
    json.dump(results_data, f, indent=2)

print(f"✅ Ablation results saved to: {results_path}")
print(f"\nBest model: {best_overall['epochs']} epochs")
print(f"  Val Loss: {best_overall['best_val_loss']:.4f}")
print(f"  Val Macro F1: {best_overall['final_val_macro_f1']:.4f}")
print(f"  Checkpoint: {best_overall['checkpoint']}")
