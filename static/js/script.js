document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {
      direction: 'left'
    });
  });

  function visibility(event) {
    let element = event.target.parentNode.parentNode;
    let input = element.querySelector("input");
    if (input.type === 'password') {
        input.type = 'text';
        event.target.classList.remove('fa-eye-slash');
        event.target.classList.add('fa-eye');
    } else {
        input.type = 'password';
        event.target.classList.remove('fa-eye');
        event.target.classList.add('fa-eye-slash');
    }
  }