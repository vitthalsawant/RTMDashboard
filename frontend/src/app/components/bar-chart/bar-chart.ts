import { Component, ElementRef, inject, OnDestroy, viewChild } from '@angular/core';
import { Chart } from 'chart.js/auto';
import { DashboardService } from '../../services/dashboard';
import { ProductionItem } from '../../models/dashboard.model';

@Component({
  selector: 'app-bar-chart',
  imports: [],
  templateUrl: './bar-chart.html',
  styleUrl: './bar-chart.css',
})
export class BarChart implements OnDestroy {
  private service = inject(DashboardService);
  private chart?: Chart;

  open = false;
  canvas = viewChild<ElementRef<HTMLCanvasElement>>('canvas');

  openChart(): void {
    this.open = true;
    this.service.getProductionSummary().subscribe((data) => {
      setTimeout(() => this.renderChart(data), 0);
    });
  }

  ngOnDestroy(): void {
    this.chart?.destroy();
  }

  private renderChart(data: ProductionItem[]): void {
    const el = this.canvas()?.nativeElement;
    if (!el) return;

    this.chart?.destroy();
    this.chart = new Chart(el, {
      type: 'bar',
      data: {
        labels: data.map((d) => d.name),
        datasets: [
          {
            label: 'Production',
            data: data.map((d) => d.production),
            backgroundColor: '#0d6efd',
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
