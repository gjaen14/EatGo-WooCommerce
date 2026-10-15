import { Dish, SideOption, BeverageOption } from '../types';
import { COMMON_SIDES, BEVERAGE_ADDONS } from './menuData';

export interface WeekDayDish extends Dish {
  boxedImage: string; // Photo of food neatly packed inside partitioned thermal box
  recommendedSide: string;
}

export interface WeekDayMenu {
  dayId: 'lunes' | 'martes' | 'miercoles' | 'jueves' | 'viernes' | 'sabado';
  dayName: string;
  theme: string;
  badge: string;
  description: string;
  dishes: WeekDayDish[];
}

export interface WeekSchedule {
  weekNumber: 1 | 2 | 3 | 4;
  title: string;
  subtitle: string;
  datesDescription: string;
  days: WeekDayMenu[];
}

// Fixed Breakfast Items (Repetidos diariamente confirmado por Mayra)
export const FIXED_BREAKFAST_ITEMS: WeekDayDish[] = [
  {
    id: 'des-hojaldre-bistec',
    name: 'Hojaldres Recién Fritas con Bistec Picado',
    category: 'desayunos',
    description: '2 hojaldres doradas y crocantes acompañadas de suave bistec de res salteado con cebolla, culantro fresco y ají dulce en su salsa.',
    price: 3.75,
    image: 'https://images.unsplash.com/photo-1541544741938-0af808871cc0?auto=format&fit=crop&w=800&q=80',
    boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
    badge: 'Favorito Panameño',
    timeAvailable: '6:30 AM - 11:00 AM',
    availableSides: [
      { id: 'extra_hojaldre', name: '1 Hojaldre Extra', extraPrice: 0.75 },
      { id: 'extra_queso_blanco', name: 'Porción Queso del País', extraPrice: 1.25 }
    ],
    recommendedSide: '2 Hojaldres Criollas',
    popular: true
  },
  {
    id: 'des-carimanola-combo',
    name: 'Carimañolas de Yuca con Carne Mechada (3 uds)',
    category: 'desayunos',
    description: 'Masa de yuca fresca suave por dentro y crujiente por fuera, rellena de abundante carne de res deshilachada sazonada con sofrito campesino.',
    price: 3.25,
    image: 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=800&q=80',
    boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
    badge: 'Crocantes de Yuca',
    timeAvailable: '6:30 AM - 11:00 AM',
    availableSides: [
      { id: 'chicheme', name: 'Chicheme Chorrerano Fresco', extraPrice: 1.75 },
      { id: 'cafe_negro', name: 'Café Antillano Caliente', extraPrice: 1.00 }
    ],
    recommendedSide: 'Chicheme Chorrerano',
    popular: true
  },
  {
    id: 'des-tortilla-huevo',
    name: 'Tortillas de Maíz Artesanal con Huevo y Salchicha Guisada',
    category: 'desayunos',
    description: '2 tortillas de maíz molido asadas y doradas con huevo al gusto y salchichas guisadas en tomate, culantro y pimentón criollo.',
    price: 3.50,
    image: 'https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=800&q=80',
    boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
    badge: 'Clásico de Fonda',
    timeAvailable: '6:30 AM - 11:00 AM',
    recommendedSide: 'Tortillas Asadas',
    popular: true
  },
  {
    id: 'des-higado-encebollado',
    name: 'Hígado Encebollado con Yuca al Vapor',
    category: 'desayunos',
    description: 'Tierno hígado de res salteado a fuego vivo con abundante cebolla morada, orégano y un toque de ají chombo dulce con yuca suave.',
    price: 4.00,
    image: 'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80',
    boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
    badge: 'Tradición Interiorana',
    timeAvailable: '6:30 AM - 11:00 AM',
    recommendedSide: 'Yuca al Mojo',
    popular: false
  },
  {
    id: 'des-chicheme-artesanal',
    name: 'Chicheme Chorrerano de Maíz Pilado (Botella 500ml)',
    category: 'desayunos',
    description: 'Bebida espesa tradicional de maíz dulce pilado, leche entera de primera, canela, nuez moscada y vainilla aromática bien fría.',
    price: 2.25,
    image: 'https://images.unsplash.com/photo-1517256064527-09c73fc73e38?auto=format&fit=crop&w=800&q=80',
    boxedImage: 'https://images.unsplash.com/photo-1551024709-8f23befc6f87?auto=format&fit=crop&w=800&q=80',
    badge: 'Receta Secreta Chorrerana',
    timeAvailable: 'Todo el Día',
    recommendedSide: 'Bien Frío',
    popular: true
  }
];

