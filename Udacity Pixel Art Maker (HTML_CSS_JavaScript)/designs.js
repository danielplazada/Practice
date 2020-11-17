function makeGrid() {
    var gridHeight = document.getElementById('inputHeight').value;
    var gridWidth = document.getElementById('inputWidth').value;
    var mainGrid = document.getElementById('pixelCanvas');
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
