import { Component, ElementRef, inject,  OnDestroy, viewChild  } from '@angular/core';
import { Chart } from 'chart.js/auto';
import { DashboardService } from '../../services/dashboard';
import { equipmentStatusDistribution, ProductionItem } from '../../models/dashboard.model';

@Component({
  selector: 'app-pie-chart',
  imports: [],
  templateUrl: './pie-chart.html',
  styleUrl: './pie-chart.css',
})
export class PieChart {
  private service =     inject(DashboardService);
  private chart?: Chart;

  open = false;
  canvas = viewChild<ElementRef<HTMLCanvasElement>>('canvas');

  openChart(): void {
    this.open = true;
    this.service.getequipmentStatusDistribution().subscribe((data) => {
      setTimeout(() => this.renderChart(data), 0);
    });
  }

  private renderChart(data: equipmentStatusDistribution[]): void {
    const el = this.canvas()?.nativeElement;
    if (!el) return;

    this.chart?.destroy();
    this.chart = new Chart(el, {
      type: 'pie',
      data: {
        labels: data.map((d) => d.status),
        datasets: [
          {
            label: 'Equipment Status Distribution',
            data: data.map((d) => d.count),
            backgroundColor: [
              '#0d6efd',
              '#198754',
              '#dc3545',
              '#ffc107',
              '#6c757d',
            ],
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
      },
    });
  } 

}