// SEMANAS 1, 2, 3 y 4 DEL CATÁLOGO INTERACTIVO
export const FOUR_WEEKS_DATA: WeekSchedule[] = [
  // ================= SEMANA 1 =================
  {
    weekNumber: 1,
    title: 'Semana 1: Fonda Clásica Panameña',
    subtitle: 'El repertorio fundamental de la cocina criolla de paila',
    datesDescription: 'Ciclo Semana 1 del Mes',
    days: [
      {
        dayId: 'lunes',
        dayName: 'Lunes',
        theme: 'Sopas & Fondas de Arranque',
        badge: '🥣 Día de Caldos Reconfortantes',
        description: 'Arranca la semana laboral con energía criolla y guisos reconfortantes de olla honda.',
        dishes: [
          {
            id: 's1-lun-sancocho',
            name: 'Sancocho Tradicional de Gallina de Patio',
            category: 'hoy',
            description: 'El rey indiscutible de Panamá: caldo espeso con ñame baboso, gallina suave y abundante culantro fresco cosechado.',
            price: 6.50,
            image: 'https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Plato Estrella',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_blanco',
            recommendedSide: 'Arroz Blanco Criollo',
            popular: true
          },
          {
            id: 's1-lun-mondongo',
            name: 'Mondongo a la Culantro con Papitas',
            category: 'hoy',
            description: 'Mondongo suave y limpio, estofado a fuego lento con salsa de tomate criollo, sofrito de culantro y papas en cubos.',
            price: 7.00,
            image: 'https://images.unsplash.com/photo-1547928576-b183fd4d1d29?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Especial Lunes',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_guandu',
            recommendedSide: 'Arroz con Guandú',
            popular: true
          },
          {
            id: 's1-lun-pollo-guisado',
            name: 'Pollo Guisado Campesino en Achiote',
            category: 'hoy',
            description: 'Presas de pollo marinadas con achiote natural del interior, orégano y pimentón, con salsa densa para bañar el arroz.',
            price: 6.00,
            image: 'https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Favorito Ejecutivo',
            availableSides: COMMON_SIDES,
            defaultSideId: 'tajadas',
            recommendedSide: 'Arroz Blanco y Tajadas',
            popular: true
          }
        ]
      },
      {
        dayId: 'martes',
        dayName: 'Martes',
        theme: 'Mondongo & Guisos Criollos',
        badge: '🥘 Sabores Profundos',
        description: 'Guisos tradicionales de larga cocción con salsas intensas y cortes magros.',
        dishes: [
          {
            id: 's1-mar-mondongo-garbanzo',
            name: 'Mondongo Criollo con Garbanzos y Chorizo',
            category: 'almuerzos',
            description: 'Receta de abuela con tiernos garbanzos españoles, chorizo tableño ahumado y mondongo en salsa espesa perfumada con laurel.',
            price: 7.25,
            image: 'https://images.unsplash.com/photo-1547928576-b183fd4d1d29?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Especial Martes',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_blanco',
            recommendedSide: 'Arroz Blanco y Patacones',
            popular: true
          },
          {
            id: 's1-mar-ropa-vieja',
            name: 'Ropa Vieja Criolla Deshilachada',
            category: 'almuerzos',
            description: 'Falda de res desmechada a mano salteada con cebolla caramelizada, pimentones dulces tricolores y salsa de tomate casera.',
            price: 7.00,
            image: 'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Clásico de Oficina',
            availableSides: COMMON_SIDES,
            defaultSideId: 'tajadas',
            recommendedSide: 'Arroz con Guandú y Tajadas',
            popular: true
          }
        ]
      },
      {
        dayId: 'miercoles',
        dayName: 'Miércoles',
        theme: 'Paila Criolla & Guachos',
        badge: '🍚 Mitad de Semana con Sabor',
        description: 'Arroces cocinados en calderos de hierro con sofritos intensos y carnes estofadas.',
        dishes: [
          {
            id: 's1-mie-arroz-pollo',
            name: 'Arroz con Pollo Chorrillero Tradicional',
            category: 'almuerzos',
            description: 'Arroz sazonado con achiote, deshilachado de pollo de patio, petit pois, aceitunas, pimentón asado y servido con ensalada de feria.',
            price: 6.50,
            image: 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Paila Festiva',
            availableSides: COMMON_SIDES,
            defaultSideId: 'ensalada_feria',
            recommendedSide: 'Ensalada de Feria y Plátano',
            popular: true
          },
          {
            id: 's1-mie-chuleta-criolla',
            name: 'Chuletas Ahumadas en Salsa de Piña y Ají Chombo',
            category: 'almuerzos',
            description: 'Chuletas jugosas a la plancha bañadas en compota de piña nacional glaseada con raspadura y un toque sutil de ají chombo.',
            price: 6.75,
            image: 'https://images.unsplash.com/photo-1432139555190-58524dae6a55?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Agridulce Criollo',
            availableSides: COMMON_SIDES,
            defaultSideId: 'yuca_frita',
            recommendedSide: 'Yuca al Vapor',
            popular: true
          }
        ]
      },
      {
        dayId: 'jueves',
        dayName: 'Jueves',
        theme: 'Pastas Criollas & Asados',
        badge: '🍝 Tradición con Fideos y Horno',
        description: 'La fusión panameña de pastas criollas con sofrito de fonda y pollos dorados al horno.',
        dishes: [
          {
            id: 's1-jue-macarrones',
            name: 'Macarrones Criollos con Pollo Guisado y Queso Blanco',
            category: 'almuerzos',
            description: 'Fideos macarrones largos envueltos en la salsa densa del pollo guisado con sofrito de culantro y coronados con queso del país rallado.',
            price: 6.50,
            image: 'https://images.unsplash.com/photo-1621996346565-e3adc644d946?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Clásico de Infancia',
            availableSides: COMMON_SIDES,
            defaultSideId: 'tajadas',
            recommendedSide: 'Tajadas Maduras',
            popular: true
          },
          {
            id: 's1-jue-pollo-horno',
            name: 'Pollo al Horno Glaseado con Papitas Doradas',
            category: 'almuerzos',
            description: 'Cuarto de pollo adobado con hierbas silvestres y mostaza criolla, horneado lentamente hasta lograr piel crujiente y carne jugosa.',
            price: 6.50,
            image: 'https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Opción Ligera',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_guandu',
            recommendedSide: 'Arroz con Guandú',
            popular: true
          }
        ]
      },
      {
        dayId: 'viernes',
        dayName: 'Viernes',
        theme: 'Mariscos & Pescados Caribeños',
        badge: '🐟 Sabor de Costas y Pescadores',
        description: 'Pescados frescos del Mercado del Marisco, fritos al momento o estofados al ajillo.',
        dishes: [
          {
            id: 's1-vie-corvina-frita',
            name: 'Corvina Frita al Estilo Chorrillo con Patacones',
            category: 'almuerzos',
            description: 'Filete o pescado entero marinado con limón criollo, ajo y sal de mar, frito a la perfección crocante con canasta de patacones.',
            price: 8.00,
            image: 'https://images.unsplash.com/photo-1534939561126-855b8675edd7?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Viernes de Pescado',
            availableSides: COMMON_SIDES,
            defaultSideId: 'patacones',
            recommendedSide: 'Patacones Crocantes con Mojo',
            popular: true
          },
          {
            id: 's1-vie-pescado-escabeche',
            name: 'Filete de Pescado al Escabeche Criollo',
            category: 'almuerzos',
            description: 'Pescado blanco dorado cubierto de cebollas salteadas en vinagre de frutas, mostaza criolla, pimentones y orégano.',
            price: 7.50,
            image: 'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Caribe Panameño',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_coco',
            recommendedSide: 'Arroz con Coco',
            popular: true
          }
        ]
      },
      {
        dayId: 'sabado',
        dayName: 'Sábado',
        theme: 'Paila Familiar de Fin de Semana',
        badge: '🍲 Almuerzo Tranquilo y Reconfortante',
        description: 'Sancochos espesos y parrillada criolla para disfrutar en familia o en guardia de oficina.',
        dishes: [
          {
            id: 's1-sab-sancocho-especial',
            name: 'Gran Sancocho de Gallina con Arroz Blanco y Aguacate',
            category: 'almuerzos',
            description: 'Olla festiva de fin de semana con gallina dorada, ñame tierno, mazorca de maíz tierno y porción de aguacate fresco.',
            price: 7.00,
            image: 'https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Revitalizador',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_blanco',
            recommendedSide: 'Arroz Blanco Criollo',
            popular: true
          }
        ]
      }
    ]
  },

  // ================= SEMANA 2 =================
  {
    weekNumber: 2,
    title: 'Semana 2: Tradición Campesina & Fogón',
    subtitle: 'Platos del interior con sofrito de leña y cortes estofados',
    datesDescription: 'Ciclo Semana 2 del Mes',
    days: [
      {
        dayId: 'lunes',
        dayName: 'Lunes',
        theme: 'Sopa de Costilla & Bistec',
        badge: '🥣 Caldos de Leña',
        description: 'Sopas profundas de costilla de res cargadas de vegetales criollos y carnes encebolladas.',
        dishes: [
          {
            id: 's2-lun-sopa-costilla',
            name: 'Sopa de Costilla de Res con Yuca y Maíz',
            category: 'hoy',
            description: 'Caldo sustancioso con costilla de res tierna que se desprende del hueso, yuca campesina, mazorcas dulces y culantro.',
            price: 6.75,
            image: 'https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Reconfortante',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_blanco',
            recommendedSide: 'Arroz Blanco',
            popular: true
          },
          {
            id: 's2-lun-bistec-encebollado',
            name: 'Bistec de Cinta Encebollado con Yuca al Mojo',
            category: 'hoy',
            description: 'Finos cortes de res tierna sellados a la plancha con montículo de cebolla morada encurtida en vinagre criollo y especias.',
            price: 7.00,
            image: 'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Muy Solicitado',
            availableSides: COMMON_SIDES,
            defaultSideId: 'yuca_frita',
            recommendedSide: 'Yuca al Mojo Criollo',
            popular: true
          }
        ]
      },
      {
        dayId: 'martes',
        dayName: 'Martes',
        theme: 'Mondongo & Pollo al Estilo Fonda',
        badge: '🍗 Sabor de Fonda del Interior',
        description: 'Mondongo sazonado con orégano silvestre y pollos crocantes dorados.',
        dishes: [
          {
            id: 's2-mar-mondongo-culantro',
            name: 'Mondongo Típico de la Abuela con Ají Dulce',
            category: 'almuerzos',
            description: 'Cocido de mondongo suave con papa criolla, achiote de grano y un sofrito balanceado de culantro y cebolla.',
            price: 7.00,
            image: 'https://images.unsplash.com/photo-1547928576-b183fd4d1d29?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Especial Martes',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_guandu',
            recommendedSide: 'Arroz con Guandú',
            popular: true
          },
          {
            id: 's2-mar-pollo-frito',
            name: 'Pollo Frito Dorado al Estilo Fonda Panameña',
            category: 'almuerzos',
            description: 'Presas sazonadas con mostaza, limón y especias locales, fritas hasta lograr un exterior crujiente y jugoso.',
            price: 6.25,
            image: 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Favorito Rápido',
            availableSides: COMMON_SIDES,
            defaultSideId: 'patacones',
            recommendedSide: 'Patacones y Ensalada',
            popular: true
          }
        ]
      },
      {
        dayId: 'miercoles',
        dayName: 'Miércoles',
        theme: 'Guachos & Estofados de Caldero',
        badge: '🍲 Guacho Panameño',
        description: 'El guacho criollo espeso cocido en fondo aromático con carnes desmenuzadas.',
        dishes: [
          {
            id: 's2-mie-guacho-rabito',
            name: 'Guacho Criollo de Rabito de Puerco y Frijol',
            category: 'almuerzos',
            description: 'Arroz caldoso espeso con rabito desalado, frijoles colorados, yuca y sofrito frito por encima en cuchara de palo.',
            price: 6.75,
            image: 'https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Auténtico Típico',
            availableSides: COMMON_SIDES,
            defaultSideId: 'tajadas',
            recommendedSide: 'Tajadas Maduras',
            popular: true
          },
          {
            id: 's2-mie-carne-guisada',
            name: 'Carne de Res Guisada con Papas y Zanahorias',
            category: 'almuerzos',
            description: 'Dados de carne tiernos en estofado tradicional con abundante salsa casera espesada naturalmente con las papas.',
            price: 6.75,
            image: 'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Clásico Semanal',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_blanco',
            recommendedSide: 'Arroz Blanco Criollo',
            popular: true
          }
        ]
      },
      {
        dayId: 'jueves',
        dayName: 'Jueves',
        theme: 'Lasaña Criolla & Asados',
        badge: '🧀 Fusión Panameña',
        description: 'Capas de sabor con toques dulces de plátano maduro y carnes asadas.',
        dishes: [
          {
            id: 's2-jue-lasana-platano',
            name: 'Pastelón Criollo de Carne con Plátano Maduro',
            category: 'almuerzos',
            description: 'Capas de plátano maduro horneado, carne molida especiada con pasitas y queso prensado derretido por encima.',
            price: 7.25,
            image: 'https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Especial del Chef',
            availableSides: COMMON_SIDES,
            defaultSideId: 'ensalada_feria',
            recommendedSide: 'Ensalada Verde o Feria',
            popular: true
          }
        ]
      },
      {
        dayId: 'viernes',
        dayName: 'Viernes',
        theme: 'Mariscos & Pargo Frito Entero',
        badge: '🦐 Mariscos Frescos',
        description: 'Pargo entero con su cola crujiente y camarones al ajillo criollo.',
        dishes: [
          {
            id: 's2-vie-pargo-frito',
            name: 'Pargo Rojo Entero Frito con Patacones',
            category: 'almuerzos',
            description: 'Pargo fresco entero sazonado con ajo y limón, frito crujiente servido con torre de patacones y salsa tártara criolla.',
            price: 8.50,
            image: 'https://images.unsplash.com/photo-1534939561126-855b8675edd7?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Plato Premium',
            availableSides: COMMON_SIDES,
            defaultSideId: 'patacones',
            recommendedSide: 'Patacones con Mojo',
            popular: true
          }
        ]
      },
      {
        dayId: 'sabado',
        dayName: 'Sábado',
        theme: 'Sancocho Trifásico Especial',
        badge: '🥩 Paila de 3 Carnes',
        description: 'Sancocho robusto con gallina de patio, costilla de res y rabito ahumado.',
        dishes: [
          {
            id: 's2-sab-trifasico',
            name: 'Sancocho Trifásico de Gallina, Res y Cerdo Ahumado',
            category: 'almuerzos',
            description: 'La máxima expresión del caldo interiorano: tres carnes hervidas a fuego bajo con yuca, ñame y culantro.',
            price: 7.50,
            image: 'https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Especial Sábado',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_blanco',
            recommendedSide: 'Arroz Blanco Criollo',
            popular: true
          }
        ]
      }
    ]
  },

  // ================= SEMANA 3 =================
  {
    weekNumber: 3,
    title: 'Semana 3: Recetas de la Abuela & Paila Brava',
    subtitle: 'Estofados ricos en sofrito de culantro y achiote en grano',
    datesDescription: 'Ciclo Semana 3 del Mes',
    days: [
      {
        dayId: 'lunes',
        dayName: 'Lunes',
        theme: 'Sopa de Lentejas & Ropa Vieja',
        badge: '🥣 Caldos Nutritivos',
        description: 'Lentejas cocidas con chorizo tableño ahumado y ropa vieja bien jugosa.',
        dishes: [
          {
            id: 's3-lun-lentejas-chorizo',
            name: 'Sopa de Lentejas Caseras con Chorizo Tableño',
            category: 'hoy',
            description: 'Lentejas cocinadas con sofrito de cebolla, pimentón y rodajas de chorizo tableño artesanal que aportan ahumado.',
            price: 6.25,
            image: 'https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Nutritivo y Caliente',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_blanco',
            recommendedSide: 'Arroz Blanco Criollo',
            popular: true
          },
          {
            id: 's3-lun-ropa-vieja-tajadas',
            name: 'Ropa Vieja en Salsa Roja con Tajadas',
            category: 'hoy',
            description: 'Falda de res estofada y deshebrada con orégano y salsa criolla de tomates maduros, dulce y suave.',
            price: 7.00,
            image: 'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Clásico Criollo',
            availableSides: COMMON_SIDES,
            defaultSideId: 'tajadas',
            recommendedSide: 'Arroz Blanco y Tajadas',
            popular: true
          }
        ]
      },
      {
        dayId: 'martes',
        dayName: 'Martes',
        theme: 'Mondongo & Chuletas Doradas',
        badge: '🥩 Carnes Criollas',
        description: 'Mondongo con salsa de la casa y chuletas doradas en sartén de hierro.',
        dishes: [
          {
            id: 's3-mar-mondongo-especial',
            name: 'Mondongo a la Cazuela con Papas y Zanahorias',
            category: 'almuerzos',
            description: 'Corte magro de mondongo marinado con naranja agria y cocinado a fuego lento hasta quedar sumamente tierno.',
            price: 7.00,
            image: 'https://images.unsplash.com/photo-1547928576-b183fd4d1d29?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Estrella Martes',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_guandu',
            recommendedSide: 'Arroz con Guandú',
            popular: true
          }
        ]
      },
      {
        dayId: 'miercoles',
        dayName: 'Miércoles',
        theme: 'Arroz con Puerco a la Leña',
        badge: '🍚 Paila Festiva',
        description: 'Arroz salteado con trozos de cerdo crujientes y achiote campesino.',
        dishes: [
          {
            id: 's3-mie-arroz-puerco',
            name: 'Arroz con Puerco a la Leña y Guandú Fresco',
            category: 'almuerzos',
            description: 'Paila honda de arroz perfumado con trocitos de puerco frito en su manteca, guandú oloroso y pimentón asado.',
            price: 6.75,
            image: 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Aroma Ahumado',
            availableSides: COMMON_SIDES,
            defaultSideId: 'ensalada_feria',
            recommendedSide: 'Ensalada de Feria',
            popular: true
          }
        ]
      },
      {
        dayId: 'jueves',
        dayName: 'Jueves',
        theme: 'Coditos Criollos con Carne & Pollo Asado',
        badge: '🍝 Pastas Caseras',
        description: 'Coditos bañados en salsa criolla con carne molida y queso del país.',
        dishes: [
          {
            id: 's3-jue-coditos-carne',
            name: 'Coditos Guisados con Carne Molida y Queso Blanco',
            category: 'almuerzos',
            description: 'Pastas cortas con sofrito denso de carne de res molida, orégano campesino y queso del país espolvoreado caliente.',
            price: 6.50,
            image: 'https://images.unsplash.com/photo-1621996346565-e3adc644d946?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Comida Reconfortante',
            availableSides: COMMON_SIDES,
            defaultSideId: 'tajadas',
            recommendedSide: 'Plátano Maduro',
            popular: true
          }
        ]
      },
      {
        dayId: 'viernes',
        dayName: 'Viernes',
        theme: 'Camarones al Ajillo & Corvina Caribeña',
        badge: '🦐 Sabor Costeño',
        description: 'Camarones frescos salteados en mantequilla, ajo machacado y culantro.',
        dishes: [
          {
            id: 's3-vie-camarones-ajillo',
            name: 'Camarones al Ajillo Criollo con Patacones',
            category: 'almuerzos',
            description: 'Camarones jugosos del Pacífico salteados con ajo natural, perejil y culantro fresco con reducción de vino blanco.',
            price: 8.50,
            image: 'https://images.unsplash.com/photo-1559742811-82286364ceaf?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Especial del Mar',
            availableSides: COMMON_SIDES,
            defaultSideId: 'patacones',
            recommendedSide: 'Patacones Crocantes',
            popular: true
          }
        ]
      },
      {
        dayId: 'sabado',
        dayName: 'Sábado',
        theme: 'Sancocho de Gallina Criolla',
        badge: '🍲 Tradición Pura',
        description: 'Caldo dorado con ñame baboso y cilantro de hoja ancha.',
        dishes: [
          {
            id: 's3-sab-sancocho-duro',
            name: 'Sancocho Tradicional de Gallina con Ñame Baboso',
            category: 'almuerzos',
            description: 'Receta de campo con gallina tierna, ñame que espesa naturalmente el caldo y arroz con guandú de acompañamiento.',
            price: 7.00,
            image: 'https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Fin de Semana Criollo',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_guandu',
            recommendedSide: 'Arroz con Guandú',
            popular: true
          }
        ]
      }
    ]
  },

  // ================= SEMANA 4 =================
  {
    weekNumber: 4,
    title: 'Semana 4: Sabores de Gala Criolla & Mar y Tierra',
    subtitle: 'Los platos más celebrados para cerrar el ciclo mensual con broche de oro',
    datesDescription: 'Ciclo Semana 4 del Mes',
    days: [
      {
        dayId: 'lunes',
        dayName: 'Lunes',
        theme: 'Sancocho de Entrada & Falda Estofada',
        badge: '🥣 Cierre Mensual Criollo',
        description: 'Falda de res estofada en su salsa con vegetales campesinos y caldo de entrada.',
        dishes: [
          {
            id: 's4-lun-falda-estofada',
            name: 'Falda de Res Estofada en Salsa Criolla con Ñame',
            category: 'hoy',
            description: 'Carne de res cocinada a fuego lentísimo hasta quedar suave como mantequilla, con salsa de pimentón asado y trozos de ñame.',
            price: 7.25,
            image: 'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Plato Fuerte',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_blanco',
            recommendedSide: 'Arroz Blanco y Tajadas',
            popular: true
          },
          {
            id: 's4-lun-pollo-horneado',
            name: 'Pollo Campesino Horneado al Culantro y Achiote',
            category: 'hoy',
            description: 'Cuarto de pollo adobado 24 horas con pasta de culantro y achiote puro de Azuero, asado con piel crocante.',
            price: 6.25,
            image: 'https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Favorito Ejecutivo',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_guandu',
            recommendedSide: 'Arroz con Guandú',
            popular: true
          }
        ]
      },
      {
        dayId: 'martes',
        dayName: 'Martes',
        theme: 'Mondongo a la Culantro & Albóndigas Criollas',
        badge: '🥘 Fonda Tradicional',
        description: 'Albóndigas de res con sofrito y el mondongo clásico de la casa.',
        dishes: [
          {
            id: 's4-mar-mondongo-casa',
            name: 'Mondongo a la Culantro de la Casa Eat & Go',
            category: 'almuerzos',
            description: 'Nuestra receta insigne de mondongo tierno con salsa de la casa, culantro fresco y papas suaves.',
            price: 7.00,
            image: 'https://images.unsplash.com/photo-1547928576-b183fd4d1d29?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Especial Martes',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_guandu',
            recommendedSide: 'Arroz con Guandú',
            popular: true
          },
          {
            id: 's4-mar-albondigas',
            name: 'Albóndigas de Res en Salsa de Tomate y Culantro',
            category: 'almuerzos',
            description: 'Suaves albóndigas de carne magra sazonadas con hierbas criollas, guisadas en salsa de tomate fresco.',
            price: 6.50,
            image: 'https://images.unsplash.com/photo-1529042410759-befb1204b468?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Casero Auténtico',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_blanco',
            recommendedSide: 'Arroz Blanco y Puré',
            popular: true
          }
        ]
      },
      {
        dayId: 'miercoles',
        dayName: 'Miércoles',
        theme: 'Paila de Cerdo & Porotos con Rabito',
        badge: '🍛 Paila Profunda',
        description: 'Porotos colorados estofados con rabito de cerdo y chuletas en salsa criolla.',
        dishes: [
          {
            id: 's4-mie-porotos-rabito',
            name: 'Porotos Colorados con Rabito y Arroz Blanco',
            category: 'almuerzos',
            description: 'Guiso cremoso de porotos con carne de rabito salada y desalada a punto, sofrito campesino y arroz blanco caliente.',
            price: 6.75,
            image: 'https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Potente y Típico',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_blanco',
            recommendedSide: 'Arroz Blanco y Tajadas',
            popular: true
          }
        ]
      },
      {
        dayId: 'jueves',
        dayName: 'Jueves',
        theme: 'Espaguetis Criollos & Chuletas Asadas',
        badge: '🍝 Fideos de Fonda',
        description: 'Espaguetis con chorizo tableño y salsa roja espesa de paila.',
        dishes: [
          {
            id: 's4-jue-espaguetis-chorizo',
            name: 'Espaguetis Criollos con Pollo Desmechado y Chorizo',
            category: 'almuerzos',
            description: 'Fideos entomatados al estilo panameño con pollo deshilachado, trocitos de chorizo artesanal y queso del país.',
            price: 6.50,
            image: 'https://images.unsplash.com/photo-1621996346565-e3adc644d946?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Tradición de Fonda',
            availableSides: COMMON_SIDES,
            defaultSideId: 'tajadas',
            recommendedSide: 'Tajadas de Plátano Maduro',
            popular: true
          }
        ]
      },
      {
        dayId: 'viernes',
        dayName: 'Viernes',
        theme: 'Mariscos al Ajillo & Pescado en Salsa de Coco',
        badge: '🥥 Sabor Caribeño con Coco',
        description: 'Filete de pescado bañado en leche de coco natural con ají chombo y culantro.',
        dishes: [
          {
            id: 's4-vie-pescado-coco',
            name: 'Filete de Corvina en Salsa Criolla de Coco y Culantro',
            category: 'almuerzos',
            description: 'Filete de pescado tierno sellado y bañado en reducción de leche de coco fresca con ají chombo dulce y culantro aromático.',
            price: 8.25,
            image: 'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Especial Caribeño',
            availableSides: COMMON_SIDES,
            defaultSideId: 'patacones',
            recommendedSide: 'Arroz con Coco y Patacones',
            popular: true
          }
        ]
      },
      {
        dayId: 'sabado',
        dayName: 'Sábado',
        theme: 'Fiesta Criolla de Paila Completa',
        badge: '🎉 Gran Cierre de Semana',
        description: 'Sancocho especial de paila con torrejitas de maíz y arroz con guandú.',
        dishes: [
          {
            id: 's4-sab-sancocho-fiesta',
            name: 'Gran Sancocho Interiorano con Arroz Blanco y Aguacate',
            category: 'almuerzos',
            description: 'Caldo supremo con gallina de patio, ñame tierno, torrejita de maíz y aguacate recién cortado.',
            price: 7.25,
            image: 'https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80',
            boxedImage: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80',
            badge: 'Reconfortante Supremo',
            availableSides: COMMON_SIDES,
            defaultSideId: 'arroz_blanco',
            recommendedSide: 'Arroz Blanco Criollo',
            popular: true
          }
        ]
      }
    ]
  }
];
