import { Dish, SideOption, BeverageOption, CorporatePackage } from '../types';

export const COMMON_SIDES: SideOption[] = [
  { id: 'arroz_guandu', name: 'Arroz con Guandú Oloroso', extraPrice: 0.50 },
  { id: 'arroz_blanco', name: 'Arroz Blanco Criollo', extraPrice: 0.00 },
  { id: 'tajadas', name: 'Tajadas de Plátano Maduro', extraPrice: 0.00 },
  { id: 'patacones', name: 'Patacones Crujientes (3 uds)', extraPrice: 0.50 },
  { id: 'ensalada_feria', name: 'Ensalada de Feria (Remolacha & Papa)', extraPrice: 0.25 },
  { id: 'lentejas', name: 'Lentejas Criollas Estofadas', extraPrice: 0.00 },
];

export const BEVERAGE_ADDONS: BeverageOption[] = [
  { id: 'raspadura', name: 'Chicha de Raspadura con Limón (500ml Sellada)', price: 2.00 },
  { id: 'maracuya', name: 'Chicha de Maracuyá Natural (500ml Sellada)', price: 2.25 },
  { id: 'nance', name: 'Chicha de Nance Criollo (500ml Sellada)', price: 2.25 },
  { id: 'agua', name: 'Agua Purificada (500ml)', price: 1.25 },
];

