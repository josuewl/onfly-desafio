"""Testes adicionais: precisão da conversão para BRL."""

from helpers import run_cli


def test_currency_conversion_is_exact_decimal(tmp_path):
    """A conversão passava por float; 0.75 * 5.42 = 4.065 virava 4.0649999... e arredondava para 4.06."""
    report = run_cli(tmp_path, [{"reservation_id": "R-1", "currency": "USD", "amount": "0.75"}])

    assert report["summary"]["total_amount_brl"] == "4.07"
    assert report["top_hotels"][0]["total_brl"] == "4.07"
    assert report["by_month"][0]["total_brl"] == "4.07"
