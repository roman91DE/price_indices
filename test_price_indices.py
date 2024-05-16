#!/usr/bin/env python
# coding: utf-8

import unittest
from typing import Dict
import pandas as pd

from price_indices import *

class TestPriceIndices(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create test data
        cls.prices_0: Dict[str, float] = {
            "product_1": 100.0,
            "product_2": 200.0,
            "product_3": 300.0,
        }
        cls.prices_t: Dict[str, float] = {
            "product_1": 110.0,
            "product_2": 190.0,
            "product_3": 310.0,
        }
        cls.quantities_0: Dict[str, float] = {
            "product_1": 10.0,
            "product_2": 20.0,
            "product_3": 30.0,
        }
        cls.quantities_t: Dict[str, float] = {
            "product_1": 15.0,
            "product_2": 25.0,
            "product_3": 35.0,
        }
        # Create DataFrame
        cls.df = pd.DataFrame(
            {
                PD_DEFAULT_PRODUCT_ID_COL: ["product_1", "product_2", "product_3"]
                * 2,
                PD_DEFAULT_PRICE_COL: [100.0, 200.0, 300.0, 110.0, 190.0, 310.0],
                PD_DEFAULT_QUANTITY_COL: [10.0, 20.0, 30.0, 15.0, 25.0, 35.0],
                PD_DEFAULT_TIME_PERIOD_COL: [0, 0, 0, 1, 1, 1],
            }
        )

    def test_jevons_index(self):
        native_index = jevons_index(
            self.prices_0, self.prices_t, DEFAULT_NORMALIZATION_VAL
        )
        df_index = jevons_index_from_df(
            self.df,
            base_period=0,
            compared_period=1,
            price_col=PD_DEFAULT_PRICE_COL,
            product_id_col=PD_DEFAULT_PRODUCT_ID_COL,
            time_period_col=PD_DEFAULT_TIME_PERIOD_COL,
            normalization_value=DEFAULT_NORMALIZATION_VAL,
        )
        self.assertAlmostEqual(native_index, df_index, places=5)

    def test_dutot_index(self):
        native_index = dutot_index(
            self.prices_0, self.prices_t, DEFAULT_NORMALIZATION_VAL
        )
        df_index = dutot_index_from_df(
            self.df,
            base_period=0,
            compared_period=1,
            price_col=PD_DEFAULT_PRICE_COL,
            product_id_col=PD_DEFAULT_PRODUCT_ID_COL,
            time_period_col=PD_DEFAULT_TIME_PERIOD_COL,
            normalization_value=DEFAULT_NORMALIZATION_VAL,
        )
        self.assertAlmostEqual(native_index, df_index, places=5)

    def test_carli_index(self):
        native_index = carli_index(
            self.prices_0, self.prices_t, DEFAULT_NORMALIZATION_VAL
        )
        df_index = carli_index_from_df(
            self.df,
            base_period=0,
            compared_period=1,
            price_col=PD_DEFAULT_PRICE_COL,
            product_id_col=PD_DEFAULT_PRODUCT_ID_COL,
            time_period_col=PD_DEFAULT_TIME_PERIOD_COL,
            normalization_value=DEFAULT_NORMALIZATION_VAL,
        )
        self.assertAlmostEqual(native_index, df_index, places=5)

    def test_bmw_index(self):
        native_index = bmw_index(
            self.prices_0, self.prices_t, DEFAULT_NORMALIZATION_VAL
        )
        df_index = bmw_index_from_df(
            self.df,
            base_period=0,
            compared_period=1,
            price_col=PD_DEFAULT_PRICE_COL,
            product_id_col=PD_DEFAULT_PRODUCT_ID_COL,
            time_period_col=PD_DEFAULT_TIME_PERIOD_COL,
            normalization_value=DEFAULT_NORMALIZATION_VAL,
        )
        self.assertAlmostEqual(native_index, df_index, places=5)

    def test_laspeyres_index(self):
        native_index = laspeyres_index(
            self.prices_0, self.prices_t, self.quantities_0, DEFAULT_NORMALIZATION_VAL
        )
        df_index = laspeyres_index_from_df(
            self.df,
            base_period=0,
            compared_period=1,
            price_col=PD_DEFAULT_PRICE_COL,
            quantity_col=PD_DEFAULT_QUANTITY_COL,
            product_id_col=PD_DEFAULT_PRODUCT_ID_COL,
            time_period_col=PD_DEFAULT_TIME_PERIOD_COL,
            normalization_value=DEFAULT_NORMALIZATION_VAL,
        )
        self.assertAlmostEqual(native_index, df_index, places=5)

    def test_paasche_index(self):
        native_index = paasche_index(
            self.prices_0, self.prices_t, self.quantities_t, DEFAULT_NORMALIZATION_VAL
        )
        df_index = paasche_index_from_df(
            self.df,
            base_period=0,
            compared_period=1,
            price_col=PD_DEFAULT_PRICE_COL,
            quantity_col=PD_DEFAULT_QUANTITY_COL,
            product_id_col=PD_DEFAULT_PRODUCT_ID_COL,
            time_period_col=PD_DEFAULT_TIME_PERIOD_COL,
            normalization_value=DEFAULT_NORMALIZATION_VAL,
        )
        self.assertAlmostEqual(native_index, df_index, places=5)

    def test_fisher_index(self):
        native_index = fisher_index(
            self.prices_0,
            self.prices_t,
            self.quantities_0,
            self.quantities_t,
            DEFAULT_NORMALIZATION_VAL,
        )
        df_index = fisher_index_from_df(
            self.df,
            base_period=0,
            compared_period=1,
            price_col=PD_DEFAULT_PRICE_COL,
            quantity_col=PD_DEFAULT_QUANTITY_COL,
            product_id_col=PD_DEFAULT_PRODUCT_ID_COL,
            time_period_col=PD_DEFAULT_TIME_PERIOD_COL,
            normalization_value=DEFAULT_NORMALIZATION_VAL,
        )
        self.assertAlmostEqual(native_index, df_index, places=5)

    def test_tornqvist_index(self):
        native_index = tornqvist_index(
            self.prices_0,
            self.prices_t,
            self.quantities_0,
            self.quantities_t,
            DEFAULT_NORMALIZATION_VAL,
        )
        df_index = tornqvist_index_from_df(
            self.df,
            base_period=0,
            compared_period=1,
            price_col=PD_DEFAULT_PRICE_COL,
            quantity_col=PD_DEFAULT_QUANTITY_COL,
            product_id_col=PD_DEFAULT_PRODUCT_ID_COL,
            time_period_col=PD_DEFAULT_TIME_PERIOD_COL,
            normalization_value=DEFAULT_NORMALIZATION_VAL,
        )
        self.assertAlmostEqual(native_index, df_index, places=5)

    def test_walsh_index(self):
        native_index = walsh_index(
            self.prices_0,
            self.prices_t,
            self.quantities_0,
            self.quantities_t,
            DEFAULT_NORMALIZATION_VAL,
        )
        df_index = walsh_index_from_df(
            self.df,
            base_period=0,
            compared_period=1,
            price_col=PD_DEFAULT_PRICE_COL,
            quantity_col=PD_DEFAULT_QUANTITY_COL,
            product_id_col=PD_DEFAULT_PRODUCT_ID_COL,
            time_period_col=PD_DEFAULT_TIME_PERIOD_COL,
            normalization_value=DEFAULT_NORMALIZATION_VAL,
        )
        self.assertAlmostEqual(native_index, df_index, places=5)

    def test_sato_vartia_index(self):
        native_index = sato_vartia_index(
            self.prices_0,
            self.prices_t,
            self.quantities_0,
            self.quantities_t,
            DEFAULT_NORMALIZATION_VAL,
        )
        df_index = sato_vartia_index_from_df(
            self.df,
            base_period=0,
            compared_period=1,
            price_col=PD_DEFAULT_PRICE_COL,
            quantity_col=PD_DEFAULT_QUANTITY_COL,
            product_id_col=PD_DEFAULT_PRODUCT_ID_COL,
            time_period_col=PD_DEFAULT_TIME_PERIOD_COL,
            normalization_value=DEFAULT_NORMALIZATION_VAL,
        )
        self.assertAlmostEqual(native_index, df_index, places=5)


unittest.main()
