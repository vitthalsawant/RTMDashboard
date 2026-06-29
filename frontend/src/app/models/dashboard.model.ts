export interface DashboardSummary {
  total_equipment: number;
  running_equipment: number;
  stopped_equipment: number;
  active_alerts: number;
}

export type EquipmentStatus = 'Running' | 'Stopped' | 'Maintenance';

export interface Equipment {
  id: number;
  name: string;
  status: EquipmentStatus;
  temperature: number;
  production: number;
}

export interface Alert {
  id: number;
  equipment_id: number;
  message: string;
}

export interface DashboardData {
  equipment: Equipment[];
  alerts: Alert[];
}

export interface ProductionItem {
  name: string;
  production: number;
}
