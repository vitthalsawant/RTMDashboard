import { Component, Input } from '@angular/core';
import { DashboardSummary } from '../../models/dashboard.model';

@Component({
  selector: 'app-kpi-cards',
  imports: [],
  templateUrl: './kpi-cards.html',
  styleUrl: './kpi-cards.css',
})
export class KpiCards {
  @Input() summary: DashboardSummary | null = null;
}
