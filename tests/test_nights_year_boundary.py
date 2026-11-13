"""Testes adicionais: noites de quarto na virada de ano."""

from helpers import run_cli


def test_nights_across_year_boundary_use_checkin_month(tmp_path):
    """Noites na virada de ano e agrupamento pelo mês do check-in."""
    report = run_cli(
        tmp_path,
        [{"reservation_id": "R-1", "checkin_date": "2024-12-30", "checkout_date": "2025-01-02", "rooms": "2"}],
    )

    assert report["summary"]["total_room_nights"] == 6
    assert report["by_month"] == [
        {"month": "2024-12", "reservations": 1, "room_nights": 6, "total_brl": "100.00"}
    ]
