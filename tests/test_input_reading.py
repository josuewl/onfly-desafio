"""Testes adicionais: leitura completa do arquivo de reservas."""

from helpers import run_cli


def test_reads_every_row_of_the_file(tmp_path):
    """O repositório parava de ler após 200 linhas, descartando reservas."""
    rows = [{"reservation_id": f"R-{index}"} for index in range(1, 251)]

    report = run_cli(tmp_path, rows)

    assert report["summary"]["total_reservations"] == 250
    assert report["summary"]["confirmed_reservations"] == 250
    assert report["summary"]["total_room_nights"] == 250
    assert report["summary"]["total_amount_brl"] == "25000.00"
