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
