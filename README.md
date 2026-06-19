# RTM Dashboard

A database foundation for a **Real-Time Monitoring (RTM) Dashboard** that tracks industrial equipment status, temperature, production output, and related alerts.

## Overview

This project provides the PostgreSQL schema and seed data for monitoring factory machines. Each piece of equipment has a status (`Running`, `Stopped`, or `Maintenance`), temperature, and production metrics. Alerts are linked to specific equipment and surface operational issues.


## Database Schema

- 16/06/2026 to 18/06/2026

### `equipment`

| Column        | Type           | Description                               |
|---------------|----------------|-------------------------------------------|
| `id`          | SERIAL         | Primary key                               |
| `name`        | VARCHAR(100)   | Equipment name (e.g. Machine A)           |
| `status`      | VARCHAR(50)    | `Running`, `Stopped`, or `Maintenance`    |
| `temperature` | NUMERIC(6,2)   | Current temperature                       |
| `production`  | NUMERIC(10,2)  | Production output                         |

### `alerts`

| Column         | Type           | Description                    |
|----------------|----------------|--------------------------------|
| `id`           | SERIAL         | Primary key                    |
| `equipment_id` | INTEGER        | Foreign key → `equipment(id)`  |
| `message`      | VARCHAR(255)   | Alert description              |

Deleting an equipment row cascades to its alerts (`ON DELETE CASCADE`).

## Designing/Setup Frontend structure using commands 
- 18/06/2026

ng new frontend
cd frontend 


ng g c components/kpi-cards

ng g c components/trend-chart

ng g c components/pie-chart

ng g c components/bar-chart

ng g s services/dashboard


mkdir src/app/models

src/app/models/dashboard.model.ts

ng g c pages/dashboard

mkdir src/app/shared

ng g c shared/header

npm install bootstrap

## Author

[Vitthal Sawant](https://github.com/vitthalsawant)
