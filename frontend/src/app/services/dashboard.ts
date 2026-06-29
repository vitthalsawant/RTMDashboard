import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { DashboardSummary, ProductionItem } from '../models/dashboard.model';

const API_URL = 'http://localhost:8000';

@Injectable({ providedIn: 'root' })
export class DashboardService {
  private http = inject(HttpClient);

  getSummary(): Observable<DashboardSummary> {
    return this.http.get<DashboardSummary>(`${API_URL}/dashboard`);
  }

  getProductionSummary(): Observable<ProductionItem[]> {
    return this.http.get<ProductionItem[]>(`${API_URL}/production-summary`);
  }
}
