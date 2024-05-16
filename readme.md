# Price Indices Package

## Overview

This package provides functions to calculate various price indices, including both unweighted and weighted methods. The package includes native Python implementations as well as pandas DataFrame-based implementations for flexible data handling.

## Features

### Unweighted Methods:
- **Jevons Index**
- **Dutot Index**
- **Carli Index**
- **Balk-Mehrhoff-Walsh (BMW) Index**

### Weighted Methods:
- **Laspeyres Index**
- **Paasche Index**
- **Fisher Index**
- **Törnqvist Index**
- **Walsh Index**
- **Sato-Vartia Index**

## Installation

To install the package, you can use the following command:

```bash
pip install price_indices
```

## Constants

The following constants are used in the package:

- `PD_DEFAULT_PRICE_COL`: Default column name for prices in DataFrame.
- `PD_DEFAULT_PRODUCT_ID_COL`: Default column name for product IDs in DataFrame.
- `PD_DEFAULT_QUANTITY_COL`: Default column name for quantities in DataFrame.
- `PD_DEFAULT_TIME_PERIOD_COL`: Default column name for time periods in DataFrame.
- `DEFAULT_NORMALIZATION_VAL`: Default normalization value for indices.

## Functions

### Unweighted Methods (Native Python)

#### `jevons_index(prices_0: Dict[str, float], prices_t: Dict[str, float], normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Jevons price index.

#### `dutot_index(prices_0: Dict[str, float], prices_t: Dict[str, float], normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Dutot price index.

#### `carli_index(prices_0: Dict[str, float], prices_t: Dict[str, float], normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Carli price index.

#### `bmw_index(prices_0: Dict[str, float], prices_t: Dict[str, float], normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Balk-Mehrhoff-Walsh (BMW) price index.

### Unweighted Methods (pandas DataFrame)

#### `jevons_index_from_df(df: pd.DataFrame, base_period: int, compared_period: int, price_col: str = PD_DEFAULT_PRICE_COL, product_id_col: str = PD_DEFAULT_PRODUCT_ID_COL, time_period_col: str = PD_DEFAULT_TIME_PERIOD_COL, normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Jevons price index from a pandas DataFrame.

#### `dutot_index_from_df(df: pd.DataFrame, base_period: int, compared_period: int, price_col: str = PD_DEFAULT_PRICE_COL, product_id_col: str = PD_DEFAULT_PRODUCT_ID_COL, time_period_col: str = PD_DEFAULT_TIME_PERIOD_COL, normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Dutot price index from a pandas DataFrame.

#### `carli_index_from_df(df: pd.DataFrame, base_period: int, compared_period: int, price_col: str = PD_DEFAULT_PRICE_COL, product_id_col: str = PD_DEFAULT_PRODUCT_ID_COL, time_period_col: str = PD_DEFAULT_TIME_PERIOD_COL, normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Carli price index from a pandas DataFrame.

#### `bmw_index_from_df(df: pd.DataFrame, base_period: int, compared_period: int, price_col: str = PD_DEFAULT_PRICE_COL, product_id_col: str = PD_DEFAULT_PRODUCT_ID_COL, time_period_col: str = PD_DEFAULT_TIME_PERIOD_COL, normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Balk-Mehrhoff-Walsh (BMW) price index from a pandas DataFrame.

### Weighted Methods (Native Python)

#### `laspeyres_index(prices_0: Dict[str, float], prices_t: Dict[str, float], quantities_0: Dict[str, float], normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Laspeyres price index.

#### `paasche_index(prices_0: Dict[str, float], prices_t: Dict[str, float], quantities_t: Dict[str, float], normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Paasche price index.

#### `fisher_index(prices_0: Dict[str, float], prices_t: Dict[str, float], quantities_0: Dict[str, float], quantities_t: Dict[str, float], normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Fisher price index.

#### `tornqvist_index(prices_0: Dict[str, float], prices_t: Dict[str, float], quantities_0: Dict[str, float], quantities_t: Dict[str, float], normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Törnqvist price index.

#### `walsh_index(prices_0: Dict[str, float], prices_t: Dict[str, float], quantities_0: Dict[str, float], quantities_t: Dict[str, float], normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Walsh price index.

