import { AsyncPipe } from '@angular/common';
import { Component, inject } from '@angular/core';
import { Header } from '../../shared/header/header';
import { KpiCards } from '../../components/kpi-cards/kpi-cards';
import { BarChart } from '../../components/bar-chart/bar-chart';
import { TrendChart } from '../../components/trend-chart/trend-chart';
import { PieChart } from '../../components/pie-chart/pie-chart';
import { DashboardService } from '../../services/dashboard';

@Component({
  selector: 'app-dashboard',
  imports: [Header, KpiCards, BarChart, TrendChart, PieChart, AsyncPipe],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css',
})
export class Dashboard {
  private dashboardService = inject(DashboardService);

  summary$ = this.dashboardService.getSummary();
}