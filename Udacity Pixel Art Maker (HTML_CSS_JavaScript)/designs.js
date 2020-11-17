function makeGrid() {
    var gridY = document.getElementById('inputHeight').value;
    var gridX = document.getElementById('inputWidth').value;
    var mainGrid = document.getElementById('pixelCanvas');

    for (let x = 0; x < gridY; x++) {
      let row = mainGrid.insertRow(x);

      for (let y = 0; y < gridX; y++) {
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