import { Component } from '@angular/core';
import { Header } from '../../shared/header/header';
import { KpiCards } from '../../components/kpi-cards/kpi-cards';
import { BarChart } from '../../components/bar-chart/bar-chart';
import { TrendChart } from '../../components/trend-chart/trend-chart';
import { PieChart } from '../../components/pie-chart/pie-chart';

@Component({
  selector: 'app-dashboard',
  imports: [Header, KpiCards, BarChart, TrendChart, PieChart],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css',
})
export class Dashboard {}
