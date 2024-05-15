#!/usr/bin/env python
# coding: utf-8

# In[2]:


from typing import Dict
from math import sqrt, log, exp


# # Price Indices
#
# ## Bilateral Methods
#
# ### Unweighted Methods

# In[ ]:


def jevons_index(prices_0: Dict[str, float], prices_t: Dict[str, float]) -> float:
    """
    Calculate the Jevons price index.

    Args:
        prices_0 (Dict[str, float]): Prices of products at time 0.
        prices_t (Dict[str, float]): Prices of products at time t.

    Returns:
        float: Jevons price index.
    """
    matched_products = set(prices_0.keys()) & set(prices_t.keys())
    n = len(matched_products)

    if n == 0:
        raise ValueError("No matched products found.")

    product = 1.0
    for product_id in matched_products:
        product *= (prices_t[product_id] / prices_0[product_id]) ** (1 / n)

    return product


def dutot_index(prices_0: Dict[str, float], prices_t: Dict[str, float]) -> float:
    """
    Calculate the Dutot price index.

    Args:
        prices_0 (Dict[str, float]): Prices of products at time 0.
        prices_t (Dict[str, float]): Prices of products at time t.

    Returns:
        float: Dutot price index.
    """
    matched_products = set(prices_0.keys()) & set(prices_t.keys())

    if not matched_products:
        raise ValueError("No matched products found.")

    sum_prices_0 = sum(prices_0[product_id] for product_id in matched_products)
    sum_prices_t = sum(prices_t[product_id] for product_id in matched_products)

    return sum_prices_t / sum_prices_0


def carli_index(prices_0: Dict[str, float], prices_t: Dict[str, float]) -> float:
    """
    Calculate the Carli price index.

    Args:
        prices_0 (Dict[str, float]): Prices of products at time 0.
        prices_t (Dict[str, float]): Prices of products at time t.

    Returns:
        float: Carli price index.
    """
    matched_products = set(prices_0.keys()) & set(prices_t.keys())
    n = len(matched_products)

    if n == 0:
        raise ValueError("No matched products found.")

    sum_relatives = sum(
        prices_t[product_id] / prices_0[product_id] for product_id in matched_products
    )

    return sum_relatives / n


def bmw_index(prices_0: Dict[str, float], prices_t: Dict[str, float]) -> float:
    """
    Calculate the Balk-Mehrhoff-Walsh (BMW) price index.

    Args:
        prices_0 (Dict[str, float]): Prices of products at time 0.
        prices_t (Dict[str, float]): Prices of products at time t.

    Returns:
        float: BMW price index.
    """
    matched_products = set(prices_0.keys()) & set(prices_t.keys())

    if not matched_products:
        raise ValueError("No matched products found.")

    numerator = 0.0
    denominator = 0.0

    for product_id in matched_products:
        price_0 = prices_0[product_id]
        price_t = prices_t[product_id]
        price_ratio = price_t / price_0
        weight = (price_0 / price_t) ** 0.5

        numerator += price_ratio * weight
        denominator += weight

    if denominator == 0:
        raise ValueError("Denominator is zero, cannot compute BMW index.")

    return numerator / denominator


# ### Weighted Methods

# In[4]:


def laspeyres_index(
    prices_0: Dict[str, float],
    prices_t: Dict[str, float],
    quantities_0: Dict[str, float],
) -> float:
    """
    Calculate the Laspeyres price index.

    Args:
        prices_0 (Dict[str, float]): Prices of products at time 0.
        prices_t (Dict[str, float]): Prices of products at time t.
        quantities_0 (Dict[str, float]): Quantities of products at time 0.

    Returns:
        float: Laspeyres price index.
    """
    matched_products = (
        set(prices_0.keys()) & set(prices_t.keys()) & set(quantities_0.keys())
    )

    if not matched_products:
        raise ValueError("No matched products found.")

    numerator = sum(
        quantities_0[product_id] * prices_t[product_id]
        for product_id in matched_products
    )
    denominator = sum(
        quantities_0[product_id] * prices_0[product_id]
        for product_id in matched_products
    )

    return numerator / denominator


def paasche_index(
    prices_0: Dict[str, float],
    prices_t: Dict[str, float],
    quantities_t: Dict[str, float],
) -> float:
    """
    Calculate the Paasche price index.

    Args:
        prices_0 (Dict[str, float]): Prices of products at time 0.
        prices_t (Dict[str, float]): Prices of products at time t.
        quantities_t (Dict[str, float]): Quantities of products at time t.

    Returns:
        float: Paasche price index.
    """
    matched_products = (
        set(prices_0.keys()) & set(prices_t.keys()) & set(quantities_t.keys())
    )

    if not matched_products:
        raise ValueError("No matched products found.")

    numerator = sum(
        quantities_t[product_id] * prices_t[product_id]
        for product_id in matched_products
    )
    denominator = sum(
        quantities_t[product_id] * prices_0[product_id]
        for product_id in matched_products
    )

    return numerator / denominator


