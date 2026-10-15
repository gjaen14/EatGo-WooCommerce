export type Category = 
  | 'hoy' 
  | 'desayunos' 
  | 'almuerzos' 
  | 'guarniciones' 
  | 'bebidas' 
  | 'postres';

export interface SideOption {
  id: string;
  name: string;
  extraPrice: number;
}

export interface BeverageOption {
  id: string;
  name: string;
  price: number;
}

export interface Dish {
  id: string;
  name: string;
  category: Category;
  description: string;
  price: number;
  image: string;
  badge?: string;
  isDailySpecial?: boolean;
  timeAvailable?: string;
  availableSides?: SideOption[];
  defaultSideId?: string;
  popular?: boolean;
}

export interface CartItem {
  cartItemId: string;
  dishId: string;
  name: string;
  basePrice: number;
  unitPrice: number;
  quantity: number;
  selectedSide?: string;
  selectedBeverage?: string;
  notes?: string;
  totalPrice: number;
}

export type DeliveryType = 'delivery' | 'pickup';

export type PaymentMethod = 'yappy' | 'tarjeta' | 'efectivo';

export type DayOfWeek = 'lunes' | 'martes' | 'miercoles' | 'jueves' | 'viernes' | 'sabado';

export interface OrderDetails {
  customerName: string;
  phone: string;
  deliveryType: DeliveryType;
  officeBuilding: string;
  floorOffice: string;
  deliveryTime: string;
  paymentMethod: PaymentMethod;
  notes: string;
}

export interface CorporatePackage {
  id: string;
  name: string;
  servings: number;
  price: number;
  description: string;
  includes: string[];
  image: string;
}
