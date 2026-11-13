"""Testes adicionais: desempate do ranking de hotéis."""

from helpers import run_cli


def test_top_hotels_tie_is_broken_by_hotel_id_ascending(tmp_path):
    """Com reverse=True o desempate por hotel_id ficava decrescente."""
    report = run_cli(
        tmp_path,
        [
            {"reservation_id": "R-1", "hotel_id": "H03", "hotel_name": "Hotel C", "amount": "500.00"},
            {"reservation_id": "R-2", "hotel_id": "H01", "hotel_name": "Hotel A", "amount": "500.00"},
            {"reservation_id": "R-3", "hotel_id": "H02", "hotel_name": "Hotel B", "amount": "900.00"},
        ],
    )

    assert [hotel["hotel_id"] for hotel in report["top_hotels"]] == ["H02", "H01", "H03"]
