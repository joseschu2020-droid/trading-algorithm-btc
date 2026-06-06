# trading-algorithm-btc
trading-algorithm-btc
# BTC Trading Strategy (SMA Crossover)

Este proyecto es una estrategia básica de trading algorítmico en Python.

## Objetivo

Analizar el precio de Bitcoin y generar señales de compra y venta usando medias móviles.

## Estrategia

- SMA20 (media móvil corta)
- SMA50 (media móvil larga)
- BUY cuando SMA20 cruza arriba de SMA50
- SELL cuando SMA20 cruza abajo de SMA50

## Tecnologías

- Python
- Pandas
- YFinance
- Matplotlib

## Cómo ejecutar

```bash
pip install -r requirements.txt
python main.py
