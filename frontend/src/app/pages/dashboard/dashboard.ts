import { Component } from '@angular/core';
import { Header } from '../../shared/header/header';
import { KpiCards } from '../../components/kpi-cards/kpi-cards';

@Component({
  selector: 'app-dashboard',
  imports: [Header, KpiCards],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css',
})
export class Dashboard {}
