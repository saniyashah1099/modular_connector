import re

class SymbolMapper:
    def __init__(self):
        # Define known stablecoin variations
        self.quote_map = {
            "USD": ["USD", "USDT", "USDC", "BUSD", "TUSD"],
            "BTC": ["BTC", "XBT"],
            "ETH": ["ETH"]
        }

    def normalize_symbol(self, symbol: str) -> str:
        """
        Convert a symbol like '1000BONK-USD', 'BONKUSDT', 'BONK-USD' to 'BONK/USD'
        """
        # Clean and unify delimiters
        symbol = symbol.upper().replace("_", "-").replace("/", "-")

        # Extract alphanumeric tokens
        parts = re.findall(r"[A-Z0-9]+", symbol)

        # Try every possible 2-part split and test for valid quote
        for i in range(1, len(parts)):
            base = "".join(parts[:i])
            quote = "".join(parts[i:])
            standard_quote = self._map_quote(quote)
            if standard_quote:
                return f"{base}/{standard_quote}"

        # If no mapping found, return raw with placeholder
        return f"{symbol}/UNKNOWN"

    def _map_quote(self, quote: str) -> str:
        """
        Map a quote currency to a standard version.
        """
        for standard, variants in self.quote_map.items():
            if quote in variants:
                return standard
        return None