export const DISHES: Dish[] = [
  // 1. Menú de Hoy (Almuerzos criollos del día)
  {
    id: 'mondongo-culantro',
    name: 'Mondongo a la Culantro con Papas',
    category: 'hoy',
    description: 'Tierno mondongo cocido a fuego lento con sofrito criollo de culantro coyote, ají chombo suave y papas en salsa espesa.',
    price: 7.00,
    image: 'https://images.unsplash.com/photo-1547928576-b183fd4d1d29?auto=format&fit=crop&w=800&q=80',
    badge: 'Plato Estrella de Hoy',
    isDailySpecial: true,
    availableSides: COMMON_SIDES,
    defaultSideId: 'arroz_blanco',
    popular: true,
  },
  {
    id: 'pollo-guisado',
    name: 'Pollo Guisado Criollo',
    category: 'hoy',
    description: 'Presas de pollo jugosas marinadas en achiote campesino, cebolla morada, orégano y pimentones frescos en reducción criolla.',
    price: 6.50,
    image: 'https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=800&q=80',
    badge: 'Más Vendido Oficinas',
    isDailySpecial: true,
    availableSides: COMMON_SIDES,
    defaultSideId: 'arroz_guandu',
    popular: true,
  },
  {
    id: 'corvina-frita',
    name: 'Corvina Frita al Ajillo Criollo',
    category: 'hoy',
    description: 'Filete de corvina fresca dorada al punto crocante con costra ligera de ajo, limón mandarina y culantro fresco.',
    price: 8.75,
    image: 'https://images.unsplash.com/photo-1534939561126-855b8675edd7?auto=format&fit=crop&w=800&q=80',
    badge: 'Fresco del Día',
    isDailySpecial: true,
    availableSides: COMMON_SIDES,
    defaultSideId: 'patacones',
  },
  {
    id: 'sancocho-criollo',
    name: 'Sancocho Criollo Tradicional',
    category: 'hoy',
    description: 'El clásico caldo panameño de gallina con ñame baboso cocido en su punto, aromatizado con abundante culantro fresco.',
    price: 6.00,
    image: 'https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80',
    badge: 'Reconfortante',
    isDailySpecial: true,
    availableSides: [
      { id: 'arroz_blanco', name: 'Arroz Blanco de Acompañamiento', extraPrice: 0.00 },
      { id: 'arroz_guandu', name: 'Arroz con Guandú', extraPrice: 0.50 },
    ],
    defaultSideId: 'arroz_blanco',
    popular: true,
  },

  // 2. Desayunos Fijos (Desde las 6:30 AM)
  {
    id: 'bistec-encebollado',
    name: 'Bistec Encebollado Criollo',
    category: 'desayunos',
    description: 'Corte fino de res sellado y cubierto con abundante cebolla caramelizada en salsa de tomate criolla.',
    price: 5.50,
    image: 'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80',
    badge: 'Desde 6:30 a.m.',
    timeAvailable: '6:30 a.m. - 11:00 a.m.',
    availableSides: [
      { id: 'hojaldre_2', name: '2 Hojaldres Calientes', extraPrice: 1.50 },
      { id: 'tortilla_2', name: '2 Tortillas de Maíz', extraPrice: 1.50 },
      { id: 'patacones_3', name: '3 Patacones Crujientes', extraPrice: 1.50 },
    ],
    defaultSideId: 'hojaldre_2',
    popular: true,
  },
  {
    id: 'combo-canalero',
    name: 'Combo Desayuno Canalero',
    category: 'desayunos',
    description: 'Bistec encebollado jugoso acompañado de 2 hojaldres recién fritas y café criollo con leche.',
    price: 6.75,
    image: 'https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80',
    badge: 'Completo Express',
    timeAvailable: '6:30 a.m. - 11:00 a.m.',
    popular: true,
  },
  {
    id: 'hojaldre-unidad',
    name: 'Hojaldre Criolla Dorada',
    category: 'desayunos',
    description: 'Masa tradicional aireada, dorada y crujiente por fuera con centro suave. Hecha al momento.',
    price: 1.25,
    image: 'https://images.unsplash.com/photo-1621996346565-e3d5d6281691?auto=format&fit=crop&w=800&q=80',
    badge: 'Crujiente',
    timeAvailable: 'Desde 6:30 a.m.',
  },
  {
    id: 'carimanola-yuca',
    name: 'Carimañola de Yuca con Carne',
    category: 'desayunos',
    description: 'Yuca fresca machacada y rellena de carne picada sazonada con sofrito criollo, frita a punto de oro.',
    price: 1.75,
    image: 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80',
    badge: 'Artesanal',
    timeAvailable: 'Desde 6:30 a.m.',
  },
  {
    id: 'tortilla-maiz',
    name: 'Tortilla de Maíz Criollo Frita',
    category: 'desayunos',
    description: 'Tortilla gruesa de puro maíz amarillo del interior, textura crocante exterior y tierna por dentro.',
    price: 1.50,
    image: 'https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=800&q=80',
    timeAvailable: 'Desde 6:30 a.m.',
  },
  {
    id: 'empanada-queso',
    name: 'Empanada de Maíz con Queso del País',
    category: 'desayunos',
    description: 'Empanada de masa de maíz recién moldeada y rellena de queso blanco artesanal fundente.',
    price: 1.60,
    image: 'https://images.unsplash.com/photo-1608039829572-78524f79c4c7?auto=format&fit=crop&w=800&q=80',
    timeAvailable: 'Desde 6:30 a.m.',
  },

  // 3. Almuerzos Criollos Ejecutivos Adicionales
  {
    id: 'carne-ropa-vieja',
    name: 'Ropa Vieja en Salsa Criolla',
    category: 'almuerzos',
    description: 'Falda de res deshilachada a mano, estofada con pimentones morrones, cebollas y sofrito tradicional.',
    price: 7.25,
    image: 'https://images.unsplash.com/photo-1588166524941-3bf61a9c41db?auto=format&fit=crop&w=800&q=80',
    badge: 'Favorito',
    availableSides: COMMON_SIDES,
    defaultSideId: 'arroz_guandu',
  },
  {
    id: 'chuleta-ahumada',
    name: 'Chuleta Ahumada al Achiote y Piña',
    category: 'almuerzos',
    description: 'Gruesa chuleta ahumada sellada con glaseado criollo de piña dulce, ajo asado y especias.',
    price: 6.75,
    image: 'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80',
    availableSides: COMMON_SIDES,
    defaultSideId: 'arroz_guandu',
  },

  // 4. Guarniciones Extras
  {
    id: 'porcion-arroz-guandu',
    name: 'Porción Extra Arroz con Guandú',
    category: 'guarniciones',
    description: 'Cocido con leche de coco y guandú fresco oloroso según la receta de fonda tradicional.',
    price: 2.00,
    image: 'https://images.unsplash.com/photo-1516684732162-798a0062be99?auto=format&fit=crop&w=800&q=80',
  },
  {
    id: 'porcion-tajadas',
    name: 'Orden de Tajadas de Plátano Maduro',
    category: 'guarniciones',
    description: 'Plátano maduro en su punto dulce cortado en tiras y caramelizado a fuego lento (4 unidades).',
    price: 1.50,
    image: 'https://images.unsplash.com/photo-1628294895950-9805252327bc?auto=format&fit=crop&w=800&q=80',
  },
  {
    id: 'porcion-patacones',
    name: 'Orden de Patacones con Sal Marina',
    category: 'guarniciones',
    description: 'Plátano verde prensado al momento y frito a doble cocción para máxima crocancia (4 unidades).',
    price: 2.00,
    image: 'https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=800&q=80',
  },
  {
    id: 'porcion-ensalada-feria',
    name: 'Ensalada de Feria Tradicional',
    category: 'guarniciones',
    description: 'Papa suave y remolacha cocida con mayonesa casera y un toque suave de mostaza criolla.',
    price: 1.75,
    image: 'https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80',
  },

  // 5. Bebidas Selladas (Sin derrames)
  {
    id: 'chicha-raspadura',
    name: 'Chicha de Raspadura con Limón (500ml)',
    category: 'bebidas',
    description: 'Panela de caña auténtica disuelta en frío con zumo de limón fresco. Botella PET sellada con tapa de seguridad.',
    price: 2.00,
    image: 'https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?auto=format&fit=crop&w=800&q=80',
    badge: '100% Sellada Antiderrame',
    popular: true,
  },
  {
    id: 'chicha-maracuya',
    name: 'Chicha de Maracuyá Natural (500ml)',
    category: 'bebidas',
    description: 'Pulpa de maracuyá fresca recién colada y endulzada al punto exacto. Empaque sellado de fábrica para oficina.',
    price: 2.25,
    image: 'https://images.unsplash.com/photo-1556881286-fc6915169721?auto=format&fit=crop&w=800&q=80',
    badge: '100% Sellada Antiderrame',
  },
  {
    id: 'chicha-nance',
    name: 'Chicha de Nance Criollo (500ml)',
    category: 'bebidas',
    description: 'Sabor auténtico del campo panameño preparado con nances macerados y azúcar morena.',
    price: 2.25,
    image: 'https://images.unsplash.com/photo-1622483767028-3f66f32aef97?auto=format&fit=crop&w=800&q=80',
    badge: '100% Sellada Antiderrame',
  },

  // 6. Postres
  {
    id: 'pesada-nance',
    name: 'Pesada de Nance con Queso Blanco',
    category: 'postres',
    description: 'Tradicional postre caliente/tibio a base de pulpa de nance espesada con fécula y trozos generosos de queso del país.',
    price: 2.75,
    image: 'https://images.unsplash.com/photo-1551024709-8f23befc6f87?auto=format&fit=crop&w=800&q=80',
    badge: 'Tradición Interiorana',
  },
  {
    id: 'manjar-blanco',
    name: 'Porción de Manjar Blanco Casero',
    category: 'postres',
    description: 'Dulce de leche panameño elaborado en paila de cobre hasta obtener su textura densa y acaramelada.',
    price: 2.50,
    image: 'https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=800&q=80',
  }
];

