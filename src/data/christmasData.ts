export interface ChristmasDish {
  id: string;
  name: string;
  category: 'cenas' | 'porciones' | 'guarniciones' | 'bebidas';
  description: string;
  price: number;
  unit: string;
  image: string;
  badge?: string;
  servingsInfo: string;
}

export interface ChristmasPackage {
  id: string;
  name: string;
  servings: number;
  price: number;
  description: string;
  includes: string[];
  image: string;
  badge: string;
}

export const CHRISTMAS_DISHES: ChristmasDish[] = [
  {
    id: 'nav-jamon-glaseado',
    name: 'Jamón Navideño Glaseado con Piña, Clavos y Raspadura',
    category: 'cenas',
    description: 'Pierna de jamón horneada a fuego lento, caramelizada con sirope artesanal de raspadura de caña, piña nacional confitada y clavos de olor aromáticos.',
    price: 85.00,
    unit: 'Pieza entera (aprox. 12-14 lbs)',
    image: 'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80',
    badge: '👑 El Rey de la Nochebuena',
    servingsInfo: 'Rinde para 12-15 personas'
  },
  {
    id: 'nav-pernil-asado',
    name: 'Pernil Criollo Asado a la Leña con Sofrito Criollo',
    category: 'cenas',
    description: 'Pernil de cerdo marinado 48 horas con ajo criollo, naranja agria, orégano silvestre y culantro, asado lentamente hasta quedar jugoso por dentro con cuero crujiente.',
    price: 78.00,
    unit: 'Pieza entera (aprox. 10-12 lbs)',
    image: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80',
    badge: '🔥 Sabor a Fogón Interiorano',
    servingsInfo: 'Rinde para 10-12 personas'
  },
  {
    id: 'nav-pavo-criollo',
    name: 'Pavo Horneado Criollo en Reducción de Oporto y Hierbas',
    category: 'cenas',
    description: 'Pavo entero sazonado con mantequilla de hierbas, vino oporto y especias criollas, acompañado de abundante gravy casero.',
    price: 92.00,
    unit: 'Pavo entero (aprox. 12-14 lbs)',
    image: 'https://images.unsplash.com/photo-1514944298352-f47225103407?auto=format&fit=crop&w=800&q=80',
    badge: 'Especial Navideño',
    servingsInfo: 'Rinde para 12-16 personas'
  },
  {
    id: 'nav-tamal-gallina',
    name: 'Tamales Tradicionales de Gallina Criolla de Patio (6 uds)',
    category: 'porciones',
    description: 'Masa de maíz nuevo pilado envuelta en hoja de bijao, rellena de abundante gallina criolla de patio, aceitunas, alcaparras, pimentón y pasitas.',
    price: 21.00,
    unit: 'Pack de 6 tamales grandes',
    image: 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80',
    badge: '100% Hoja de Bijao',
    servingsInfo: '6 personas ($3.50 c/u)'
  },
  {
    id: 'nav-arroz-pina',
    name: 'Bandeja de Arroz Navideño con Piña, Almendras y Pasas',
    category: 'guarniciones',
    description: 'Arroz esponjoso sazonado con caldo aromático, trocitos de piña confitada, almendras tostadas crujientes y pasitas rubias.',
    price: 24.00,
    unit: 'Bandeja familiar (aprox. 5 lbs)',
    image: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
    badge: 'Acompañante Clásico',
    servingsInfo: 'Rinde para 10-12 personas'
  },
  {
    id: 'nav-ensalada-feria',
    name: 'Bandeja de Ensalada de Feria Tradicional (Remolacha & Papa)',
    category: 'guarniciones',
    description: 'Clásica ensalada panameña festiva de remolacha dulce, papas suaves, zanahorias en cubitos, huevo duro y mayonesa criolla.',
    price: 20.00,
    unit: 'Bandeja familiar (aprox. 5 lbs)',
    image: 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80',
    badge: 'El Clásico Rosa',
    servingsInfo: 'Rinde para 10-12 personas'
  },
  {
    id: 'nav-ron-ponche',
    name: 'Ron Ponche Artesanal Panameño con Ron Abuelo (Botella 750ml)',
    category: 'bebidas',
    description: 'Receta de la casa con leche condensada, yemas de huevo, canela, nuez moscada y Ron Abuelo Añejo sellado al vacío.',
    price: 16.00,
    unit: 'Botella de vidrio 750ml',
    image: 'https://images.unsplash.com/photo-1517256064527-09c73fc73e38?auto=format&fit=crop&w=800&q=80',
    badge: 'Receta de la Abuela',
    servingsInfo: '5-6 copas generosas'
  },
  {
    id: 'nav-dulce-frutas',
    name: 'Dulce Criollo de Frutas Cristalizadas y Ron Añejo',
    category: 'bebidas',
    description: 'Panqué denso macerado 3 meses en ron añejo con higos, pasitas, nueces, cáscara de naranja confitada y ciruelas pasas.',
    price: 14.00,
    unit: 'Molde entero 1 lb',
    image: 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80',
    badge: 'Tradición Decembrina',
    servingsInfo: '8-10 porciones'
  }
];

export const CHRISTMAS_PACKAGES: ChristmasPackage[] = [
  {
    id: 'pack-nav-familiar',
    name: 'Banquete Navideño Familiar Nochebuena',
    servings: 10,
    price: 145.00,
    description: 'La cena completa lista para calentar y servir en Nochebuena o Fin de Año sin pasar todo el día cocinando.',
    includes: [
      'Jamón Navideño Glaseado con Piña y Raspadura (rebanado)',
      'Pernil Criollo Asado a la Leña (porciones jugosas)',
      'Bandeja grande de Arroz con Piña, Almendras y Pasitas',
      'Bandeja de Ensalada de Feria Tradicional',
      '10 Tamales Criollos de Gallina de Patio en Hoja de Bijao',
      '1 Botella de Ron Ponche Artesanal de la Casa (750ml)'
    ],
    image: 'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80',
    badge: 'Más Vendido para Familias'
  },
  {
    id: 'pack-nav-corporativo',
    name: 'Cena de Fin de Año Corporativa (25 Colaboradores)',
    servings: 25,
    price: 360.00,
    description: 'Empacado en bandejas térmicas de grado gastronómico o cajas troqueladas individuales con cubiertos festivos y factura con RUC.',
    includes: [
      'Pernil Asado a la Leña + Jamón Glaseado (2 proteínas por persona)',
      'Arroz Navideño con Almendras y Frutas',
      'Ensalada de Feria Tradicional',
      '25 Tamales de Gallina de Patio',
      '25 Porciones de Dulce de Frutas Navideño',
      '2 Botellas de Ron Ponche Artesanal',
      'Empaque térmico que mantiene el calor a 75°C hasta por 3 horas'
    ],
    image: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80',
    badge: 'Ideal para Oficinas'
  },
  {
    id: 'pack-nav-gala-licitacion',
    name: 'Gran Banquete Navideño B2B / Institucional (50 a 300 Pax)',
    servings: 50,
    price: 675.00,
    description: 'Servicio formal tipo buffet asistido con rechauds de acero inoxidable, personal uniformado o 50 cajas ejecutivas troqueladas.',
    includes: [
      'Menú completo de 3 tiempos navideños con 2 proteínas principales',
      'Estación de bebidas navideñas (chichas naturales y ponche)',
      'Tamales artesanales certificados en inocuidad alimentaria MINSA',
      'Facturación fiscal con RUC y DV / Aceptación Panamá Compra',
      'Transporte térmico garantizado en horario estricto'
    ],
    image: 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=800&q=80',
    badge: 'Contratos & Licitaciones'
  }
];
