import time
import random

# Simulate a database of account balances
accounts = {
    "user123": 100.0,
    "user456": 50.0
}

# Simulate a transaction log for idempotency keys.
# This set stores keys of transactions that have successfully modified the state.
# It acts as the "contract" ensuring a transaction's effect is applied only once.
processed_transactions = set()

def process_deposit(account_id: str, amount: float, idempotency_key: str) -> dict:
    """
    Processes a deposit transaction idempotently.
    Ensures that a transaction with the same idempotency_key is processed only once.
    """
    print(f"\n--- Attempting to process transaction for {account_id} with key '{idempotency_key}' ---")
    print(f"  Current balance for {account_id}: {accounts.get(account_id, 0.0)}")

    # 1. Idempotency check: Has this key been processed before?
    # If the key is found, it means the state change has already occurred.
    if idempotency_key in processed_transactions:
        print(f"  [IDEMPOTENT] Transaction with key '{idempotency_key}' already processed. Skipping state change.")
        return {"status": "success", "message": "Transaction already processed (idempotent).", "new_balance": accounts.get(account_id)}

    # Simulate potential network delay or processing time
    time.sleep(random.uniform(0.1, 0.5))

    # 2. Actual state change (if not processed yet)
    if account_id not in accounts:
        accounts[account_id] = 0.0
    
    accounts[account_id] += amount
    
    # 3. Record the idempotency key *after* successful state change.
    # This marks the transaction as completed and prevents future duplicates.
    processed_transactions.add(idempotency_key)
    
    print(f"  [PROCESSED] Successfully deposited {amount} to {account_id}. New balance: {accounts[account_id]}")
    return {"status": "success", "message": "Transaction processed.", "new_balance": accounts[account_id]}

# --- Demonstration ---
print("Initial account balances:", accounts)

# Scenario 1: A single successful deposit
print("\n--- Scenario 1: Single successful deposit ---")
process_deposit("user123", 20.0, "txn_abc_1")
print("Balances after Scenario 1:", accounts)

# Scenario 2: Simulate a retry for the *same* transaction (same idempotency key)
# The idempotency mechanism should prevent a duplicate update.
print("\n--- Scenario 2: Retrying the same deposit (should be idempotent) ---")
process_deposit("user123", 20.0, "txn_abc_1") 
print("Balances after Scenario 2 (retry):", accounts)

# Scenario 3: Another unique deposit for a different user
print("\n--- Scenario 3: Another unique deposit ---")
process_deposit("user456", 10.0, "txn_def_2")
print("Balances after Scenario 3:", accounts)

# Scenario 4: Simulate multiple retries for a new transaction
# Only the first attempt should cause a state change.
print("\n--- Scenario 4: Multiple retries for a new transaction ---")
process_deposit("user123", 5.0, "txn_ghi_3")
process_deposit("user123", 5.0, "txn_ghi_3") # Retry 1
process_deposit("user123", 5.0, "txn_ghi_3") # Retry 2
print("Balances after Scenario 4 (multiple retries):", accounts)

print("\nFinal account balances:", accounts)
print("Processed transaction keys:", processed_transactions)