#### `sato_vartia_index(prices_0: Dict[str, float], prices_t: Dict[str, float], quantities_0: Dict[str, float], quantities_t: Dict[str, float], normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Sato-Vartia price index.

### Weighted Methods (pandas DataFrame)

#### `laspeyres_index_from_df(df: pd.DataFrame, base_period: int, compared_period: int, price_col: str = PD_DEFAULT_PRICE_COL, quantity_col: str = PD_DEFAULT_QUANTITY_COL, product_id_col: str = PD_DEFAULT_PRODUCT_ID_COL, time_period_col: str = PD_DEFAULT_TIME_PERIOD_COL, normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Laspeyres price index from a pandas DataFrame.

#### `paasche_index_from_df(df: pd.DataFrame, base_period: int, compared_period: int, price_col: str = PD_DEFAULT_PRICE_COL, quantity_col: str = PD_DEFAULT_QUANTITY_COL, product_id_col: str = PD_DEFAULT_PRODUCT_ID_COL, time_period_col: str = PD_DEFAULT_TIME_PERIOD_COL, normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Paasche price index from a pandas DataFrame.

#### `fisher_index_from_df(df: pd.DataFrame, base_period: int, compared_period: int, price_col: str = PD_DEFAULT_PRICE_COL, quantity_col: str = PD_DEFAULT_QUANTITY_COL, product_id_col: str = PD_DEFAULT_PRODUCT_ID_COL, time_period_col: str = PD_DEFAULT_TIME_PERIOD_COL, normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Fisher price index from a pandas DataFrame.

#### `tornqvist_index_from_df(df: pd.DataFrame, base_period: int, compared_period: int, price_col: str = PD_DEFAULT_PRICE_COL, quantity_col: str = PD_DEFAULT_QUANTITY_COL, product_id_col: str = PD_DEFAULT_PRODUCT_ID_COL, time_period_col: str = PD_DEFAULT_TIME_PERIOD_COL, normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Törnqvist price index from a pandas DataFrame.

#### `walsh_index_from_df(df: pd.DataFrame, base_period: int, compared_period: int, price_col: str = PD_DEFAULT_PRICE_COL, quantity_col: str = PD_DEFAULT_QUANTITY_COL, product_id_col: str = PD_DEFAULT_PRODUCT_ID_COL, time_period_col: str = PD_DEFAULT_TIME_PERIOD_COL, normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Walsh price index from a pandas DataFrame.

#### `sato_vartia_index_from_df(df: pd.DataFrame, base_period: int, compared_period: int, price_col: str = PD_DEFAULT_PRICE_COL, quantity_col: str = PD_DEFAULT_QUANTITY_COL, product_id_col: str = PD_DEFAULT_PRODUCT_ID_COL, time_period_col: str = PD_DEFAULT_TIME_PERIOD_COL, normalization_value: float = DEFAULT_NORMALIZATION_VAL) -> float`
Calculate the Sato-Vartia price index from a pandas DataFrame.

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

## Usage Examples

Here's a quick example of how to use the package:

```python
import pandas as pd
from price_indices import jevons_index, jevons_index_from_df, PD_DEFAULT_PRICE_COL, PD_DEFAULT_PRODUCT_ID_COL, PD_DEFAULT_TIME_PERIOD_COL, DEFAULT_NORMALIZATION_VAL

# Example data
data = {
    PD_DEFAULT_PRODUCT_ID_COL: ['product_1', 'product_2', 'product_3'] * 2,
    PD_DEFAULT_PRICE_COL: [100, 200, 300, 110, 190, 310],
    PD_DEFAULT_TIME_PERIOD_COL: [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)

# Calculate Jevons index using native Python function
prices_0 = {'product_1': 100, 'product_2': 200, 'product_3': 300}
prices_t = {'product_1': 110, 'product_2': 190, 'product_3': 310}
jevons_index_value = jevons_index(prices_0, prices_t, DEFAULT_NORMALIZATION_VAL)

# Calculate Jevons index using pandas DataFrame function
jevons_index_df_value = jevons_index_from_df(df, base_period=0, compared_period=1)

print("Jevons Index (native):", jevons_index_value)
print("Jevons Index (DataFrame):", jevons_index_df_value)
```
