 $(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('.datepicker').datepicker({
      format: "dd mmmm, yyyy",
      yearRange: [1950,2006],
      defaultDate: "02 07, 1990",
      showClearBtn: true,
      i18n: {
        done: "Select"
      }
    });
  });