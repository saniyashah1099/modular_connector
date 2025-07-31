from symbol_mapper import SymbolMapper

mapper = SymbolMapper()

examples = [
    "BONKUSDT",
    "1000BONK-USD",
    "BONK-USD",
    "BTCUSDC",
    "ETH_XBT"
]

for raw in examples:
    print(f"{raw}  →  {mapper.normalize_symbol(raw)}")
