$(document).foundation()

document.querySelector('h1').addEventListener('click', function(){
  alert("You poked an h1 header!");
});

document.querySelector('p').addEventListener('click', function(){
  alert("You poked a paragraph!");
});

document.querySelector('ol').addEventListener('click', function(){
  alert("You poked an ordered list!");
});

document.querySelector('ul').addEventListener('click', function(){
  alert("You poked an unordered list!!!!!!!!!!");
});

function confirmDeleteModal(id) {
  $('#deleteModal').modal();
  $('#deleteButton').html('<a href="?delete='+id+'" class="btn btn-danger" onclick="return closeDeleteModal('+id+')">Delete</a>');
}

function closeDeleteModal(id) {
  $('#deleteModal').modal('hide');
  return true
}
