var game = {
  user: '',
  computer: '',
  currentPlayer: '',
  moves: 1,
};

function setFig(id) {
  if (id === 'x') {
    game.user = '<span class="fa fa-times"></span>';
    game.computer = '<span class="far fa-circle"></span>';
  } else if (id === 'o') {
    game.user = '<span class="far fa-circle"></span>';
    game.computer = '<span class="fa fa-times"></span>';
  }
  firstMove();
  setCurrPl('user');
}

function firstMove() {
  $('#fifth').html(game.computer);
  $('#fifth').removeAttr('onClick');
}

function setCurrPl(curr) {
  game.currentPlayer = curr;
}

function icon(id) {
  if (game.currentPlayer == 'user') {
    $('#' + id).html(game.user);
    $('#' + id).removeAttr('onClick');
    gameStatus();
    setCurrPl('computer');
  } else if (game.currentPlayer == 'computer') {
    $('#' + id).html(game.computer);
    $('#' + id).removeAttr('onClick');
    gameStatus();
    setCurrPl('user');
  }
  game.moves++;
  if (game.moves === 9) {
    draw()
  }

  if (game.currentPlayer == 'computer') {
    comp();
  }
};

function comp() {
  switch (true) {
    case $('#first').html() != game.user && $('#first').html() != game.computer:
      icon('first');
      break;
    case $('#second').html() !== game.user && $('#second').html() !== game.computer:
      icon('second');
      break;
    case $('#third').html() !== game.user && $('#third').html() !== game.computer:
      icon('third');
      break;
    case $('#fourth').html() !== game.user && $('#fourth').html() !== game.computer:
      icon('fourth');
      break;
    case $('#fifth').html() !== game.user && $('#fifth').html() !== game.computer:
      icon('fifth');
      break;
    case $('#sixth').html() !== game.user && $('#sixth').html() !== game.computer:
      icon('sixth');
      break;
    case $('#seventh').html() !== game.user && $('#seventh').html() !== game.computer:
      icon('seventh');
      break;
    case $('#eight').html() !== game.user && $('#eight').html() !== game.computer:
      icon('eight');
      break;
    case $('nineth').html() !== game.user && $('#nineth').html() !== game.computer:
      icon('nineth');
      break;
  }
};

function gameStatus() {
  var curPlayer;

  if (game.currentPlayer == 'user') {
    curPlayer = game.user;
  } else if (game.currentPlayer == 'computer') {
    curPlayer = game.computer;
  }

  switch (true) {
    case $('#first').html() === curPlayer && $('#second').html() === curPlayer &&
    $('#third').html() === curPlayer:
      show('#first', '#second', '#third');
      break;
    case $('#fourth').html() === curPlayer && $('#fifth').html() === curPlayer &&
    $('#sixth').html() === curPlayer:
      show('#fourth', '#fifth', '#sixth');
      break;
    case $('#seventh').html() === curPlayer && $('#eight').html() === curPlayer &&
    $('#nineth').html() === curPlayer:
      show('#seventh', '#eight', '#nineth');
      break;
    case $('#first').html() === curPlayer && $('#fourth').html() === curPlayer &&
    $('#seventh').html() === curPlayer:
      show('#first', '#fourth', '#seventh');
      break;
    case $('#second').html() === curPlayer && $('#fifth').html() === curPlayer &&
    $('#eight').html() === curPlayer:
      show('#second', '#fifth', '#eight');
      break;
    case $('#third').html() === curPlayer && $('#sixth').html() === curPlayer &&
    $('#nineth').html() === curPlayer:
      show('#third', '#sixth', '#nineth');
      break;
    case $('#first').html() === curPlayer && $('#fifth').html() === curPlayer &&
    $('#nineth').html() === curPlayer:
      show('#first', '#fifth', '#nineth');
      break;
    case $('#third').html() === curPlayer && $('#fifth').html() === curPlayer &&
    $('#seventh').html() === curPlayer:
      show('#third', '#fifth', '#seventh');
      break;
    default:
      draw();
  }
};

function show(x, y, z) {
  var x = $(x),
    y = $(y),
    z = $(z);
  x.addClass('win');
  y.addClass('win');
  z.addClass('win');
  lockAll();
  setTimeout(reset, 1500);
}

function reset() {
  $('.game-field').html('');
  game.moves = 1;
  $('.game-field').attr('onClick', 'icon(this.id)');
  $('.win').removeClass('win');
  setTimeout(firstMove, 200);
}

function start() {
    $('#myModal').modal('show')
};

function draw() {
    console.log('draw')
};

$(document).ready(function() {
    // Show the Modal on load
    $("#myModal").modal("show")
});