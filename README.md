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

18-06-2026

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

Header creted in shared folder -
import header in dashboard -
import header in app.ts -
import dashboard in approute.ts -

19-06-2026

image added in header
as per header hight and width i set the hight width for image in header.css 

Top 4 - ( show only count )

 - Total equipment
  - Running
  - Stopped
  - Active Alert

  
below 3 ( After click open chart )

  - Temperature Trend
  - equipment status distrubution
  - production summary

<img width="1916" height="1074" alt="image" src="https://github.com/user-attachments/assets/f551b070-69ec-4fda-9c9b-5b8d1ffc0f71" />




## Author

[Vitthal Sawant](https://github.com/vitthalsawant)