def fisher_index(
    prices_0: Dict[str, float],
    prices_t: Dict[str, float],
    quantities_0: Dict[str, float],
    quantities_t: Dict[str, float],
) -> float:
    """
    Calculate the Fisher price index.

    Args:
        prices_0 (Dict[str, float]): Prices of products at time 0.
        prices_t (Dict[str, float]): Prices of products at time t.
        quantities_0 (Dict[str, float]): Quantities of products at time 0.
        quantities_t (Dict[str, float]): Quantities of products at time t.

    Returns:
        float: Fisher price index.
    """
    laspeyres = laspeyres_index(prices_0, prices_t, quantities_0)
    paasche = paasche_index(prices_0, prices_t, quantities_t)

    return sqrt(laspeyres * paasche)


def tornqvist_index(
    prices_0: Dict[str, float],
    prices_t: Dict[str, float],
    quantities_0: Dict[str, float],
    quantities_t: Dict[str, float],
) -> float:
    """
    Calculate the Törnqvist price index.

    Args:
        prices_0 (Dict[str, float]): Prices of products at time 0.
        prices_t (Dict[str, float]): Prices of products at time t.
        quantities_0 (Dict[str, float]): Quantities of products at time 0.
        quantities_t (Dict[str, float]): Quantities of products at time t.

    Returns:
        float: Törnqvist price index.
    """
    matched_products = (
        set(prices_0.keys())
        & set(prices_t.keys())
        & set(quantities_0.keys())
        & set(quantities_t.keys())
    )

    if not matched_products:
        raise ValueError("No matched products found.")

    s_0 = {
        product_id: (prices_0[product_id] * quantities_0[product_id])
        for product_id in matched_products
    }
    s_t = {
        product_id: (prices_t[product_id] * quantities_t[product_id])
        for product_id in matched_products
    }
    total_0 = sum(s_0.values())
    total_t = sum(s_t.values())

    log_index = sum(
        ((s_0[product_id] / total_0 + s_t[product_id] / total_t) / 2)
        * log(prices_t[product_id] / prices_0[product_id])
        for product_id in matched_products
    )

    return exp(log_index)


def walsh_index(
    prices_0: Dict[str, float],
    prices_t: Dict[str, float],
    quantities_0: Dict[str, float],
    quantities_t: Dict[str, float],
) -> float:
    """
    Calculate the Walsh price index.

    Args:
        prices_0 (Dict[str, float]): Prices of products at time 0.
        prices_t (Dict[str, float]): Prices of products at time t.
        quantities_0 (Dict[str, float]): Quantities of products at time 0.
        quantities_t (Dict[str, float]): Quantities of products at time t.

    Returns:
        float: Walsh price index.
    """
    matched_products = (
        set(prices_0.keys())
        & set(prices_t.keys())
        & set(quantities_0.keys())
        & set(quantities_t.keys())
    )

    if not matched_products:
        raise ValueError("No matched products found.")

    numerator = sum(
        sqrt(quantities_0[product_id] * quantities_t[product_id]) * prices_t[product_id]
        for product_id in matched_products
    )
    denominator = sum(
        sqrt(quantities_0[product_id] * quantities_t[product_id]) * prices_0[product_id]
        for product_id in matched_products
    )

    return numerator / denominator


def sato_vartia_index(
    prices_0: Dict[str, float],
    prices_t: Dict[str, float],
    quantities_0: Dict[str, float],
    quantities_t: Dict[str, float],
) -> float:
    """
    Calculate the Sato-Vartia price index.

    Args:
        prices_0 (Dict[str, float]): Prices of products at time 0.
        prices_t (Dict[str, float]): Prices of products at time t.
        quantities_0 (Dict[str, float]): Quantities of products at time 0.
        quantities_t (Dict[str, float]): Quantities of products at time t.

    Returns:
        float: Sato-Vartia price index.
    """
    matched_products = (
        set(prices_0.keys())
        & set(prices_t.keys())
        & set(quantities_0.keys())
        & set(quantities_t.keys())
    )

    if not matched_products:
        raise ValueError("No matched products found.")

    s_0 = {
        product_id: (prices_0[product_id] * quantities_0[product_id])
        for product_id in matched_products
    }
    s_t = {
        product_id: (prices_t[product_id] * quantities_t[product_id])
        for product_id in matched_products
    }
    total_0 = sum(s_0.values())
    total_t = sum(s_t.values())

    phi = {}
    numerator = 0.0
    denominator = 0.0

    for product_id in matched_products:
        s0 = s_0[product_id] / total_0
        st = s_t[product_id] / total_t
        phi[product_id] = (st - s0) / (log(st) - log(s0))
        denominator += phi[product_id]

    for product_id in matched_products:
        phi[product_id] /= denominator
        numerator += phi[product_id] * log(prices_t[product_id] / prices_0[product_id])

    return exp(numerator)