export const CORPORATE_PACKAGES: CorporatePackage[] = [
  {
    id: 'corp-5',
    name: 'Bandeja Ejecutiva Express (5 Personas)',
    servings: 5,
    price: 32.50,
    description: 'Diseñado para almuerzos rápidos de equipo de trabajo en oficina con entrega sincronizada a las 12:00 MD.',
    includes: [
      '5 Almuerzos a elegir (Pollo Guisado, Mondongo o Chuleta)',
      '5 Guarniciones individuales (Arroz con Guandú + Tajadas)',
      '5 Chichas frías selladas (Raspadura con limón o Maracuyá)',
      '5 Sets de cubiertos biodegradables + servilletas',
      'Empaque térmico master trilaminado caliente garantizado'
    ],
    image: 'https://images.unsplash.com/photo-1555244162-803834f70033?auto=format&fit=crop&w=800&q=80'
  },
  {
    id: 'corp-10',
    name: 'Paquete Directorio / Reunión (10 Personas)',
    servings: 10,
    price: 63.00,
    description: 'Perfecto para capacitaciones, comités y directivas que necesitan comida criolla de alta calidad sin interrupciones.',
    includes: [
      '10 Almuerzos ejecutivos con proteínas variadas',
      '10 Acompañamientos premium a elección',
      '10 Bebidas selladas de 500ml',
      '10 Postres criollos individuales (Pesada o Manjar)',
      'Factura fiscal electrónica inmediata para contabilidad de empresa',
      'Despacho puntual y entrega directa en recepción de oficina'
    ],
    image: 'https://images.unsplash.com/photo-1541544741938-0af808871cc0?auto=format&fit=crop&w=800&q=80'
  }
];

export const PACKAGING_BENEFITS = [
  {
    title: 'Troquelado Antiderrame',
    desc: 'Bandejas compartimentadas con sello perimetral rígido para que la salsa del guisado jamás toque las tajadas ni el arroz.',
    icon: 'ShieldCheck'
  },
  {
    title: 'Barrera Térmica 75°C',
    desc: 'Mantiene la temperatura ideal de cocción desde nuestra paila hasta tu cubículo sin necesidad de microondas.',
    icon: 'Flame'
  },
  {
    title: 'Botellas PET Selladas con Precinto',
    desc: 'Chichas naturales embotelladas y tapadas a rosca con anillo de seguridad. Cero goteos en mochilas o ascensores.',
    icon: 'PackageCheck'
  },
  {
    title: 'Cero Fila - Retiro o Despacho',
    desc: 'Tu comanda sale etiquetada con tu nombre y piso de oficina. Llegar, tomar y disfrutar sin perder tiempo de almuerzo.',
    icon: 'Clock'
  }
];
