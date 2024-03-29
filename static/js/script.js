document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.fixed-action-btn');
  var instances = M.FloatingActionButton.init(elems, {
    direction: 'left',
    hoverEnabled: false
  });
});

/* Code for toggle password visibility taken and edited from W3Schools */
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

function closeNav() {
  var elem = document.querySelector('.sidenav');
  var instance = M.Sidenav.getInstance(elem);
  instance.close();
}