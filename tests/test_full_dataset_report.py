"""Testes adicionais: regressão ponta a ponta no dataset real."""

import csv

from helpers import PROJECT_ROOT, run_cli


def test_full_dataset_report(tmp_path):
    """Dataset real (300 linhas); valores conferidos por cálculo independente das regras do README.

    As linhas do CSV real já trazem todas as colunas, então o run_cli não aplica nenhum valor do BASE; e a
    tabela de câmbio que ele grava é idêntica a data/taxas_cambio.csv.
    """
    with (PROJECT_ROOT / "data" / "reservas_hoteis.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    report = run_cli(tmp_path, rows)

    assert report["report_version"] == "1.0"
    assert report["generated_at"].endswith("-03:00")
    assert report["summary"] == {
        "total_reservations": 300,
        "confirmed_reservations": 235,
        "cancelled_reservations": 31,
        "no_show_reservations": 34,
        "total_room_nights": 1347,
        "total_amount_brl": "396170.00",
        "average_nightly_rate_brl": "294.11",
    }
    assert report["by_month"] == [
        {"month": "2024-12", "reservations": 35, "room_nights": 174, "total_brl": "61335.80"},
        {"month": "2025-01", "reservations": 37, "room_nights": 235, "total_brl": "64662.89"},
        {"month": "2025-02", "reservations": 26, "room_nights": 138, "total_brl": "45991.09"},
        {"month": "2025-03", "reservations": 39, "room_nights": 215, "total_brl": "65984.99"},
        {"month": "2025-04", "reservations": 21, "room_nights": 146, "total_brl": "31335.97"},
        {"month": "2025-05", "reservations": 39, "room_nights": 196, "total_brl": "63507.98"},
        {"month": "2025-06", "reservations": 38, "room_nights": 243, "total_brl": "63351.29"},
    ]
    assert report["top_hotels"] == [
        {"hotel_id": "H06", "hotel_name": "Hotel Salvador Centro", "room_nights": 160, "total_brl": "45165.46"},
        {"hotel_id": "H10", "hotel_name": "Hotel Madrid, Gran Vía", "room_nights": 120, "total_brl": "45041.69"},
        {"hotel_id": "H12", "hotel_name": "Hotel Miami Beach", "room_nights": 106, "total_brl": "41647.69"},
        {"hotel_id": "H07", "hotel_name": "Hotel Brasília Tower", "room_nights": 148, "total_brl": "39920.52"},
        {"hotel_id": "H11", "hotel_name": "Hotel Buenos Aires", "room_nights": 102, "total_brl": "37455.69"},
    ]
