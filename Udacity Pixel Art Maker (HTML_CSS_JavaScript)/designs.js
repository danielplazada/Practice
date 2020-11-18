function makeGrid() {
    var gridHeight = document.getElementById('inputHeight').value;
    //GridHeight to store the grid hieightfrom user input
    var gridWidth = document.getElementById('inputWidth').value;
     //GridWidth to store the grid width for user input
    var mainGrid = document.getElementById('pixelCanvas');
    //mainGrid that will show up on the screen
    mainGrid.innerHTML = '';
    for (let x = 0; x < gridHeight; x++) {
      let row = mainGrid.insertRow(x);

      for (let y = 0; y < gridWidth; y++) {
        let cell = row.insertCell(y);

        cell.addEventListener('click', function(event) {

        event.target.style.backgroundColor = document.getElementById('colorPicker').value;
        });
      }
    }
  }

    document.getElementById('sizePicker').addEventListener('submit', function(event) {
    event.preventDefault();
    makeGrid();
  });
