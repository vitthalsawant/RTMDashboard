import { Component, ElementRef, inject,  OnDestroy, viewChild } from '@angular/core';
import { ProductionItem, temperatureDistribution } from '../../models/dashboard.model';
import { Chart } from 'chart.js/auto';
import { DashboardService } from '../../services/dashboard';

@Component({
  selector: 'app-trend-chart',
  imports: [],
  templateUrl: './trend-chart.html',
  styleUrl: './trend-chart.css',
})
export class TrendChart {
  private service = inject(DashboardService);
  private chart?: Chart;

  open = false;
  canvas = viewChild<ElementRef<HTMLCanvasElement>>('canvas');

  openChart(): void {
    this.open = true;
    this.service.getTemperatureDistribution().subscribe((data) => {
      setTimeout(() => this.renderChart(data), 0);
    });
  }

  private renderChart(data: temperatureDistribution[]): void {
    const el = this.canvas()?.nativeElement;
    if (!el) return;

    this.chart?.destroy();
    this.chart = new Chart(el, {
      type: 'line',
      data: {
        labels: data.map((d) => d.name),
        datasets: [
          {
            label: 'Temperature Trend',
            data: data.map((d) => d.temperature),
            backgroundColor: '#0d6efd',
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            title: {
              display: true,
              text: 'Machine Name',
            },
          },
          y: {
            title: {
              display: true,
              text: 'Temperature (°C) ',
            },
            beginAtZero: true,
          },
        },
      },
    });
  }   
}
