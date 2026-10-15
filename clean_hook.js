  // Sincronizar textos exactos en Home Cards (Platos Destacados)
  .text('MÁS VENDIDO OFICINAS');
  
  // Agregar icono bag.svg al boton Agregar en Home de forma limpia (sin duplicar)
  var bagSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:8px;"><path d="M3.4 5.467a2 2 0 0 0-.4 1.2V20a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6.667a2 2 0 0 0-.4-1.2l-2-2.667A2 2 0 0 0 17 2H7a2 2 0 0 0-1.6.8z"></path><path d="M3 6h18"></path><path d="M16 10a4 4 0 0 1-8 0"></path></svg>';
  
  .each(function() {
    var  = ;
    if (!.find('svg').length) {
      .find('.elementor-button-text').html(bagSvg + 'Agregar');
    }
  });