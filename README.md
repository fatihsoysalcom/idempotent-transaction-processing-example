# Idempotent Transaction Processing Example

This Python example demonstrates the concept of idempotency in transaction processing. It simulates a simple financial deposit operation that uses an 'idempotency key' to ensure that even if the same request is received multiple times, the underlying account balance is updated only once, preventing duplicate state changes. This highlights how idempotency acts as a contract for consistent system state.

## Language

`python`

## How to Run

Save the code as `main.py`.
Run from your terminal: `python main.py`

## Original Article

This example accompanies the Turkish article: [İdempotans Bir Anahtar Değil, Bir Sözleşmedir: Neden Önemli?](https://fatihsoysal.com/blog/idempotans-bir-anahtar-degil-bir-sozlesmedir-neden-onemli/).

## License

MIT — see [LICENSE](LICENSE).
